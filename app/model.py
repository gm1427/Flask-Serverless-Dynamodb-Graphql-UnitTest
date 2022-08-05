import os

from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model

class UserModel(Model):
    class Meta:
        table_name = 'users-table-dev'
        host = 'http://localhost:8000' 
        
    userId = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    email = UnicodeAttribute(null=False)