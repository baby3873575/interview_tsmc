from flask_mongoengine import MongoEngine
db = MongoEngine()


class Todos(db.EmbeddedDocument):
    todo_id = db.IntField(primary_key=True,required=True)
    title = db.StringField(max_length=120)
    completed = db.BooleanField(max_length=255)
    meta = {
        'strict': False,
        "skip_base_validate": True
    }
