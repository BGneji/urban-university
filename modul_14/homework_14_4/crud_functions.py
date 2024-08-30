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


# def add_user(user_id, username, first_name):
#     check_user = cursor.execute("SELECT * FROM Users WHERE id=?", (user_id,))
#     if check_user.fetchone() is None:
#         cursor.execute(f'''
#     INSERT INTO Users VALUES('{user_id}', '{username}','{first_name}', 0)
# ''')
#     connection.commit()

# for i in range(1,5):
#      cursor.execute("INSERT INTO Products(title, description, price) VALUES(?, ?,?)", (f'Product{i}', f'Описание {i}', f'{i*100}'))

def get_all_products():
    connection = sqlite3.connect('home_database.db')
    cursor = connection.cursor()
    all_product = cursor.execute("SELECT * FROM Products")
    res = all_product.fetchall()
    return res




connection.commit()
connection.close()