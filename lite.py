import sqlite3

conn = sqlite3.connect('database.db')  # коннектор для соединения программы с БД
cur = conn.cursor()


# cur.execute("CREATE TABLE user (id SERIAL, first_name text, second_name text);")


def insert(first_name, second_name):
    cur.execute(f"INSERT INTO user (first_name, second_name) VALUES('{first_name}', '{second_name}')")
    conn.commit()


for i in range(10):
    insert(str(i**2), str(i**3))

cur.execute("SELECT first_name, second_name FROM user")
a = cur.fetchall()

for t in a:
    print(f"{t}")
