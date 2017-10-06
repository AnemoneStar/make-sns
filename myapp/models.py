from myapp import db

class MyModel:
    def toDictHook(self, d):
        return d
    def toDict(self):
        d = {}
        for c in self.__table__.columns:
            name = c.name
            if name[-2:] == "Id":
                name = name[:-2]
            d[name] = getattr(self, name)
            d[name] = getattr(d[name], "toDict", lambda :d[name])()
        return self.toDictHook(d)

class User(db.Model, MyModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    screenName = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)
    posts = db.relationship('Post', backref='user')
    def toDictHook(self, d):
        del d["password"]
        return d


class Post(db.Model, MyModel):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(72)) # くっ
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
 