import graphene
from app.typedefs.UserType import UserType
from app.model import UserModel

class UpdateUser(graphene.Mutation):
   class Arguments:
       userId = graphene.String(required=True)
       name = graphene.String()
       email = graphene.String()
       
   user = graphene.Field(lambda: UserType)   
   def mutate(self, info, **kwargs):
        user = UserModel.get(kwargs.get('userId'))
        name = kwargs.get('name')
        email = kwargs.get('email')
        if not name:
            name = user.name
        if not email:
            email = user.email
        user.update(
            actions=[
                UserModel.name.set(name),
                UserModel.email.set(email),
            ]
        )
        return UpdateUser(user=user)