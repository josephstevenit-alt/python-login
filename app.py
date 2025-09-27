from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

# MySQL connection
connection = pymysql.connect(
    host="localhost",
    user="root",        # change if needed
    password="joek",    # your MySQL password
    database="student", # your database
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
            cursor.execute(sql, (name, email))
        connection.commit()
        return f"<h3>Thanks, {name}. Your data is saved ✅</h3>"
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"

if __name__ == "__main__":
    app.run(debug=True)
