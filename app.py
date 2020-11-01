from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authentication,identity
from user import UserRegister
from item import Item,ItemList

# Initialize the Flask App
app = Flask(__name__)
app.secret_key = "" ## add a secret key
api = Api(app)

jwt = JWT(app,authentication,identity) # /auth

# Add resource endpoints
api.add_resource(Item,"/item/<string:name>")
api.add_resource(ItemList,"/items")
api.add_resource(UserRegister,"/register")

# Run the api on port 5000
if __name__ == "__main__":
    app.run(debug=True,port=5000)