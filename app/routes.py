from flask import Blueprint, request, jsonify
from app.models import db, Farmer, Product, MachineBooking, WeatherInfo
from app.ussd import handle_ussd_request, handle_business_request

bp = Blueprint('ussd', __name__)

@bp.route('/ussd', methods=['POST'])
def ussd():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "")

    response = handle_ussd_request(phone_number, text)

    return response

@bp.route('/business', methods=['POST'])
def business():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "")

    response = handle_business_request(phone_number, text)

    return response
