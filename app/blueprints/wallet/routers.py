from flask import render_template
from . import wallet_bp


@wallet_bp.route('/')
def wallet():
    # template is located under app/blueprints/wallet/templates/balance.html
    return render_template('balance.html')