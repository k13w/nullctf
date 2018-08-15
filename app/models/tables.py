from app import db
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin, SQLAlchemyBackend
from flask_login import current_user
from app import blueprint

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String, unique=True)
    score = db.Column(db.Integer, default=0)
    solved = db.Column(db.String(400))
    lastSubmit = db.Column(db.DateTime)

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

    def __init__(self, username, email, solved):
        self.username = username
        self.email = email
        self.solved = solved

    def __repr__(self):
        return '<User %r>' % self.username

    def get_chal(self):
        return list(map(int, self.solved.split(',')[:-1]))

class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)

blueprint.backend = SQLAlchemyBackend(OAuth, db.session, user=current_user, user_required=False)

class Challenges(db.Model):
    __tablename__ = 'challenges'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    category = db.Column(db.String(80))
    content = db.Column(db.Text)
    flag = db.Column(db.String(40))
    value = db.Column(db.String(20))

    def __init__(self, name, category, content, flag, value):
        self.name = name
        self.category = category
        self.content = content
        self.flag = flag
        self.value = value

    def __repr__(self):
        return '<Challenges %r>' % self.name
