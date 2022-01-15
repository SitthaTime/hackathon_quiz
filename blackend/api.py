from flask import Flask, jsonify, request
from flask_cors import CORS
import connectdb

app = Flask(__name__)
CORS(app)

@app.route('/name',methods = ['GET'])
def name():
    data = connectdb.selectName()
    return jsonify(data)

@app.route('/date',methods = ['POST'])
def date():
    request_data = request.get_json()
    code = request_data['code']
    date = request_data['date']
    data = connectdb.selectTime(code, date)
    return jsonify(data)

@app.route('/save',methods = ['POST'])
def save():
    request_data = request.get_json()
    code = request_data['code']
    date = request_data['date']
    time = request_data['time']
    connectdb.save(code, date, time)
    return jsonify({"status": True})

if __name__ == "__main__":
    app.run(debug=True)