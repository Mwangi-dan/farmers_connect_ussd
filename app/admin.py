from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import db
from app.models import Farmer, Product, MachineBooking, WeatherInfo, Machine, Order

def setup_admin(app):
    admin = Admin(app, name='Farmers Connect Admin', template_mode='bootstrap3')

    admin.add_view(ModelView(Farmer, db.session))
    admin.add_view(ModelView(Product, db.session))
    admin.add_view(ModelView(Machine, db.session))
    admin.add_view(ModelView(MachineBooking, db.session))
    admin.add_view(ModelView(WeatherInfo, db.session))
    admin.add_view(ModelView(Order, db.session))
