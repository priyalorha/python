from flask_login import UserMixin
from flask_mongoengine import MongoEngine
import datetime

mongo_db = MongoEngine()
mongo_db.connect("test")

class User(UserMixin, mongo_db.DynamicDocument):
    meta = {'collection': 'admin_user'
        , 'indexes': ['email', 'password']}
    first_name = mongo_db.StringField(max_length=40)
    last_name = mongo_db.StringField(max_length=40)
    email = mongo_db.StringField(max_length=40, unique=True)
    password = mongo_db.StringField()
    can_create = mongo_db.BooleanField(default=False)
    can_edit = mongo_db.BooleanField(default=False)
    can_delete = mongo_db.BooleanField(default=False)
    can_export = mongo_db.BooleanField(default=False)
    can_import = mongo_db.BooleanField(default=False)
    is_admin = mongo_db.BooleanField()
    is_view1 = mongo_db.BooleanField()
    is_view2 = mongo_db.BooleanField()
    is_view3 = mongo_db.BooleanField()
    insert_date = mongo_db.DateTimeField(default=datetime.datetime.utcnow)
    def __unicode__(self ,):
        return self.email
User=User()
User.first_name='Priya'
User.last_name="Lorha"
User.email="priyalorha@gmail.com"
User.password="abcd123"
User.is_admin=True
User.can_create=True
User.can_edit=True
User.can_delete=True
User.can_export=True
User.can_import =True
User.save()