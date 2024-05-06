import sqlite3

# .db - ombor fayli
# db , ombor fayliga bog'lanish
con = sqlite3.connect("./students.db", check_same_thread=False)
# omborni boshqarish obyekti 
cur = con.cursor()

sql = """CREATE TABLE students(
    name TEXT,
    age INTEGER,
    point INTEGER);"""
# sql buyruqlarini bajarish 
cur.execute(sql)
