from flask import render_template
from . import wallet_bp

@wallet_bp.route('/')
def wallet():
    return render_template('/balance.html' )