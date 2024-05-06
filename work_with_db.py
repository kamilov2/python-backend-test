import sqlite3
# pip install requests  - ornatib olish uchun
import requests  # type: ignore
import time

url = "https://jsonplaceholder.typicode.com/users"

data = requests.get(url)

con = sqlite3.connect("./users.db", check_same_thread=False)
cur = con.cursor()

# sql = """CREATE TABLE users(
#     id IDENTITY(1,1) PRIMARY KEY ,
#     name TEXT,
#     username TEXT,
#     email TEXT,
#     address TEXT,
#     phone TEXT,
#     website TEXT,
#     company TEXT);"""

for user in data.json():
    sql = f"""INSERT INTO users(id,name,username,email,address,phone,website,company)
            VALUES(
            {int(user.get("id"))},
            "{user.get('name')}",
            "{user.get('username')}",
            "{user.get('email')}",
            "{user.get('address')['street']} {user.get('address')['city']}",
            "{user.get('phone')}",
            "{user.get('website')}",
            "{user.get('company')['name']}");
    """
    # print(sql)
    try:
        cur.execute(sql)
    except sqlite3.DatabaseError as er:
        print(er)
    else:
        con.commit()
        time.sleep(1)
        print("OK")
else:
    cur.close()
    con.close() 

# print(data.status_code) # 200 - OK

# print(data) # <Response [200]>
# print(dir(data)) # 
# print(data.json()) # 10 user data json


# .db - ombor fayli
# db , ombor fayliga bog'lanish
# con = sqlite3.connect("./students.db", check_same_thread=False)
# omborni boshqarish obyekti 
# cur = con.cursor()

# sql = """CREATE TABLE students(
#     name TEXT,
#     age INTEGER,
#     point INTEGER);"""
# sql buyruqlarini bajarish 
# cur.execute(sql)
