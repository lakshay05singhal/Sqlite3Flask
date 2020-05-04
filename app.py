from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def insert():
    if request.method=='POST':
        name = request.form.get('name')
        price = request.form.get('price')
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (name, price))
        connection.commit()
        connection.close()

    return render_template('insert.html')

@app.route('/items')
def items():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "SELECT * FROM items"
    result = cursor.execute(query)
    items = []
    for row in result:
        items.append({'name': row[0], 'price': row[1]})
        
    return {"items": items}

if __name__ == '__main__':
    app.run(debug=True)