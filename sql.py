#Model
import sqlite3
with sqlite3.connect("Reminder.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE Reminder(Task TEXT, Task_Description TEXT)""")
    c.execute('INSERT INTO Reminder VALUES("Meeting","Client from US at 1pm")')
    c.execute('INSERT INTO Reminder VALUES("Go for walk","To park at 5pm")')
    c.execute('INSERT INTO Reminder VALUES("Movie","Lulu PVR at 8pm")')
    c.execute('INSERT INTO Reminder VALUES("Reception","Radisson Blu at 6pm")')
    c.execute('INSERT INTO Reminder VALUES("Interview","UST at 10am")')