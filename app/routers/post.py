#from asyncio import tasks
#from posixpath import ismount
#from unittest import result

#from click import get_current_context
from sqlalchemy import func

from app import oauth2
from .. import models, schemas, oauth2
from fastapi import Body, Depends, FastAPI, Response,status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.database import  get_db
from typing import  List,Optional

router= APIRouter(prefix="/sqlalchemy/posts", tags=['POST-SQLALCHEMY'])

#@router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])
def get_post(db: Session=Depends(get_db), user_id: int=Depends(oauth2.get_current_user),limit:int=10, skip:int=0,search:Optional[str]=""):

    print(search)
    #posts = db.query(models.Post).all() # returns all posts (like social media)
    #limit
    
    #posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    posts=db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id==models.Post.id, isouter=True).group_by(models.Post.id
        ).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()# sqlalchemy by ddefault its gonna be a LEFT JOIN
    #print(results)
    #############################################################
    ### FOR MAKING OUR APP PRIVATE ADD THIS SECTION TO OUR CODE 
    #posts = db.query(models.Post).filter(models.Post.owner_id==user_id.id).all() #only returns the post that created by that id 
    #############################################################################################################################
    #print(user_id.id)
    return  posts


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.Post)
def created_posts(post:schemas.PostBase, db: Session=Depends(get_db), user_id: int=Depends(oauth2.get_current_users)):

    #print(post.dict())
    
    #new_post= models.Post(title=post.title, content=post.content, published= post.published)
    #print(user_id.id)
    #print(user_id.email)
   
    new_post=models.Post(owner_id=user_id.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

@router.get("/{id}", response_model=schemas.PostOut)
def get_post(id: int, db: Session=Depends(get_db), user_id: int=Depends(oauth2.get_current_users)):
    
    #post= db.query(models.Post).filter(models.Post.id == id).first()
    post=db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id==models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    
    if not post:
        #response.status_code=404
        
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found" )
        #response.status_code=status.HTTP_404_NOT_FOUND
        #return {"message": f"post with id {id} not found"}
    #return{"post detail": f"here is post {id}"}
    #############################################################
    ### FOR MAKING OUR APP PRIVATE ADD THIS SECTION TO OUR CODE 
    #if post.owner_id!=user_id.id:
    #    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"NOT Authorized to perform requested action")
    ##############################################################
    return post

@router.delete("/{id}")
def delete_post(id: int, db: Session=Depends(get_db), user_id: int=Depends(oauth2.get_current_users)):
    
    post_quary = db.query(models.Post).filter(models.Post.id==id)
    post=post_quary.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} doesn't exist")
    
    if post.owner_id!=user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"NOT Authorized to perform requested action")
    post_quary.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}")
def update_post (id:int, updated_post:schemas.PostBase ,db: Session=Depends(get_db), user_id: int=Depends(oauth2.get_current_users)):
   post_query=  db.query(models.Post).filter(models.Post.id==id)
   post=post_query.first()
   if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} doesn't exist")
   if post.owner_id!=user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"NOT Authorized to perform requested action")
   post_query.update(updated_post.dict(), synchronize_session=False)
   #post_query.update({'title':'hey this is updated title sqlalchmy', 'content':'this is the updated content sqlalchemy'}, synchronize_session=False)
   db.commit()
   return post_query.first()
############################################################################

