import sqlite3

connection = sqlite3.connect('data.db')
#First we make a connection with the database, don't worry if you don't have one
#It will automatically create for you

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"   

cursor.execute(create_table)

connection.commit()

connection.close()