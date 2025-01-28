import flask
from flask import Flask, request, render_template, redirect, jsonify, session
import mysql.connector
import _mysql_connector
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

var1 = Flask(__name__)
var1.secret_key = 'your_secret_key_here'

db = ""
dbb = ""
us = ""
s1 = ""


@var1.route("/", methods=['GET', 'POST'])
def homee():
    if request.method == "POST":
        feed = request.form["feedback"]
        s = "feedback successfully sent"
        return render_template("first.html", s=s)
    else:
        return render_template("first.html")


@var1.route("/enter", methods=['GET', 'POST'])
def roomch():
    global db
    if request.method == 'POST':
        try:
            db = request.form["roomname"]
            session['room'] = db
            mydb4 = mysql.connector.connect(host="localhost", user="root", passwd="sri@vatsav840", database=db)
            myc4 = mydb4.cursor()
            if mydb4:
                ss = "your room name has matched"
                return redirect('/login')
        except Exception as e:
            ss1 = "No room matched! or else any unknown error occured"
            return render_template("h1.html", ss1=ss1)
    else:
        return render_template("h1.html")


@var1.route("/createdb", methods=['GET', 'POST'])
def creatingdb():
    global dbb
    if request.method == 'POST':
        dbb = request.form["databasen"]
        mydb4 = mysql.connector.connect(host="localhost", user="root", passwd="sri@vatsav840", database="testt")
        myc4 = mydb4.cursor()
        try:
            ss = f"CREATE DATABASE {dbb}"
            myc4.execute(ss)
            res4 = myc4.fetchone()
            if res4:
                cs1 = "Something wrong while creating room"
                return render_template("h2.html", cs1=cs1)
            else:
                cs2 = "Room successfully created"
                try:
                    minedb = mysql.connector.connect(host="localhost", user="root", passwd="sri@vatsav840",
                                                     database=dbb)
                    minec = minedb.cursor()
                    ss2 = "CREATE TABLE sign (username VARCHAR(45) , pass VARCHAR(45), upiid VARCHAR(45))"
                    ss3 = f"CREATE TABLE {dbb}(username VARCHAR(45) , descc TEXT,date varchar(45),amount int)"
                    minec.execute(ss2)
                    minec.execute(ss3)
                    res5 = minec.fetchone()
                    res6 = minec.fetchone()
                    if res5 and res6:
                        es = "Error in creating table"
                        return render_template("h2.html")
                    else:
                        cs3 = "with no issues"
                        return render_template("h2.html", cs2=cs2, cs3=cs3)
                except Exception as e:
                    es = "Error in connecting to database"
                    return render_template("h2.html", cs2=cs2, es=es)

        except Exception as e:
            cs3 = "Try another name for your room"
            return render_template("h2.html", cs3=cs3)

    else:
        return render_template("h2.html")


@var1.route("/sigup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        s1 = request.form["username"]
        s2 = request.form["password"]
        s3 = request.form["upi"]
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="sri@vatsav840", database=db)
        myc = mydb.cursor()
        try:
            qq4 = "insert into sign (username,pass,upiid) values(%s,%s,%s)"
            values = (s1, s2, s3)
            myc.execute(qq4, values)
            res4 = myc.fetchone()
            mydb.commit()
            mydb.close()
        except Exception as e:
            ss = "try with another username"
            return render_template("h3.html", ss=ss)
        if res4:
            pop1 = "oops!Signup not successfull try again!"
            return render_template("h3.html", pop1=pop1)
        else:
            pop = "Signup successfull! You can login now"
            return render_template("h3.html", pop=pop)
    else:
        return render_template("h3.html")


@var1.route("/login", methods=["POST", "GET"])
def loginpage():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="sri@vatsav840", database=db)
            myc = mydb.cursor()
            q = "SELECT * FROM sign WHERE username=%s AND pass=%s"
            values = (username, password)
            myc.execute(q, values)
            res = myc.fetchone()
            if res:
                session['username'] = username  # Storing username in session
                return redirect("/bill")
            else:
                s = "Invalid credentials! Try again"
                return render_template("h4login.html", s=s)
        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            return render_template("h4.html", es="An error occurred. Please try again.")
    else:
        return render_template('h4login.html')


