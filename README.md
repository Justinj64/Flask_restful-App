# Flask_Restful Application 
(Tested on : Python 3.8.6)

## - Problem Definition
To create a RESTful API with Python and Flask with Jwt for authentication.
Should cover basic Http request methods as given below;
- Get 
- Post
- Put 
- Delete

## - Implementation

- In the repo , execute the file "create_table.py".With help of Sqlite3 a  file data.db which will be used for storage of items.

- Change the secret key in app.py and execute the file as "python app.py".

- In Security.py , the credentials need to be changed accordingly for authentication.

- The Request flow and  endpoints are as follows:
    1) Register the user  
       >**POST - localhost:5000/register**  
       Json payload :   {"username":"","password":""}

	2) Authenticate the user  
        >**POST - localhost:5000/auth**  
        Json payload :  {"username":"","password":""}

	3) Use Token created in step 2 as Authorization header
        >**GET - localhost:5000/items**

	4) Create an item  
        >**POST - localhost:5000/item/itemName**  
        Json payload : {"price":15.00}

	5) Get a particular item
        >**GET - localhost:5000/item/itemName**

	6) Update or create an item if not exists
        >**PUT - localhost:5000/item/itemName**  
        Json payload : {"price":15.00}

	7) Delete an item
        >**DELETE - localhost:5000/item/itemName**




