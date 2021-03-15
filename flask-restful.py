from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from sqlalchemy_orm import Users, session, Students
import jwt

app = Flask(__name__)
api = Api(app)

class allStudents(Resource):
    def get(self):
        data = []
        results = session.query(Students).all()
        for i in results:
            st=  {}
            st['id'] = i.id
            st['name']=  i.name
            st['email']=  i.email            
            data.append(st)
            print(st)
        return data

    
    def post(self):
        data = request.form
        name = data['name']
        email = data['email']
        student=  Students(name=name, email=email)
        session.add(student)
        session.commit()
        return {'Message': "Created"}

class singleStudent(Resource):
    def delete(self, id):
        student = session.query(Students).filter_by(id=id).first()
        session.delete(student)
        session.commit()
        return {'Message': "Student Deleted"}


    def get(self, id):
        student = session.query(Students).filter_by(id=id).first()
        st =  {}
        st['id'] = student.id
        st['name'] = student.name
        st['email']=  student.email
        return st


class Authenticated(Resource):
    def get(self):
        data = []    
        try:
            token = request.headers['Token']
            print('Token', token)
            if token is not None:
                user = jwt.decode(token, 'login-user', algorithms='HS256')
                if session.query(Users).filter_by(username=user.get('username')):
                    data = []
                    results = session.query(Students).all()
                    for i in results:
                        st=  {}
                        st['id'] = i.id
                        st['name']=  i.name
                        st['email']=  i.email            
                        data.append(st)
                    return data
                else:
                    pass
            else:
                return jsonify({'Message':'Please provide token for access all the students'})
        except:
            return jsonify({'Message':'Please provide token for access all the students'})


api.add_resource(allStudents, '/')
api.add_resource(singleStudent, '/single/<id>')
api.add_resource(Authenticated, '/all-students')


@app.route('/get-token', methods=['POST'])
def token():
    data = request.get_json()
    print(data)
    user = session.query(Users).filter_by(username = data['username']).first()
    if user is None:
        return jsonify({'Message': 'User not found'})
    else:
        return jsonify({"Token": jwt.encode({'username': user.username},'login-user', algorithm='HS256')})

if __name__=='__main__':
    app.run(debug=True)
