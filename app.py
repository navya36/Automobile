from flask import Flask,request,render_template
import mysql.connector as mysql

app=Flask(__name__)

db=mysql.connect(
    host="localhost",
    user="root",
    password="**********",
    database="project"  
)
cur=db.cursor()

app=Flask(__name__)

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/register')
def registerPage():
    return render_template('register.html')

@app.route('/two')
def twoPage():
    return render_template('two.html')


@app.route('/about')
def aboutPage():
    return render_template('about.html')

@app.route('/services')
def homePage():
    return render_template('services.html')


@app.route('/contact')
def contactPage():
    return render_template('contact.html')


@app.route('/registerdata',methods=['post'])
def displayData():
    email=request.form['email']
    psw=request.form['psw']
    pswrepeat=request.form['pswrepeat']
    print(email,psw,pswrepeat) # read data from table
    # use iterator to iterate the records existed in table
    # check whether this rollno is existed in the records
    # if match found display user exist
    # if not then insert data
    sql1="select * from projecttab"
    cur.execute(sql1)
    result1=cur.fetchall()
    data1=[]
    flag=0
    for k in result1:
        print(k)
        data1.append(k)
    for s in data1:
        if email==s[0]: 
            flag=0
            sql1="select * from projecttab"
            cur.execute(sql1)
            result1=cur.fetchall()
            data1=[]
            for k in result1:
                print(k)
                data1.append(k)
        else:
            flag=1
            sql1="select * from projecttab"
            cur.execute(sql1)
            result1=cur.fetchall()
            data1=[]
            for k in result1:
                print(k)
                data1.append(k)
    if flag==1:
        sql="INSERT INTO projecttab(email,password,rpassword) VALUES (%s,%s,%s)"
        values=(email,psw,pswrepeat)
        cur.execute(sql,values)
        db.commit()
        return "registration sucess"
    else:
        return "registration unsucess"

@app.route('/login')
def logindata():
    return render_template('login.html')

@app.route('/logindata',methods=['post'])
def verify():
    email=request.form['email']
    psw=request.form['psw']
    sql="select * from projecttab"
    cur.execute(sql)
    result=cur.fetchall()
    data=[]
    for i in result:
        print(i)
        data.append(i)
    j=0
    for i in data:
        if email==i[0] and psw==i[1]: # you have to use some boolean value
            dec=1
        else:
            dec=0
    if dec==1:
        return render_template("home.html")
    else:
        return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)



