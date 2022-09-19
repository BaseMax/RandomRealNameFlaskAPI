from flask import Flask, render_template, jsonify
from functions import CreateSeveralUser

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("README.html")

@app.route("/get")
@app.route("/get/")
def getNewUser():
    user = CreateSeveralUser(1, 0)
    return jsonify({
        "status": 1,
        "names": user
    }), 200

@app.route("/get/<int:amount>")
def getNewUsers(amount):
    users = CreateSeveralUser(amount, 0)
    return jsonify({
        "status": 1,
        "names": users
    }), 200

@app.route("/get/<int:amount>/<string:gender>")
def getFromExactGender(amount, gender):
    if gender.lower() == "male" or gender.lower() == "female":
        users = CreateSeveralUser(amount, 1 if gender == "male" else 2)
        return jsonify({
            "status": 1,
            "names": users
        }), 200
    return jsonify({
        "status": 0,
        "message": "Oops, sorry. Something does not go as we expected."
    }), 400
    
@app.route("/get/<string:gender>")
def getUserFromAnGender(gender):
    if gender.lower() == "male" or gender.lower() == "female":
        user = CreateSeveralUser(1, 1 if gender == "male" else 2)
        return jsonify({
            "status": 1,
            "names": user
        }), 200
    return jsonify({
        "status": 0,
        "message": "Oops, sorry. Something does not go as we expected."
    }), 400
        
@app.errorhandler(404)
def NotFound(error):
    return jsonify({
        "status": 0,
        "message": str(error)
    }), 404


if __name__ == "__main__":
    app.run(debug=True)