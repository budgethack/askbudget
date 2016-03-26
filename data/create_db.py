#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('askbudget_db')
print "Opened database successfully";

conn.execute('''CREATE TABLE QUESTION
        (ID        INTEGER PRIMARY KEY AUTOINCREMENT,
         QUESTION  TEXT NOT NULL);''')
print "Table created successfully";

conn.close()
