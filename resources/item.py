#import sqlite3
from flask import Flask,request,jsonify
from flask.wrappers import Request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required #jwt_required is more important as once authentication is correct using JWT jwt_required decorator checks whether user is logged in 
from security import authentication, identity  
from models.item import ItemModel
#from user import User,UserRegister
class Item(Resource): 
    parser = reqparse.RequestParser() # this is used instead of request.get_json() because sometimes we need only a specific value to be updated but the json may contain other information as well so in order to extract specific value from the json we use parser
    parser.add_argument('price', type = float, required = True, help = "This field cannot be left blank")  #we declare this and above line in the class itself since it does not require self. calling statement
    parser.add_argument('store_id', type = int, required = True, help = "Every item needs a store id.")
    @jwt_required() #user authentication key will be generate at /auth we have to paste in postman application of /item/<name>(refer the postman) this decorator can be used in get,post,put,delete methods also
    def get(self, name): 
        # item = next(filter(lambda x:x['name']==name,items),None) #next will return the first item present with the name suppose we didn't find the item then it will return None
        # return {"item" : item} , 200 if item else 404  #404 is the value used if nothing is found 
        # connection = sqlite3.connect(r'D:\flask_tutorial\flask_project_using_sql\data.db')  #using sql
        # cursor = connection.cursor() 
        # query = "select * from items where name=?" 
        # result =  cursor.execute(query,(name,)) 
        # row = result.fetchone() 
        # connection.close() 
        item = ItemModel.find_by_name(name)  

        if item: 
            return item.json()
       
        return {'message' : 'item not found'},404
    


    def post(self, name) : 
        if ItemModel.find_by_name(name) : 
            return {'message':"An item with name '{}' already exists".format(name)}, 400
        # if next(filter(lambda x:x['name']==name,items),None) is not None:
        #     return {'message':"An item with name '{}' already exists".format(name)}, 400 #400 means bad request 
        #data = request.get_json() #gets the into from the json file alternate to this is  
        data = Item.parser.parse_args()
        #item = ItemModel(name,data["price"],data['store_id'])  
        item = ItemModel(name,**data)
        try:
            item.save_to_db()
        except : 
            return {'message' : 'An error occured while inserting the item.'}, 500
        return item.json(), 201
        # items.append(item) 
        # return item,201 #201 is used to denote when something is created 


    def delete(self, name) :  
        # connection = sqlite3.connect(r'D:\flask_tutorial\flask_project_using_sqlalchemy\data.db') 
        # cursor = connection.cursor() 
        # query = "delete from items where name=?" 
        # cursor.execute(query,(name,)) 
        # connection.commit() 
        # connection.close()  
        # global items 
        # items = list(filter(lambda x:x['name']!=name,items))  
        item = ItemModel.find_by_name(name) 
        if item:
            item.delete_from_db()
        return {'message' : "item deleted successfullly"} 

    def put(self, name): 
        #here parser is decleared again just to know we can declare parser inside the instance method also 
        #parser = Item.reqparse.RequestParser() # this is used instead of request.get_json() because sometimes we need only a specific value to be updated but the json may contain other information as well so in order to extract specific value from the json we use parser
        #parser.add_argument('price', type = float, required = True, help = "This field cannot be left blank")
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name) 
        # updated_item = ItemModel(name, data['price']) 
        if item is None: 
            # try : 
            #     updated_item.insert()
            # except : 
            #     return {'message' : 'An error occured inserting the item'},500 
            # item = ItemModel(name,data['price'],data['store_id']) 
            item = ItemModel(name,**data)
        else: 
        #     try :
        #         updated_item.update()
        #     except : 
        #         return {'message' : 'An error occured while updating the item'},500 
        # #return {'messsage':"nothings printed wasted"} 
            item.price = data['price']  
            item.store_id = data['store_id']
        item.save_to_db()
        return item.json()
 
        


class ItemList(Resource) :  
    def get(self): 
        # connection = sqlite3.connect(r'D:\flask_tutorial\flask_project_using_sqlalchemy\data.db') 
        # cursor = connection.cursor() 
        # query = 'select *  from items'
        # result = cursor.execute(query) 
        # items = []
        # for row in result :
        #     #items.append({'name' : row[0],'price' : row[1]}) 
        #     items.append({'name' : row[1],'price' : row[2]})
        # if items: 
        #     return {"total_items" : items}
        # else: 
        #     return {'message' : 'No items present here'} 
        #return {"items":items} 
        return {'total_items' : [item.json() for item in ItemModel.query.all()]}  #or return {'total_items' : list(map(lambda x: x.json(), ItemModel.query.all()))} 