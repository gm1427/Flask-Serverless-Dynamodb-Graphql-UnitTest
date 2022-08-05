import graphene
from graphene_pynamodb import PynamoObjectType
from app.model import UserModel

class UserType(PynamoObjectType):

    class Meta:
        model = UserModel
        interfaces = (graphene.Node,)
