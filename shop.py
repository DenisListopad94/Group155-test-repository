import re

"""
pattern - сырая строка
re.match(pattern,str) # поиск по шаблону в начале строки вывод через group
re.search(pattern,str) # поиск по шаблону во всей строке
re.findall(pattern,str) # поиск всех совпадений по шаблону
re.split(pattern,str,[maxsplit = 0]) разбиение по шаблону определённое число раз
re.sub(pattern,repl,str) замена шаблона строкой repl в строке str
"""
"""
.	Один любой символ, кроме новой строки \n.
?	0 или 1 вхождение шаблона слева
+	1 и более вхождений шаблона справа
*	0 и более вхождений шаблона справа
\w	Любая цифра или буква (\W — все, кроме буквы или цифры)
\d	Любая цифра [0-9] (\D — все, кроме цифры)
\D  Любая не цифра [^0-9]
\s	Любой пробельный символ и (\t \r \n) (\S — любой непробельный символ)
\b	Начало или конец слова
\B  Не начало или конец слова
[..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
\	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
^ и $	Начало и конец строки соответственно
{n,m}	От n до m вхождений ({,m} — от 0 до m)
a|b	Соответствует a или b
()	Группирует выражение и возвращает найденный текст
\t, \n, \r	Символ табуляции, новой строки и возврата каретки соответственно
"""
# lst = []
# pattern = r'\w+cat\w+'
# s = 'catпривет я тво тётя вф выфв dsa ad tscat cat dascatas '
# rez = re.findall(pattern,s)
# print(rez)
# lst +=rez
# pattern = r'\bcat\w+'
# s = 'catпривет я тво тётя вф выфв dsa ad tscat cat dascatas '
# rez = re.findall(pattern,s)
# print(rez)
# lst +=rez
# pattern = r'\bcat\b'
# s = 'catпривет я тво тётя вф выфв dsa ad tscat cat dascatas '
# rez = re.findall(pattern,s)
# print(rez)
# lst +=rez
# pattern = r'\w+cat\b'
# s = 'catпривет я тво тётя вф выфв dsa ad tscat cat dascatas '
# rez = re.findall(pattern,s)
# print(rez)
# lst +=rez
# print(len(lst))
import sqlite3

conn = sqlite3.connect('HW_43.db')
cur = conn.cursor()

a = [('sun',), ('sky',), ('world',), ('life',)]

cur.execute('''CREATE TABLE IF NOT EXISTS tab_1(
id INTEGER PRIMARY KEY AUTOINCREMENT, 
col_1 TEXT
)
''')
conn.commit()


cur.executemany('''INSERT INTO tab_1 VALUES(NULL,?)''', a)
conn.commit()

cur.execute('''SELECT * FROM tab_1''')
k = cur.fetchall()
print(k)
