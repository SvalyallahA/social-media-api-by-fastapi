#SQLALCHEMY
#################
# session is responsible for talking to the databases.
# this function blow connect us to the database or get a session to the database 
# every time we get a request  we are gonna get a session we are gonna in to build send sql statements to it and after the request done we close it out 
#def get_db():
    #db = SessionLocal()
   # try:
   #     yield db
   # finally:
   #     db.close()
######################

    #rating:Optional[int]=None

#connect db to python code
#while True:

   # try: 
     #   conn=psycopg2.connect(host='localhost',database='fastapiDB',user='postgres',password='tt2191aa', cursor_factory=RealDictCursor)
      #  cursor=conn.cursor()
      #  print("Database connection was successfull!")
      ##  break
   # except Exception as error:
   #     print("connecting to the database failed")
   #     print("Error: ",error)
    #    time.sleep(2)





#my_posts=[{"title":"title of post 1", "content":"content of post 1", "id":1},{"title":"favorite foods", "content":"I like pizza", "id":2} ]

#def find_post(id):
    #for p in my_posts:
   #     if p["id"]==id:
    #        return p

#def find_index_post(id):
 #   for i,p in enumerate(my_posts):
  #      if p['id']==id:
   #         return i




#@app.get("/")
#async def root():
  #  d=[]
   # for i in range(10):
   #     d.append(i**2)
   # return {"message":d}

#@app.get("/sqlalchemy")
#def test_posts(db: Session=Depends(get_db)):

  #  post=db.query(models.Post).all()

  #  return {"data":post}

