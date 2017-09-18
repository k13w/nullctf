from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(50))
    email = db.Column(db.String, unique=True)
    score = db.Column(db.String(20))
    solved = db.Column(db.String(400))

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, email, score, solved):
        self.username = username
        self.password = password
        self.email = email
        self.score = score
        self.solved = solved

    def __repr__(self):
        return '<User %r>' % self.username

class Challenges(db.Model):
    __tablename__ = 'challenges'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    category = db.Column(db.String(80))
    content = db.Column(db.String(800))
    flag = db.Column(db.String(40))
    score = db.Column(db.String(20))

    def __repr__(self):
        return '<Challenges %r>' % self.name
