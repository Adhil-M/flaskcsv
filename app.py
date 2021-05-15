from flask import Flask ,render_template ,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import csv

app=Flask(__name__)
app.secret_key='secret tobe set here'


ENV = 'dev'
if ENV =='dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://newuser:1234@localhost/newstudent'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI']=''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class student(db.Model):
    __tablname__='newstudent'
    fullname=db.Column(db.String(50))
    rollno=db.Column(db.Integer,primary_key=True)
    maths=db.Column(db.Integer)
    physics=db.Column(db.Integer)
    chemistry=db.Column(db.Integer)
    biology=db.Column(db.Integer)

    def __init__(self,fullname,rollno,maths,physics,chemistry,biology) :
        self.fullname=fullname
        self.rollno=rollno
        self.physics=physics
        self.maths=maths
        self.chemistry=chemistry
        self.biology=biology
        
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/showtable',methods=['GET'])
def showtable():
    if request.method=='GET':
        print("GOT req")
        data=student.query.all()
        Data=()
        for d in data:
            dl=list(Data)
            student1=(d.fullname,d.rollno,d.maths,d.physics,d.chemistry,d.biology)
            dl.append(student1)
            Data=tuple(dl)
        return jsonify(Data)





with open('./static/MOCK_DATA.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    line=0
    for row in csv_reader:
        if line!=0:
            if db.session.query(student).filter(student.rollno==row[1]).count()==0:
                data=student(row[0],row[1],row[2],row[3],row[4],row[5])
                db.session.add(data)
        line=line+1
    db.session.commit()

if __name__=='__main__':
    app.run(host='0.0.0.0',port=7000)
