from .blueprints.verify import verify_bp
from .blueprints.wallet import wallet_bp
from .blueprints.auth import auth_bp
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users'

    db = SQLAlchemy(app=app)

    class Users(db.Model):
        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String, nullable = False)
        email = db.Column(db.String, nullable = False)

        def __repr__(self):
            return '<Name %r>'% self.name

    @app.route('/')
    def home():
        return render_template('/base.html')

    app.register_blueprint(verify_bp, url_prefix='/verify')
    app.register_blueprint(wallet_bp, url_prefix='/wallet')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app