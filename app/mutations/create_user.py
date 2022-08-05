import graphene
from app.typedefs.UserType import UserType
from app.model import UserModel

class CreateUser(graphene.Mutation):
   class Arguments:
       userId = graphene.String(required=True)
       name = graphene.String(required=True)
       email = graphene.String(required=True)
   user = graphene.Field(lambda: UserType)   
   def mutate(self, info, userId, name, email):
       user = UserModel(userId=userId, name=name, email=email)
       user.save()
       
       return CreateUser(user=user)