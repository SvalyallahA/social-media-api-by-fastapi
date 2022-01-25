


#from pyexpat import model
#import secrets

#from turtle import pos, title
#from types import new_class
#from typing import Optional, List #to return list of post for sqlalchemy 
#from fastapi import Body, Depends, FastAPI, Response,status, HTTPException
from fastapi import FastAPI
#from markupsafe import re
#from random import randrange
#import psycopg2
#from psycopg2.extras import RealDictCursor
#import time
#from sqlalchemy.orm import Session
#from . import models,schemas, utils
from app.database import engine, get_db
##########################################
from app.routers import post, postgres,user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


#print(settings.secret_key)


#models.Base.metadata.create_all(bind=engine) #SQLALCHEMY / we dont need it because we are using alembic now 

app = FastAPI()

origins=["*"]#[*] allows every domain
app.add_middleware(
    CORSMiddleware, # its a function that runs before any request
    allow_origins=origins, # what domain should be able to talk to our api 
    allow_credentials=True,
    allow_methods=["*"],#allow some specific http methods
    allow_headers=["*"],#allow specific headers
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(postgres.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    
    return {"message":"HELLO WORLD"}