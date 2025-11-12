from .extension import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name
