def create_user():
    return """
    mutation userMutations($email: String!, $name: String!, $userId: String!){
        createUser(email:$email, name:$name, userId:$userId){
            user{
            name
            email
            userId
            }
        }
    }
   """
   
    
def update_user():
    return """
        mutation userMutations{
            updateUser(name:"testUpdate", userId:"2"){
                user{
                    name
                    email
                    userId
                }
            }
        }
    """


def delete_user():
    return """
         mutation userMutations($userId: String!){
            deleteUser(userId:$userId){
                success
            }
        }
    """