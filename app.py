from flask import Flask,render_template
import mysql.connector
from dotenv import load_dotenv
import os
app = Flask(__name__)

def get_db ():
	return mysql.connector.connect(
			host = os.getenv("MYSQL_HOST", "mysql"),
			user = os.getenv("MYSQL_USER", "user"),
			password = os.getenv("MYSQL_PASSWORD", "password"),
			database = os.getenv("MYSQL_DATABASE", "dashboard")
			)
@app.route("/")
def home ():
	
	db = get_db()
	cursor = db.cursor(dictionary = True)
	cursor.execute("select * from users")
	users = cursor.fetchall()
	cursor.close()
	db.close()

	return render_template("index.html", users=users)
if __name__ == "__main__":
	app.run(host="0.0.0.0" , port= 4000)

	
