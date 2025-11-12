from flask import render_template
from . import auth_bp


@auth_bp.route('/')
def auth():
    # template is located under app/blueprints/auth/templates/signup.html
    return render_template('signup.html')

