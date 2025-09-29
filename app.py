from flask import Flask,render_template,request
import mysql.connector
app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login():
    msg = ""
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]
        mydb = mysql.connector.connect (
            host = "sql7.freesqldatabase.com",
            user = "sql7800601",
            password = "2G7MQp34r7",
            database = "sql7800601"
        )
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM LoginDetails WHERE username = %s AND password = %s',
        (username, password))
        account = mycursor.fetchone()
        if account:
            print("Login Successful!")
            name = account[1]
            msg = "Login successful"
            return render_template("login.html", msg=msg)
        else:
            msg = "Incorrect Details, please try again"
            return render_template("login.html", msg=msg) 

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/register_user", methods= ["POST", "GET"])
def register_user():
    msg = ""
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    mydb = mysql.connector.connect (
        host = "sql7.freesqldatabase.com",
        user = "sql7800601",
        password = "2G7MQp34r7",
        database = "sql7800601"
        )
    mycursor = mydb.cursor()
    mycursor.execute('SELECT * FROM LoginDetails WHERE username = %s OR email = %s',
        (username, email))
    account = mycursor.fetchone()

    if account:
        msg = "This account already exists"
    else:
        mycursor.execute("INSERT INTO LoginDetails(username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        mydb.commit()
        msg = "Registration successful"
        return render_template("register.html", msg=msg)

@app.route("/register")
def register():
    return render_template("register.html")


app.run(host='0.0.0.0', port= 8080, debug=True)