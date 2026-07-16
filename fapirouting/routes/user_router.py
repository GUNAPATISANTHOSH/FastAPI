from fastapi import APIRouter
router=APIRouter(prefix='/user',default="user module APIs")

'''
usage=GET user details
URL=http://127.0.0.1:8000/products/read
Method Type:GET
Required feilds= None
Access type:Public
'''
@router.get("/")
def get_user():
    return "Getting user Details"

'''
usage=create user details
URL=http://127.0.0.1:8000/products/read
Method Type:POST
Required feilds= None
Access type:Public
'''
@router.post("/")
def create_user():
    return "Created user Details"

'''
usage=update user details
URL=http://127.0.0.1:8000/products/read
Method Type:PUT
Required feilds= None
Access type:Public
'''
@router.put("/")
def Update_user():
    return "updated user Details"

'''
usage=delete user details
URL=http://127.0.0.1:8000/products/read
Method Type:DELETE
Required feilds= None
Access type:Public
'''
@router.delete("/")
def delete_user():
    return "deleted user Details"