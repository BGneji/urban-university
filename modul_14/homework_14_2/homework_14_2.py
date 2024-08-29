import sqlite3
import random

connection = sqlite3.connect('not_telegram_14_2.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
id  INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER, 
balance INTEGER NOT NULL
)
""")

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Удаление пользователя с id=6
# cursor.execute('DELETE FROM Users WHERE id = 6')
# Подсчитать общее количество записей.
cursor.execute('SELECT count(username) FROM Users')
total_users = cursor.fetchone()[0]
print(f'Подсчёт кол-ва всех пользователей {total_users}')

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
print(f'Подсчёт суммы всех балансов {all_balances}')

print(all_balances / total_users)

# cursor.execute("SELECT * FROM Users")
# all_ = cursor.fetchall()
# for elem in all_:
#     print(elem)


connection.commit()
connection.close()
