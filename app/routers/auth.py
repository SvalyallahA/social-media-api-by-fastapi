from fastapi import APIRouter,Depends,status,HTTPException,Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models,utils,oauth2
router=APIRouter(tags=['Authentication'])


@router.post('/login', response_model=schemas.Token)
#def login(user_credntials:schemas.UserLogin, db: Session=Depends(database.get_db)):
def login(user_credntials:OAuth2PasswordRequestForm = Depends(), db: Session=Depends(database.get_db)):
     #OAuth2PasswordRequestForm returns username and password
    user=db.query(models.User).filter(models.User.email==user_credntials.username).first()
   
    
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    if not utils.verify(user_credntials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")
    
    #create token
    #return token
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    #return {"token": "example token"}
    return{"access_token":access_token, "token_type":"bearer"}



