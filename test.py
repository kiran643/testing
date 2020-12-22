import mysql.connector
#from flaskext.mysql import MySQL
from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

cnx = mysql.connector.connect(user='root',password='1234',host='localhost',database='test',auth_plugin='mysql_native_password')
cursor = cnx.cursor()
@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        
        data = request.get_json()
        uid = data['uid']
        name = data['name']
        pwd = data['pwd']
        q = ("insert into users(uid,uname,pwd) values(%s, %s, %s)")
        cursor.execute(q,(uid,name,pwd))
        cnx.commit()
        #cursor.close()
        #return jsonify({'name':'ok'}) 
        return jsonify({'data':'insert successfully'})

@app.route('/disp', methods=['GET','POST'])
def disp():
    if request.method == 'GET':
        q = ("select * from users")
        cursor.execute(q)
        re = cursor.fetchall()
        #uidd = re['uid']
        #cnx.close()
        return jsonify(re)


@app.route('/update', methods=['GET','POST','PUT'])
def update():
    if request.method == 'PUT':
        cnx = mysql.connector.connect(user='root',password='1234',host='localhost',database='test',auth_plugin='mysql_native_password')
        cursor = cnx.cursor()
        data = request.get_json()
        uid = data['uid']
        name = data['name']
        pwd = data['pwd']
        q = ("select * from users where uid=%s")
        cursor.execute(q,(uid,))
        re = cursor.fetchall()
        if re:
            q1 = ("update users set uname=%s,pwd=%s where uid=%s")
            cursor.execute(q1,(name,pwd,uid)) 
            cnx.commit()
            return jsonify({'data':"update successfully"})
        return jsonify({"msg":"No data found"})

@app.route('/delete', methods=['GET','POST','DELETE'])
def delete():
    if request.method == 'DELETE':
        d = request.get_json()
        u = int(d['uid'])
        q = ("select * from users where uid=%s")
        cursor.execute(q,(u,))
        re = cursor.fetchall()
        if re:
            q1 = ("delete from users where uid=%s")
            cursor.execute(q1,(u,)) 
            cnx.commit()
            return jsonify({"mgs":"delete successfuly"})
        return jsonify({"msg":"No data found"})
        

if __name__ == '__main__':
    app.run(debug=True)    
                             
