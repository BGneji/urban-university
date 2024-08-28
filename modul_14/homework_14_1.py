import sqlite3
import random
connection = sqlite3.connect('not_telegram.db')
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
# добавление данных в базу данных
for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)", (f'User{i}', f'example{i}@gmail.com', (i*10), 1000))

# Обновите balance у каждой 2ой записи начиная с 1ой на 500:
for user in range(1, 11):
    cursor.execute("UPDATE Users SET balance = ? WHERE id % 2 = 1", (500,))

# Удалите каждую 3ую запись в таблице начиная с 1ой
cursor.execute('DELETE FROM Users WHERE id % 3 = 1')
# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
cursor.execute('SELECT username, email, age, balance  FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    print(user)


connection.commit()
connection.close()
