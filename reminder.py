#Controller
from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3  
from functools import wraps

DATABASE = 'reminder.db'
app = Flask(__name__)
app.config.from_object(__name__)
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    reminder = request.form['reminder']
    if not task or not reminder:
        flash("All fields are required. Please try again.")
        return redirect(url_for('main'))
    else:
        g.db = connect_db()
        g.db.execute('insert into Reminder(task,reminder) values (?, ?)',[request.form['task'], request.form['reminder']])
        g.db.commit()
        g.db.close()
        flash('New entry was successfully posted!')
        return redirect(url_for('main'))

def login():
    session['logged_in'] = True
    return redirect(url_for('main'))

@app.route('/main')
@login_required
def main():
    g.db = connect_db()
    cur = g.db.execute('select * from Reminder')
    reminders = [dict(task=row[0], reminder=row[1]) for row in cur.fetchall()]
    g.db.close()
    return render_template('main.html', reminders=reminders)
    #return "Reminder App"
if __name__ == '__main__':
    app.run(debug=True)
