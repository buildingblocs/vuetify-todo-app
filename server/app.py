from flask import Flask, jsonify, request
from flask import session
import datetime as dt
import sqlite3

app = Flask(__name__)
app.secret_key = "super_secret_key"

@app.route('/api/new_todo', methods=["POST"])
def new_todo():
    title = request.get_json()["title"]
    dueDate = request.get_json()["dueDate"]
    msg = ""
    print("title", title)

    all_records = []
    
    with sqlite3.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute("INSERT INTO todos (title, dueDate, isDone) VALUES(?, ?, ?);", (title, dueDate, 0))
            con.commit()
            msg = "Record successfully added"
            print(msg)

            # get developer detail
            sqlite_select_query = """SELECT title, dueDate, isDone FROM todos"""
            cur.execute(sqlite_select_query)
            print("SELECT DONE")
            records = cur.fetchall()

            for row in records:
                title = row[0]
                dueDate = row[1]
                isDone = bool(row[2])
                print(dueDate)
                all_records.append(dict(title=title, dueDate=dueDate, isDone=isDone));
        except:
            con.rollback()
            msg = "error in insert operation"
            print(msg)
    return jsonify(all_records)

@app.route("/api/clear_todo", methods=["POST"])
def clear():
    with sqlite3.connect("database.db") as con:
        try:
            con.execute('DROP TABLE todos')
            con.execute('CREATE TABLE todos (title TEXT NOT NULL, dueDate timestamp, isDone BIT)')
            print("cleared")
        except:
            con.rollback()
            msg = "error in insert operation"
            print(msg)
    return jsonify([])

if __name__ == '__main__':
    app.run(debug=True)
