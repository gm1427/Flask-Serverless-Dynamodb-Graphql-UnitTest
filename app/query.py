import graphene
from app.model import  UserModel
from app.typedefs.UserType import UserType

from flask import jsonify

class UserQuery(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="friend"))
    getUser = graphene.Field(UserType, userId=graphene.String(required=True))
    getAllUsers = graphene.List(UserType)
    user = graphene.Field(UserType)
    
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    
    def resolve_getUser(parent, info, userId):
        return UserModel.get(userId)
    
    def resolve_getAllUsers(self, args):
        return list(UserModel.scan())