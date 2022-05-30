# import sqlite3
#
# with sqlite3.connect('Cars.db') as conn:
#     cursor = conn.cursor()
#     conn.commit()
#
#     cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     mark TEXT,
#     year INTEGER,
#     speed REAL
#     )""")
#     conn.commit()
#     Cars =[
#         ('Mazda', 2015, 289.13),
#         ('BMW', 2011, 302.53),
#         ('ZAZ', 1962, 95.53)
#     ]
    # cursor.execute("""INSERT INTO cars VALUES(NULL,?,?,?)""",('Volvo',2005,256.53))
    # conn.commit()
    # cursor.executemany("""INSERT INTO cars VALUES(NULL,?,?,?)""",Cars)
    # conn.commit()
    # cursor.execute("""SELECT * FROM cars WHERE year > 2000 LIMIT 2""")
    # k  = cursor.fetchall()
    # for item in k:
    #     print(*item)

    # cursor.execute("""UPDATE Cars SET speed = '278.23', year = '2020' WHERE id = 1 """)
    # conn.commit()
    #
    # cursor.execute("""DELETE FROM cars WHERE id = 3""")
    #
    # cursor.execute("""SELECT * FROM cars """)
    # k  = cursor.fetchall()
    # for item in k:
    #     print(*item)

# public(публичный)
# protected (защищённый)
# private (приватный)
# class A:
#     a = 2
#     _b = 5
#     __c = 7
#     def info(self):
#         print(self.__c)
#
# obj_A = A()
# print(obj_A.a)
# print(obj_A._b)
# print(obj_A._A__c)
# obj_A.info()
