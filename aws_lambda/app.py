from flask import Flask
from flask import Response
import json



app = Flask(__name__)


@app.route('/get-users', methods=["GET"])
def getUser():
    response = {"message": "Data fetch successfully", "data": [{'name': 'Vishvajit'}, {'name': 'shivam'}]}
    return Response(response=json.dumps(response), status=200)


if __name__ == '__main__':
    app.run(port=7000, host='0.0.0.0')