@var1.route("/bill", methods=['POST', 'GET'])
def enterbill():
    if 'username' not in session:
        return redirect("/login")

    if request.method == 'POST':
        desci = request.form["describe"]
        date = request.form["date"]
        amou = request.form["amount"]
        username = session['username']  # Retrieve username from session

        try:
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="sri@vatsav840", database=db)
            myc = mydb.cursor()

            # Insert a new entry
            qq4 = f"INSERT INTO {db} (username, descc, date, amount) VALUES (%s, %s, %s, %s)"
            values = (username, desci, date, amou)
            myc.execute(qq4, values)

            mydb.commit()
            mydb.close()

            pop = "Data stored successfully"
            try:
                mydbb = mysql.connector.connect(host="localhost", user="root", passwd="sri@vatsav840", database=db)
                mycc = mydbb.cursor()
                query = f"SELECT DISTINCT username FROM {db}"
                mycc.execute(query)
                unique_names = [row[0] for row in mycc.fetchall()]
                lenn = len(unique_names)
                session['lengthoftable'] = lenn
                mycc.close()
                mydbb.close()
                sender_email = "deepakeppakayala008@gmail.com"
                password = "your_password"
                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = ", ".join(unique_names)
                message["Subject"] = "Test Email"
                body = (f"{username} has uploded in (room) {db}\n"
                        f"description:{desci}\n date:{date}\n amount:{amou}")
                message.attach(MIMEText(body, "plain"))
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()  # Secure the connection
                    server.login(sender_email, "scuu acko cdrr cmkr")
                    text = message.as_string()
                    server.sendmail(sender_email, unique_names, text)
                    succe = "mail sent!!"
                return render_template("bill.html", succe=succe, pop=pop)
            except Exception as e:
                erm = "error while sending mail"
                return render_template("bill.html", erm=erm)

        except mysql.connector.Error as err:
            print("MySQL Error:", err)
            return render_template("bill.html", ss="An error occurred. Please try again.")
    else:
        return render_template("bill.html")


@var1.route('/summary', methods=['GET', 'POST'])
def summaryy():
    if 'username' not in session:
        return redirect("/login")

    us = session['username']
    room_name = session.get('room')
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="sri@vatsav840", database=room_name)
        myc = mydb.cursor()
        q = f"SELECT * FROM {room_name} WHERE username=%s"
        myc.execute(q, (us,))
        res = myc.fetchall()
        return render_template("summ.html", res=res)
    except Exception as e:
        excp = "Error!"
        return render_template("summ.html", excp=excp)


@var1.route('/spliting', methods=['GET', 'POST'])
def split():
    if 'username' not in session:
        return redirect("/login")
    db_pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="my_pool",
        pool_size=5,
        host="localhost",
        user="root",
        passwd="sri@vatsav840",
        database=session['room']
    )

    try:

        mydbz = db_pool.get_connection()
        mycz = mydbz.cursor()

        query = f"SELECT username, SUM(amount) FROM {session['room']} GROUP BY username"
        mycz.execute(query)
        user_balances = {row[0]: row[1] for row in mycz.fetchall()}
        mycz.close()
        mydbz.close()

        # Calculate average
        num_users = len(user_balances)
        total_expense = sum(user_balances.values())
        average_expense = total_expense / num_users

        balances_diff = {user: balance - average_expense for user, balance in user_balances.items()}

        debtors = {user: balance for user, balance in balances_diff.items() if balance < 0}
        creditors = {user: balance for user, balance in balances_diff.items() if balance > 0}

        transactions = []
        for debtor, debtor_balance in debtors.items():
            for creditor, creditor_balance in creditors.items():
                if debtor_balance != 0 and creditor_balance != 0:
                    amount_to_transfer = min(abs(debtor_balance), creditor_balance)
                    transactions.append((debtor, creditor, amount_to_transfer))
                    balances_diff[creditor] -= amount_to_transfer
                    balances_diff[debtor] += amount_to_transfer

        return render_template("splitbill.html", transactions=transactions, average_expense=average_expense)
    except Exception as e:
      print("Error in split route:", e)
      error_message = "Error while splitting"
      return render_template("splitbill.html", error_message=error_message)

if __name__ == "__main__":
    var1.run(host="0.0.0.0", port=5001, debug=True)
