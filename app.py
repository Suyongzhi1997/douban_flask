from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def home():
    return index()


@app.route('/movie')
def movie():
    data_list = list()
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        data_list.append(item)
    cur.close()
    con.close()
    print(data_list)
    return render_template("movie.html", movies=data_list)


if __name__ == '__main__':
    app.run(debug=True)
