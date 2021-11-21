import sqlite3  
from db import db

class UserModel(db.Model):  
    __tablename__ = 'users' 

    id = db.Column(db.Integer, primary_key = True) 
    username = db.Column(db.String(80)) 
    password = db.Column(db.String(80)) 

    def __init__(self, username, password) :  
        self.username = username 
        self.password = password  
    
    def save_to_db(self):
        db.session.add(self) 
        db.session.commit()
    
    @classmethod
    def find_by_username(cls, username) : 
        # connection = sqlite3.connect(r'D:\flask_tutorial\flask_project_using_sqlalchemy\data.db') 
        # cursor = connection.cursor() 

        # query = "select * from users where username=?" 
        # result = cursor.execute(query, (username,))  
        # row = result.fetchone() #this will provide the first row after the implementation of the query 
        # if row : 
        #     #user = cls(row[0],row[1],row[2])  #two way we can declare the values to the class method (def __init__)
        #     user = cls(*row)
        # else: 
        #     user = None 
        # connection.close() 
        # return user  
        return cls.query.filter_by(username = username).first() #in sqlalchemy just one line of this query will do the need for us the code is similar to select * from items where name=name limit 1;

    @classmethod 
    def find_by_id(cls,_id) : 
        # connection = sqlite3.connect(r'D:\flask_tutorial\flask_project_using_sqlalchemy\data.db') 
        # cursor = connection.cursor() 
        
        # query = 'select * from users where id=?' 
        # result = connection.execute(query,(_id,)) 
        # row = result.fetchone() 
        
        # if row: 
        #     ids = cls(*row)  
        # else: 
        #     ids = None 
        # connection.close() 
        # return ids   
        return cls.query.filter_by(id = _id).first()
