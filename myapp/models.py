from myapp import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    screenName = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(72)) # くっ
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    def toDict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
 