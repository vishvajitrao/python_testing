from flask import Flask, Response, json


app = Flask(__name__)

students = [
    {
        "student_id": 1,
        "student_name": "Vishvajit",
        "address": "Noida"
    },
    {
        "student_id": 2,
        "student_name": "Shivam",
        "address": "Delhi"
    },
    {
        "student_id": 3,
        "student_name": "Kumar",
        "address": "Pune"
    },
    {
        "student_id": 4,
        "student_name": "John",
        "address": "USA"
    }
]

@app.route("/home", methods=['GET'])
def home():
    return Response(response=json.dumps(students), status=200)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000)