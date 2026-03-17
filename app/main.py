from fastapi import FastAPI
from app.api.tasks import router
 
app = FastAPI(
    title='My Task API',
    description='My very first Python API!',
)
 
app.include_router(router)
 
@app.get('/')
async def home():
    return {'message': 'Welcome to My Task API!'}
