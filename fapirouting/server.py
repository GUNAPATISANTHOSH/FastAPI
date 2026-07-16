from fastapi import FastAPI
from routes.user_router import router as user_router
from routes.product_router import router as product_router
app = FastAPI()

'''
usage=Application root request
URL=http://127.0.0.1:8000/
Method Type:GET
Required feilds= None
Access type:Public
'''
@app.get("/")
def root_request():
    return "Application Root Created successfully"
app.include_router(user_router)
app.include_router(product_router)