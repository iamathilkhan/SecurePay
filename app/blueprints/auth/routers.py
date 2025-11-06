from flask import render_template
from . import auth_bp

@auth_bp.route('/')
def auth():
    return render_template('/signup.html')