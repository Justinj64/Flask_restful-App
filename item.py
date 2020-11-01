import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required

# Item class that contains routing methods and processing data
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",type=float,required=True,help="this field cannot be left blank")
    
    @jwt_required()
    def get(self,name):
        item = self.find_by_name(name)
        if item:
            return item
        return {"message":"Item not found"},404
    
    @classmethod
    def find_by_name(cls,name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "Select * from items where name = ?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()
        if row:
            return {"item":{"name":row[0],"price":row[1]}}  

    def post(self,name):
        if self.find_by_name(name):
            return {"message":f"Item with name {name} alrady exists"},400 # something wrong with request
        data = Item.parser.parse_args()
        item = {"name":name,
                "price":data["price"]}
        try:
            self.insert(item)        
        except:
            return {"message":"An errorhas occured during insert"},500 # internal server error

        return item,201      

    @classmethod
    def insert(cls,item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "Insert into items values(?,?)"
        cursor.execute(query,(item["name"],item["price"]))
        connection.commit()
        connection.close()

    def delete(self,name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "Delete from items where name = ?"
        cursor.execute(query,(name,))
        connection.commit()
        connection.close()
        return {"message":"item deleted"}
    
    @classmethod
    def update(cls,item):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "Update items set price = ? where name = ?"
        cursor.execute(query,(item["price"],item["name"]))
        connection.commit()
        connection.close()
    
    def put(self,name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        updated_item = {"name":name,"price":data["price"]}

        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {"message":"An errorhas occured during insert"},500 # internal server error
        else:
            try:
                self.update(updated_item)
            except:
                return {"message":"An errorhas occured during update"},500 # internal server error    
        return updated_item        

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "Select * from items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({"name":row[0],"price":row[1]})
        connection.close()
        return {"items":items}