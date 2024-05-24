from app.models import db, Farmer, Product, MachineBooking, WeatherInfo, Machine, Order, Business
from datetime import datetime
from app.weather import fetch_weather_forecast

def handle_ussd_request(phone_number, text):
    response = ""
    farmer = Farmer.query.filter_by(phone_number=phone_number).first()

    if not farmer:
        if text == "":
            response = "CON Welcome to Farmers Connect. Please register.\n"
            response += "Enter your name:"
        elif "*" not in text:
            name = text
            farmer = Farmer(name=name, phone_number=phone_number)
            db.session.add(farmer)
            db.session.commit()
            response = "END Registration successful. Please dial again to use the services."
        else:
            response = "END Invalid input. Please try again."
    else:
        if text == "":
            response = "CON Welcome to Farmers Connect\n"
            response += "1. Marketplace\n"
            response += "2. Market Products\n"
            response += "3. Book Machines\n"
            response += "4. Check Weather\n"
            response += "5. View orders/bookings"
        elif text == "1":
            response = "CON Marketplace\n"
            products = Product.query.all()
            for product in products:
                response += f"{product.id}. {product.name} - ${product.price}\n"
            response += "0. Back"
        elif text.startswith("1*"):
            # Process order request
            try:
                _, id = text.split("*")
                product_id = int(id)
                product = Product.query.get(product_id)
                if product:
                    # Store the product ID in the session
                    response += f"{product.name} - ${product.price}\n"
                    response += "1. Confirm Order\n"
                    response += "0. Cancel Order"
                else:
                    response = "END Product not found."
                
            except ValueError:
                    response = "END Invalid input. Please try again."
                
        elif text.count('*') > 2 and text.split("*")[-1] == "1":
            # Confirm order
            order = Order(farmer_id=farmer.id, product_id=product.id, quantity=1, total=product.price, order_date=datetime.now())
            db.session.add(order)
            db.session.commit()
            response = "END Your order has been confirmed successfully!"
        elif text == "1*0":
            # Cancel order
            response = "END Order cancelled."

            
        elif text == "0":
            # Go back to main menu
            response = "CON Welcome to Farmers Connect\n"
            response += "1. Marketplace\n"
            response += "2. Book Machines\n"
            response += "3. Check Weather"
        elif text == "2":
            response = "CON Market Your Products\n"
            response += "Enter product name, price, and description separated by commas:"
        elif text == "2":
            machine = Machine.query.all()
            response = "CON Book Machines\n"
            response += "Available Machines:\n"
            for m in machine:
                response += f"{m.name}: ${m.price_per_day}\n"
            response += "Enter machine type and booking date (YYYY-MM-DD) separated by a comma:"
        elif text.startswith("3*"):
            try:
                _, booking = text.split("*")
                machine_type, booking_date = booking.split(",")
                booking = datetime.strptime(booking_date, '%Y-%m-%d').date()
                booking = MachineBooking(machine_type=machine_type, booking_date=booking, farmer_id=farmer.id)
                db.session.add(booking)
                db.session.commit()
                response = "END Your machine booking has been successful!"
            except ValueError:
                response = "END Invalid input format. Please try again."
        elif text == "4":
            response = "CON Weather Information\n"
            weather_data = fetch_weather_forecast()
            if weather_data:
                for forecast in weather_data['list']:
                    date_time = forecast['dt_txt']
                    temperature = forecast['main']['temp']
                    weather_desc = forecast['weather'][0]['description']
                    response += f"Date/Time: {date_time}, Temperature: {temperature}°C, Weather: {weather_desc}\n"
                    weather = WeatherInfo(date=date_time , info=f"{temperature}°C, {weather_desc}")
            else:
                response += "No weather data available."
            if weather:
                response += f"Date: {weather.date}\nInfo: {weather.info}"
            else:
                response += "No weather information available."
        elif text == "5":
            response = "CON View Orders/Bookings\n"
            orders = Order.query.filter_by(farmer_id=farmer.id).all()
            bookings = MachineBooking.query.filter_by(farmer_id=farmer.id).all()
            response += "Orders:\n"
            if orders:
                for order in orders:
                    product = Product.query.get(order.product_id)
                    response += f"{product.name} - {order.quantity} units\n"
            else:
                response += "No orders available."
            response += "\nBookings:\n"
            if bookings:
                for booking in bookings:
                    response += f"{booking.machine_type} - {booking.booking_date}\n"
            else:
                response += "No bookings available."
            response += "0. Back"
        elif text == "0":
            response = "CON Welcome to Farmers Connect\n"
            response += "1. Marketplace\n"
            response += "2. Market Products\n"
            response += "3. Book Machines\n"
            response += "4. Check Weather"
        else:
            response = "END Invalid input. Please try again."

    return response


def handle_business_request(phone_number, text):
    response = ""
    business = Business.query.filter_by(phone_number=phone_number).first()

    if not business:
        if text == "":
            response = "CON Welcome to Farmers Connect. Please register.\n"
            response += "Enter your business name:"
        elif "*" not in text:
            name = text
            business = Business(name=name, phone_number=phone_number)
            db.session.add(business)
            db.session.commit()
            response = "END Registration successful. Please dial again to use the services."
        else:
            response = "END Invalid input. Please try again."
    else:
        if text == "":
            response = "CON Welcome to Farmers Connect\n"
            response += "1. Add products to inventory\n"
            response += "2. View orders\n"
            response += "3. Add machines to inventory\n"
            response += "4. View bookings\n"
        elif text == "1":
            response = "CON Add Products to Inventory\n"
            response += "Enter product name, price, and description separated by commas:"
        elif text.startswith("1*"):
            try:
                _, product_description = text.split("*")
                name, price, description = product_description.split(",")
                price = float(price)
                product = Product(name=name, price=price, description=description, business_id=business.id)
                db.session.add(product)
                db.session.commit()
                response = "END Product added to inventory successfully!"
            except ValueError:
                response = "END Invalid input format. Please try again."
        elif text == "2":
            response = "CON View Orders\n"
            orders = Order.query.filter_by(business_id=business.id).all()
            for order in orders:
                product = Product.query.get(order.product_id)
                response += f"{product.name} - {order.quantity} units\n"
            response += "0. Back"
        elif text == "3":
            response = "CON Add Machines to Inventory\n"
            response += "Enter machine name, price per day, and description separated by commas:"
        elif text.startswith("3*"):
            try:
                _, machine_description = text.split("*")
                name, price_per_day, description = machine_description.split(",")
                price_per_day = float(price_per_day)
                machine = Machine(name=name, price_per_day=price_per_day, description=description)
                db.session.add(machine)
                db.session.commit()
                response = "END Machine added to inventory successfully!"
            except ValueError:
                response = "END Invalid input format. Please try again."
        elif text == "4":
            response = "CON View Bookings\n"
            bookings = MachineBooking.query.filter_by(business_id=business.id).all()
            for booking in bookings:
                response += f"{booking.machine_type} - {booking.booking_date}\n"
            response += "0. Back"

        else:
            response = "END Invalid input. Please try again."