import graphene
from app.mutations.create_user import CreateUser
from app.mutations.update_user import UpdateUser
from app.mutations.delete_user import DeleteUser


class UserMutations (graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()