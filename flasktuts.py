from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)




# db.create_all()
# b1 = Books(name='Book1')
# b2 = Books(name = 'Book2')
# b3 = Books(name=  'Book3')

# db.session.add_all([b1, b2, b3])
# db.session.commit()


@app.route('/', methods=['GET'])
def home():
    return "This is the home page"

books_dict=  []
@app.route('/api/all-students', methods=['GET'])
def get_all_students():
    results = Students.query.all()
    for value in results:
        st = {}
        st['id'] = value.id
        st['name'] = value.name
        st['email'] = value.email

        books_dict.append(st)
    return jsonify(books_dict)


@app.route('/api/single_student/<id>', methods=['GET'])
def get_single_students(id):
    student = Students.query.filter_by(id=id).first()
    st_dict = {}
    st_dict[id] = student.id
    st_dict['name']=  student.name
    st_dict['email']=  student.email

    return jsonify(st_dict)



@app.route('/api/create_student', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Students(name=data['name'], email=data['email'])
    db.session.add(student)
    db.session.commit()
    return jsonify({'Message': 'Student created successfully', 'Student': data})


@app.route('/api/update_student/<id>', methods=['PUT'])
def update_student(id):
    student = Students.query.filter_by(id=id).first()
    data = request.get_json()
    if data['name'] is not None and data['email'] is not None:
        student.name = data['name']
        student.email = data['email']
        db.session.commit()
        return jsonify({'Message': 'Updated'})
    else:
        return jsonify({'Message': 'Not update'})


@app.route('/api/student_delete/<id>', methods=['DELETE'])
def delete_student(id):
    student = Students.query.filter_by(id=id).first()
    db.session.delete(student)
    db.session.commit()
    return jsonify({'Message': 'Student deleted'})


if __name__=="__main__":
    app.run(debug=True)




