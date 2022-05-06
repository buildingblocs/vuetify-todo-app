from flask import Flask, jsonify, request
import datetime as dt
import sqlite3

app = Flask(__name__)
app.secret_key = "super_secret_key"

@app.route('/api/new_todo', methods=["POST"])
def new_todo():
    title = request.get_json()["title"]
    msg = ""
    print("title", title)
    
    with sqlite3.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute("INSERT INTO todos (title, isDone) VALUES(?, ?);", (title, 0))
            con.commit()
            msg = "Record successfully added"
            print(msg)
        except:
            con.rollback()
            msg = "error in insert operation"
            print(msg)
    return jsonify([])

@app.route("/api/todos", methods=["GET"])
def todos():
    all_records = []
    with sqlite3.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute("SELECT title, isDone FROM todos")
            records = cur.fetchall()

            for row in records:
                title = row[0]
                isDone = bool(row[1])
                all_records.append(dict(title=title, isDone=isDone));
        except:
            con.rollback()
            msg = "error in insert operation"
            print(msg)
    return jsonify(all_records);

@app.route("/api/clear_todo", methods=["POST"])
def clear():
    with sqlite3.connect("database.db") as con:
        try:
            con.execute('DROP TABLE todos')
            con.execute('CREATE TABLE todos (title TEXT NOT NULL, isDone BIT)')
        except:
            con.rollback()
            msg = "error in insert operation"
            print(msg)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
