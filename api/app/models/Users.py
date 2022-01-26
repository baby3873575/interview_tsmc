from flask_mongoengine import MongoEngine
from .base import BaseDocument
from .Posts import Posts
from .Todos import Todos
db = MongoEngine()


class Users(BaseDocument):
    user_id = db.IntField(primary_key=True,required=True)
    name = db.StringField(max_length=255)
    username = db.StringField(max_length=255)
    email = db.StringField(max_length=255)
    address = db.DictField()
    phone = db.StringField(max_length=255)
    website = db.StringField(max_length=255)
    company = db.DictField()
    posts = db.ListField(db.EmbeddedDocumentField(Posts))
    todos = db.ListField(db.EmbeddedDocumentField(Todos))
    meta = {
        'strict': False,
        "skip_base_validate": True
    }
