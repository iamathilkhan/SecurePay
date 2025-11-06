from app.blueprints.verify import verify_bp
from app.blueprints.wallet import wallet_bp
from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template('base.html')

    app.register_blueprint(verify_bp, url_prefix='/verify')
    app.register_blueprint(wallet_bp, url_prefix='/wallet')
    app.register_blueprint()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug = True)