from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from database import models
from database.database import engine
from routers import post

app = FastAPI()
app.include_router(post.router)

# @app.get('/')
# def hello_world():
#     return 'Hello world!'

models.Base.metadata.create_all(engine)

# app.mount('/images', StaticFiles(directory='images'), name='images')

# VITE runs on port 5173, normally 3000
# origins = ['http://localhost:5173']
origins = ['*']

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=['*'],
    allow_headers=['*']
)