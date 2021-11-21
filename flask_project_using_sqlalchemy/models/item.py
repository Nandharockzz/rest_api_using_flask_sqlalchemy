#import sqlite3 
from db import db


class ItemModel(db.Model) :  
    __tablename__ = 'items' 

    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(80)) 
    price = db.Column(db.Float(precision = 2)) 
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id')) #creates a foreign key in the stores table denoting the ids
    store = db.relationship('StoreModel') #this line acts as join to the items table
    def __init__(self,name, price, store_id) :
        self.name = name 
        self.price = price 
        self.store_id = store_id
    
    def json(self): 
        return {'name' : self.name,'price' : self.price} 
    
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
