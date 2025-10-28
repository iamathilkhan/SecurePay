from flask import Blueprint

verify_bp = Blueprint('verify', __name__, template_folder='templates', static_folder='static')

from . import routers