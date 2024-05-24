from app import db

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)
    business_type = db.Column(db.String(128), nullable=False)

class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'))
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(256))

class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(256))

class MachineBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_type = db.Column(db.String(128), nullable=False)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'))
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'))
    booking_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(128), default='Pending')

class WeatherInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    info = db.Column(db.String(256), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'))
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmer.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(128), default='Pending')
    
