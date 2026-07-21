from fastapi import FastAPI
from routes.product_router import router as product_router
app=FastAPI()

'''
usage: Application Root request
RestAPI URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None 
Access Type:Public
'''
@app.get("/")
def root_request():
    return {'msg':'Application Root Request'}

app.include_router(product_router)