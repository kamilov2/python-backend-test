import datetime
import os

# task 
# test_dir papkani tekshirib ichida .bat formatidagi barcha fayllarni ochirib yuboradigan kod yozing

# dir_list = os.listdir('./test_dir')
# for file in dir_list:
#     if file.endswith(".bat"):
#         os.remove(f"test_dir/{file}")

# task 

# my_dir nomli papka ichiga 3 ta test_1.txt , test_2.txt va test_3.txt fayllarini hosil qiling
for i in range(1,4):
    with open(f"my_dir/test_{i}.txt", "w") as file:
        pass


# dir_list = os.listdir('./') # korsatilgan papkani ichidagi narsalarni korish list qilib
# print(dir_list)

# print(os.getcwd()) # C:\Users\Gnom\Documents\GitHub\python-backend-test
# print(dir(os.path))

# os.remove("./names.txt") # berilgan fayln o'chirish

# open() - faylni ochish uchun 
# open(file, r, encoding )

# f = open(file="./calendar.html",mode="r", encoding="utf-8")
# print(f) # <_io.TextIOWrapper name='./calendar.html' mode='r' encoding='utf-8'>
# # print(dir(f))  #

# print(f.read())  # faylni o'qish

# f = open("time_now.txt", "w", encoding="utf-8") # faylni ochish yoki hosil qilish
# f.write(f"{datetime.datetime.now()}") # faylga joriy sana va vaqtni yozish
# f.close() # faylni yopish


# names = ["Mike", "David", "Solomon","Kane"]

# with open("names.txt", "w") as file:
#     for name in names:
#         file.write(f"{name}\n")


