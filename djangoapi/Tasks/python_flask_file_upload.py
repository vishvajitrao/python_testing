from flask import Flask
from flask import request

app = Flask('__name__')


@app.route("/home", methods=['GET'])
def Home():
    user_data = {"name": "Vishvajit", "age": 22, "email": "vishvajitrao@gmail.com"}
    return user_data


@app.route("/product-upload", methods=["POST"])
def ProductUpload():
    user_data = {"name": "Vishvajit", "age": 22, "email": "vishvajitrao@gmail.com"}
    if request.method == 'POST':
        file = request.files["img"]
        print(file.filename)
        print(file.name)
        file.save(file.filename)
    return user_data


if __name__ == '__main__':
    app.run('0.0.0.0', port=8002)
