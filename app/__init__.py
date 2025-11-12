from .blueprints.verify import verify_bp
from .blueprints.wallet import wallet_bp
from .blueprints.auth import auth_bp
from flask import Flask, render_template
from .extension import db


def create_app():
    app = Flask(__name__)

    # Simple local sqlite file; move to `config.py` or ENV for production
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.db'

    # Initialize extensions
    db.init_app(app)

    @app.route('/login')
    def login():
        # blueprint-local template will be found by Flask's loader
        return render_template('login.html')

    @app.route('/')
    def home():
        return render_template('base.html')

    app.register_blueprint(verify_bp, url_prefix='/verify')
    app.register_blueprint(wallet_bp, url_prefix='/wallet')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app