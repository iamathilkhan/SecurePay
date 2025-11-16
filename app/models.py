from .extension import db


class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(60), nullable = False)
    email = db.Column(db.String(100),unique = True , nullable=False)
    loginTrack = db.Column(db.DateTime(), nullable = False)
    activity = db.Column(db.String(10), nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Bio(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer(), db.ForeignKey('users.id') ,nullable = False) 
    face = db.Column(db.LargeBinary, nullable = False)
    voice = db.Column(db.LargeBinary, nullable = False)

class Transaction(db.Model):
    transactionId = db.Column(db.Integer, primary_key = True)
    dtime = db.Column(db.DateTime(), nullable = False)
    userId = db.Column(db.Integer(), db.ForeignKey('users.id') ,nullable = False) 
    amount = db.Column(db.Integer(), nullable = False)
    receiverId = db.Column(db.Integer(), db.ForeignKey('users.id') ,nullable = False) 

class Verification(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    authId = db.Column(db.Integer(), db.ForeignKey('users.id') ,nullable = False)
    status = db.Column(db.String(10), nullable = False)
    userId = db.Column(db.Integer(), db.ForeignKey('users.id') ,nullable = False) 
    time = db.Column(db.DateTime(), nullable = False)
    face_confidence = db.Column(db.Integer, nullable = True)
    voice_confidence = db.Column(db.Integer, nullable = True)