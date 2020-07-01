from flask import Flask, redirect, render_template, request, url_for, Blueprint
from database import DB
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'GET':

        with DB() as db:
            values = db.execute('SELECT * FROM calc').fetchall()

        
        return render_template('index.html', values=values)
    
    elif request.method == 'POST':
        name = request.form['name']
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        if num2 == 0:
            return redirect(url_for('index'))
        res = num1 / num2
        print(res)
        with DB() as db:
            db.execute('INSERT INTO calc(name, num1, num2, result) VALUES (?, ?, ?, ?)', (name, num1, num2, res))

        return redirect(url_for('index'))



if __name__ == '__main__':
    app.run()
