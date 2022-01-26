from flask_mongoengine import MongoEngine
db = MongoEngine()


class Comments(db.EmbeddedDocument):
    comment_id = db.IntField(primary_key=True,required=True)
    name = db.StringField(max_length=120)
    email = db.StringField(max_length=255)
    body = db.StringField()
    meta = {
        'strict': False,
        "skip_base_validate": True
    }

class Posts(db.EmbeddedDocument):
    post_id = db.IntField(primary_key=True,required=True)
    title = db.StringField(max_length=255)
    body = db.StringField()
    comments = db.ListField(db.EmbeddedDocumentField(Comments))
    meta = {
        'strict': False,
        "skip_base_validate": True
    }
