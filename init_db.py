import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO notes (content) VALUES (?)", ('# The First Note',))
cur.execute("INSERT INTO notes (content) VALUES (?)", ('_Another note_',))
cur.execute("INSERT INTO notes (content) VALUES (?)", ('Visit [this page](https://www.digitalocean.com/community/tutorials) for more tutorials.',))

connection.commit()
connection.close()
