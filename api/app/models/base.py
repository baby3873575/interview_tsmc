from datetime import date, datetime
from flask import g
from flask_mongoengine import MongoEngine, ValidationError

# from bson import json_util
import json

db = MongoEngine()

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))


class BaseDocument(db.Document):
    create_time = db.DateTimeField(default=datetime.utcnow)
    modify_time = db.DateTimeField(default=datetime.utcnow)
    meta = {
        'allow_inheritance': True,
        'abstract': True,
        'strict': False
    }

    def __str__(self):
        return str(self.pk)

    def save(self):
        current_datetime = datetime.utcnow()
        self.modify_time = current_datetime
        return super().save()

    def update(self, **kwargs):
        current_datetime = datetime.utcnow()
        kwargs['upsert'] = False  # upsert is set to false to make create_time and modify_time flag work properly
        kwargs['modify_time'] = current_datetime
        return super().update(**kwargs)

    def to_json(self, *args, **kwargs):
        """Convert this document to JSON.

        :param use_db_field: Serialize field names as they appear in
            MongoDB (as opposed to attribute names on this document).
            Defaults to True.
        """
        use_db_field = kwargs.pop('use_db_field', True)
        return json.dumps(self.to_mongo(),default=json_serial, *args, **kwargs)

    def validate(self, *args, **kargs):
        super(BaseDocument, self).validate(*args, **kargs)




class BaseDynamicDocument(db.DynamicDocument):
    create_time = db.DateTimeField(default=datetime.utcnow)
    modify_time = db.DateTimeField(default=datetime.utcnow)
    meta = {
        'allow_inheritance': True,
        'abstract': True,
        'strict': False
    }

    def __str__(self):
        return str(self.pk)

    def save(self):
        current_datetime = datetime.utcnow()
        self.modify_time = current_datetime
        return super().save()

    def update(self, **kwargs):
        current_datetime = datetime.utcnow()
        kwargs['upsert'] = False  # upsert is set to false to make create_time and modify_time flag work properly
        kwargs['modify_time'] = current_datetime
        return super().update(**kwargs)

    def to_json(self, *args, **kwargs):
        """Convert this document to JSON.

        :param use_db_field: Serialize field names as they appear in
            MongoDB (as opposed to attribute names on this document).
            Defaults to True.
        """
        use_db_field = kwargs.pop('use_db_field', True)
        return json.dumps(self.to_mongo(),default=json_serial, *args, **kwargs)

    def validate(self, *args, **kargs):
        super().validate(*args, **kargs)

