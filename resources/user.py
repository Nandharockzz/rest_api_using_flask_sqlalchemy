import sqlite3
from sqlite3.dbapi2 import Cursor, connect 
from flask_restful import Resource,reqparse  
from models.user import UserModel

class UserRegister(Resource) :  
    parser = reqparse.RequestParser() 
    parser.add_argument('username', type = str, required = True, help = "This field cannot be left blank")  
    parser.add_argument('password', type = str, required = True, help = "This field cannot be left blank")
    def post(self) : 

        data = UserRegister.parser.parse_args()
        
        connection = sqlite3.connect(r'D:\flask_tutorial\flask_project_using_sqlalchemy\data.db') 
        cursor = connection.cursor() 
        # sub_query = "select * from users where username=? and password=?" 
        # result = cursor.execute(sub_query,(data['username'],data['password'])) 
        # row = result.fetchone()
        # if row :
        #     return {'message' : 'user already there in our database'}  #below line also doing the same thing 
        if UserModel.find_by_username(data['username']) :
            return {'message' : 'user already there in our database'}, 400

        # query = 'insert into users values (NULL,?,?)'  #since id is auto-incremented in create_tables.py file we have to mentioned it as null
        # cursor.execute(query, (data['username'],data['password'])) 

        # connection.commit() 
        # connection.close()   
        #user = UserModel(data['username'],data['price'])  
        user = UserModel(**data)
        user.save_to_db() 
        return {'message' : "User  created successfully ."},201




        


        