from flask_sqlalchemy import SQLAlchemy

# Centralized extension instances. Import `db` from other modules instead of
# instantiating SQLAlchemy(app=...) inside the factory.
db = SQLAlchemy()
