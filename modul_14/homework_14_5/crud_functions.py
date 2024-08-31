import sqlite3
import random

connection = sqlite3.connect('home_database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id  INTEGER PRIMARY KEY ,
title TEXT NOT NULL,
description TEXT,
price INT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id  INTEGER PRIMARY KEY ,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INT NOT NULL,
balance  INT NOT NULL
);
''')


def add_user(username, email, age):
    connection = sqlite3.connect('home_database.db')
    cursor = connection.cursor()
    count_user = cursor.execute("SELECT MAX(id) FROM Users").fetchone()
    cursor.execute(f'''
    INSERT INTO Users VALUES('{count_user[0] + 1}', '{username}', '{email}','{age}', {1000})
''')
    connection.commit()


# for i in range(1,5):
#      cursor.execute("INSERT INTO Products(title, description, price) VALUES(?, ?,?)", (f'Product{i}', f'Описание {i}', f'{i*100}'))

def get_all_products():
    connection = sqlite3.connect('home_database.db')
    cursor = connection.cursor()
    all_product = cursor.execute("SELECT * FROM Products")
    res = all_product.fetchall()
    return res


def is_included(username):
    connection = sqlite3.connect('home_database.db')
    cursor = connection.cursor()
    user = cursor.execute("SELECT username FROM Users WHERE username=?", (username,)).fetchone()
    print(user)
    if user is None:
        return False
    return True


connection.commit()
connection.close()
