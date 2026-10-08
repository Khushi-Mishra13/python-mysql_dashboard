from flask import Flask,render_template,request
import mysql.connector
import os
app = Flask(__name__)

def get_db ():
	return mysql.connector.connect(
			host = os.getenv("MYSQL_HOST", "mysql"),
			user = os.getenv("MYSQL_USER", "user"),
			password = os.getenv("MYSQL_PASSWORD", "password"),
			database = os.getenv("MYSQL_DATABASE", "dashboard")
			)

@app.after_request
def add_security_headers(response):
    response.headers["Server"] = ""
    response.headers["X-Content-Type-Options"] = "nosniff"

	
    response.headers["Content-Security-Policy"] = (
        "default-src 'self';"
        "script-src 'self';"
        "style-src 'self';"
        "img-src 'self';"
        "font-src 'self';"
        "connect-src 'self';"
        "media-src 'self';"
        "object-src 'none';"
        "frame-src 'none';"
        "worker-src 'self';"
        "manifest-src 'self';"
        "frame-ancestors 'none';"
        "base-uri 'self'; "
        "form-action 'self';"
    )
    return response 
@app.route("/")
def home ():
	
	db = get_db()
	cursor = db.cursor(dictionary = True)
	cursor.execute("select * from users")
	users = cursor.fetchall()
	cursor.close()
	db.close()

	return render_template("index.html", users=users)
@app.route("/search")
def search():
    username = request.args.get("username", "")

    db = get_db()
    cursor = db.cursor(dictionary=True)

    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    users = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("index.html", users=users)

if __name__ == "__main__":
	app.run(host="0.0.0.0" , port= 5000)

	
