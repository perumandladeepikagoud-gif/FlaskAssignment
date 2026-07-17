from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas Connection
MONGO_URI = "YOUR_MONGODB_CONNECTION_STRING"

client = MongoClient(MONGO_URI)
db = client["studentdb"]
collection = db["students"]

@app.route('/api')
def get_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return render_template('success.html')

    except Exception as e:
        return render_template('form.html', error=str(e))
@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    itemName = request.form['itemName']
    itemDescription = request.form['itemDescription']

    collection.insert_one({
        "itemName": itemName,
        "itemDescription": itemDescription
    })

    return "To-Do Item Added Successfully"


if __name__ == '__main__':
    app.run(debug=True)