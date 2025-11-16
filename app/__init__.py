from .blueprints.verify import verify_bp
from .blueprints.wallet import wallet_bp
from .blueprints.auth import auth_bp
from flask import Flask, render_template
from .extension import db
import os



def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'SecurePay.db')

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/')
    def home():
        return render_template('base.html')

    app.register_blueprint(verify_bp, url_prefix='/verify')
    app.register_blueprint(wallet_bp, url_prefix='/wallet')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app