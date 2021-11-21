#import sqlite3 
from db import db


class StoreModel(db.Model) :  
    __tablename__ = 'stores' 

    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(80))  
    items = db.relationship('ItemModel',lazy = 'dynamic') #communicating between primary key and foreign key
    #price = db.Column(db.Float(precision = 2)) 
    def __init__(self,name) :
        self.name = name 
        
    
    def json(self): 
        return {'name' : self.name,'items' : [item.json() for item in self.items.all()]} 
    
    @classmethod 
    def find_by_name(cls, name):
        # connection = sqlite3.connect(r'D:\flask_tutorial\flask_project_using_sqlalchemy\data.db') 
        # cursor = connection.cursor() 
        # query = "select * from items where name=?" 
        # result =  cursor.execute(query,(name,)) 
        # row = result.fetchone() 
        # connection.close() 
        # if row : 
        #     return cls(*row) 
        return cls.query.filter_by(name=name).first() #in sqlalchemy just one line of this query will do the need for us the code is similar to select * from items where name=name limit 1;

    def save_to_db(self):
    #def insert(self):  
        # connection = sqlite3.connect(r'D:\flask_tutorial\flask_project_using_sqlalchemy\data.db') 
        # cursor = connection.cursor() 
        # query = "insert into items values (?,?)" 
        # cursor.execute(query,(self.name,self.price)) 
        # connection.commit() 
        # connection.close()  
        db.session.add(self)  #this line will do the function of the above code
        db.session.commit()
    def delete_from_db(self):
    # def update(self):
    #     connection = sqlite3.connect(r'D:\flask_tutorial\flask_project_using_sqlalchemy\data.db') 
    #     cursor = connection.cursor() 
    #     query = "update items set price=? where name=?" 
    #     cursor.execute(query,(self.price,self.name)) 
    #     connection.commit() 
    #     connection.close()
        db.session.delete(self) #this line will do the function of the above code
        db.session.commit() 
