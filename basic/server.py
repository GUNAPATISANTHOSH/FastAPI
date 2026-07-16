from fastapi import FastAPI
app=FastAPI()

'''
usage=GET product details
URL=http://127.0.0.1:8000/products/read
Method Type:GET
Required feilds= None
Access type:Public
'''
@app.get("/products/read")
def get_products():
    return{"msg":"Getting products successfully"}

'''
usage=product details
URL=http://127.0.0.1:8000/products/update
Method Type:PUT
Required feilds= None
Access type:Public
'''

@app.put("/products/update")
def update_products():
    return{"msg":"product updated"}