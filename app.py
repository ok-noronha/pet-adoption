from flask import Flask, request, render_template, redirect, session, url_for
from flask_mysqldb import MySQL
import datetime
from models import User

app = Flask(__name__)

# MySQL configuration (replace with your MySQL server details)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '0000'
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

app.secret_key = 'your_secret_key'

visitor = 0
logged = 0

@app.route("/")
def route():
    cur = mysql.connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(25) PRIMARY KEY, password VARCHAR(25), is_admin INTEGER)")
    cur.close()
    return redirect(url_for("login"))

@app.route("/login", methods=['GET'])
def login():
    return render_template("login_page.html")


@app.route('/login', methods=['POST',])
def login_post():
    global logged
    # session["user"] = "ok"
    username = request.form["username"]
    password = request.form['password']
    # username="ok"
    # password="pass"
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT password FROM users WHERE username LIKE \"{username}\"")
    p = cur.fetchall()
    cur.close()
    print(p)
    if p == () :
        return redirect(url_for("login", message="No Users with given Username Found"))
    elif p[0][0] == password:
        cur = mysql.connection.cursor()
        cur.execute(f"SELECT username,password,is_admin FROM users WHERE username LIKE \"{username}\"")
        p = cur.fetchone()
        cur.close()
        session["user"] = User(username=p[0], password=p[1], is_admin=p[2]).toString()
        logged+=1
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("login"))


@app.route('/signup',methods=['GET'])
def signup():
    return render_template('login.html', button = "signup")

@app.route('/signup',methods=['POST'])
def signup_post():
    username = request.form['username']
    password = request.form['password']
    cur = mysql.connection.cursor()
    #cur.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(50),password VARCHAR(50))")
    cur.execute(f"INSERT INTO users VALUES ({username}, {password})")
    mysql.connection.commit()
    cur.close()
    return redirect("/home")

@app.route("/dashboard",methods=['GET'])
def dashboard():
    return render_template("base.html", \
                           user=session["user"])
    

@app.route("/dashboard",methods=['POST'])
def dash():
    good=["good","positive"]
    bad=["bad","negative"]
    sum=0
    text=request.form["review_text"]
    cur=mysql.connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS words(word varchar(255))")
    for word in text.split(" "):
        cur.execute(f"INSERT INTO words VALUES (\"{word}\") ")
        if word in good:
            sum+=1
        if word in bad:
            sum-=1
    #
    cur.execute("SELECT word ,count(*) FROM words group by word")
    res =cur.fetchall()
    cur.close()
    mysql.connection.commit()
    print(res)
    sent=""
    if sum>0:
        sent="postive"
    elif sum<0:
        sent="negative"
    else:
        sent="neutral"
    prvsnt = session.get('prv_sent')
    session["prv_sent"] = sent
    return render_template("dashboard.html", \
                           user = session["user"], \
                           visitors = visitor, \
                           logged= logged, \
                           conv_rate = logged/visitor, \
                           text=text, \
                           res=res, sent=sent,prv_sent=prvsnt)


@app.route("/dashboards",methods=['GET'])
def dashboards():
    user_agent = request.headers.get("User-Agent")
    visitor_ip = request.remote_addr  # Get the visitor's IP address
    visited_url = request.url        # Get the URL they accessed
    timestamp = datetime.datetime.now()
    print(user_agent,visitor_ip,visited_url,timestamp)
    return redirect("/dashboard")

app.run()