#in postman application requests are present in flask_rest_api folder
import os,re
from flask import Flask,request
from flask.wrappers import Request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT,jwt_required #jwt_required is more important as once authentication is correct using JWT jwt_required decorator checks whether user is logged in 
from security import authentication, identity 
from resources.user import UserRegister
from resources.item import Item,ItemList 
from resources.store import Store,StoreList
from db import db

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI','sqlite:///data.db') #database_url is used in delopyment in heroku. for local dev we can use sqlite itself
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #if db object is changed it looks into it by default sqlalchemy as better modification tracker builin  
app.secret_key = "nandha@30" #its an authentication
api = Api(app) 
jwt = JWT(app, authentication, identity) #http://127.0.0.1:5000/auth #it is important as it checks correct user is logging in with correct password

@app.before_first_request 
def create_tables() : 
    db.create_all() #this function creates the database for us and create along the tables required for us.

api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/item/nandha  
api.add_resource(ItemList, '/items') 
api.add_resource(UserRegister, '/register') 
api.add_resource(Store, '/store/<string:name>')  
api.add_resource(StoreList, '/stores') 
db.init_app(app)
if __name__ == '__main__':
    
    app.run(port=5000) 
