import graphene
from app.typedefs.UserType import UserType
from app.model import UserModel

class DeleteUser(graphene.Mutation):
   success = graphene.Boolean()
   class Arguments:
       userId = graphene.String(required=True)
       
   user = graphene.Field(lambda: UserType)   
   status = graphene.String()
   def mutate(self, info, userId):
        user = UserModel.get(userId)
        user.delete()
        return DeleteUser(success=True)