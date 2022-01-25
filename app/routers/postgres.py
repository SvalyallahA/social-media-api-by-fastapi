
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# from .. import models,schemas, utils
# from fastapi import Body, Depends, FastAPI, Response,status, HTTPException, APIRouter

# router=APIRouter(prefix="/posts", tags=['POSTS-PYDANTIC'])
# # while True:

#     try: 
#         conn=psycopg2.connect(host='localhost',database='fastapiDB',user='postgres',password='tt2191aa', cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("Database connection was successfull!")
#         break
#     except Exception as error:
#         print("connecting to the database failed")
#         print("Error: ",error)
#         time.sleep(2)

# my_posts=[{"title":"title of post 1", "content":"content of post 1", "id":1},{"title":"favorite foods", "content":"I like pizza", "id":2} ]

# @router.get("/")
# def get_post():
#     #access to the post table and fetch data 
#     cursor.execute("""SELECT * FROM post """)
#     posts=cursor.fetchall()
#     print(posts)
#     return{"data":posts}

# #@app.post("/posts", status_code=status.HTTP_201_CREATED)
# #def create_posts(new_post:Post):
#   # print(new_post)
#   #  print(new_post.dict())
#   ######################################
#     #post_dict=new_post.dict()
#    # post_dict['id']=randrange(0,100000)
#    # my_posts.append(post_dict)
#     #return {"data":post_dict}
# #######################################

# @router.post("/", status_code=status.HTTP_201_CREATED)
# def create_posts(post: schemas.Postgres):

#     cursor.execute(""" INSERT INTO post (title, content, published) VALUES (%s,%s,%s) RETURNING * """, (post.title,
#     post.content, post.published))
#     new_post=cursor.fetchone()
#     conn.commit() #To save into the database

#     return {"data":new_post}



# #title str, content str

# @router.get("/latest")
# def get_latest_post():
#     post=my_posts[-1]
#     return post

# @router.get("/{id}")
# def get_post(id: int, response: Response):
#    # print(type(id))
#     #post= find_post(int(id))
#     ####################################################################
#     cursor.execute(""" SELECT*FROM post WHERE id=%s """,(str(id),))
#     post=cursor.fetchone()
#     ####################################################################
#     ####################################
#     #print(test_post)
#     #post= find_post(id)
#     ####################################
#     if not post:
#         #response.status_code=404
        
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found" )
#         #response.status_code=status.HTTP_404_NOT_FOUND
#         #return {"message": f"post with id {id} not found"}
#     #return{"post detail": f"here is post {id}"}
#     return{"post detail": post}









# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id):
#     # deleting a post
#     #find the index in the array 
#     #my_posts.pop(index)
#     cursor.execute(""" DELETE FROM post WHERE id = %s RETURNING* """,(str(id),))
#     deleted_post=cursor.fetchone()
#     conn.commit()
#     ############################################
#     #index=find_index_post(int(id))
#     #if index==None:
#     ###############################################
#     if deleted_post==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} doesn't exist")
#     ################################
#     #my_posts.pop(index)
#     ################################

#     return Response(status_code=status.HTTP_204_NO_CONTENT)



# @router.put("/{id}", response_model=schemas.PostBase)
# def update_post(id:int , post:schemas.PostBase):
#     cursor.execute("""UPDATE post SET title=%s, content=%s, published=%s WHERE id=%s RETURNING *""", (post.title, post.content, 
#     post.published, str(id)))
#     updated_post=cursor.fetchone()
#     conn.commit()
#     ##################################
#     #index=find_index_post(int(id))
#     #if index==None:
#     #################################
#     if updated_post==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} doesn't exist")
#     ###################################################
#     #post_dict=post.dict()
#     #post_dict["id"]=id
#     #my_posts[index]=post_dict
#     #print(post)
#     #return {'data':post_dict}
#     #######################################################
#     return updated_post


