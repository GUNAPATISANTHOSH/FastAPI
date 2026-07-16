from fastapi import APIRouter
router=APIRouter(prefix="/products")
'''
usage=GET product details
URL=http://127.0.0.1:8000/products/
Method Type:GET
Required feilds= None
Access type:Public
'''
@router.get("/")
def get_products():
    return "Fetching Products Details Successfully "
'''
usage=Create product details
URL=http://127.0.0.1:8000/products/
Method Type:POST
Required feilds= None
Access type:Public
'''
@router.post("/")
def create_products():
    return "Created Products Details Successfully "
'''
usage=Update product details
URL=http://127.0.0.1:8000/products/read
Method Type:PUT
Required feilds= None
Access type:Public
'''
@router.put("/")
def update_products():
    return "Updated Products Details Successfully "
'''
usage=Delete product details
URL=http://127.0.0.1:8000/products/read
Method Type:DELETE
Required feilds= None
Access type:Public
'''
@router.delete("/")
def delete_products():
    return "Deleted Products Details Successfully "