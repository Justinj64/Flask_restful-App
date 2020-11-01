# Using Sqlite3 it is possible to create a lightweight disk-based database,
# that doesn’t require a separate server process. 
import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

# Query to create users table if not present
create_table = "Create Table if not exists users (id INTEGER PRIMARY KEY,username text ,password text)"

cursor.execute(create_table)

# Query to create items table if not present
create_table = "Create Table if not exists items (name text,price real)"

cursor.execute(create_table)

# Commit the changes
connection.commit()

# Close the connection
connection.close()