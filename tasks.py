# for loop tasks

# k = 10
# n = 5

# for i in range(n):
#     print(k)
    
# task 2 
# a = int(input("A ni kirit"))
# b = int(input("B ni kirit"))
# count = 0
# if a < b:
#     for i in range(a,b+1):
#         print(i)
#         count += 1
#     print("Barcha sonlar ", count)
#     print("Barcha sonlar len orqali ", len(range(a,b+1)))

# task 4
# price = 15000
# for i in range(1,11):
#     print(i * price)

# task 5 
# userdan matn qabul qiling toki "z" harfi topilmagunicha barcha harflarini ekranga chiqaring
# input >> 'keldizku'
# output >> k,e,l,d,i,z

# text = input("Matn kirit \n")
# i = 0
# while i <= (len(text) - 1):
#     print(text[i])
#     i += 1
#     if text[i] == "z":
#         break
#***** task 1 ******
# 10 ta 2 xonalik butun son berilgan ulardan faqat 0 bilan tugaganlarini summasini hisoblang
# import random 
# nums = []
# for i in range(10):
#     nums.append(random.randint(10,99))

# print(nums)
# summa = 0
# for x in nums:
#     if str(x)[1] == "0":
#         summa += x 
# print(summa)
    


#***** task 2 ******
# stringda son berilgan  siz shuday kop xonali sonlarni xonalarini alohida alohida qilib oralarida bo'sh joylar bilan chiqaring
# input:"1437239000"
# output:1 437 239 000

#***** task 3 ******
# a = [1, 2, 4, 65, 8, 8, 6, 2, 6, 2, 2, 3]
# b = [4, 5, 65, 7, 98, 5, 12, 2, 65, 89, 47]
# result = []
# ushbu massivlarda ishtirok etgan sonlardan iborat massiv hosil qiling
# hosil bo'lgan massivda faqat sondan bitta bo'lishi kerak 

# for i in a:
#     if i in b:
#         if i in result:
#             print("Bor")
#         else:
#             result.append(i)
# print(result) # [2, 4, 65]


# task 11
# User kiritgan qatorda nechi marta “A” harfi ishtirok etganini hisoblang , agar “A” harfi qator boshidan boshlab 3 martadan kop ishtirok etsa u xolda barcha qolgan “A” harflarini “E” harfiga o’zgartiring

# >>>ananasga
# >>>enenesge

# task 
# n soni berilgan 0 dan n gacha bolgan barcha toq sonlardan iborat massiv hosil qiling
# input : n = 7
# output :[1,3,5]

# tajribasiz 
# n = 21
# result = []
# for i in range(n):
#     if i % 2 == 1:
#         result.append(i)
# print(result) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# tajribali
# print(list(range(1,n,2))) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# TASK
# n ta elementdan tashkil topgan massivda faqat toq sonlarni chiqaruvchi va ularni sonini chiqaruvchi dasturc tuzing
# input: [1,2,3,4,5]
# output: 1,3,5 toqlar soni = 3
# n = 13
# l = list(range(1,n,2))
# print(l)
# print(len(l))

# task 
# n ta elementdan tashkil topgan massivda eng oxirgi elementdan 1 qiymat kichkina elementni ekranga chiqaring aga bunaqa son bolmasa 0 chiqsin 
# input: [1,4,9,8,6]
# output: 0
# input: [1,4,7,2,5]
# output: 4
# arr = [1,4,9,8,10]
# last_item = arr[-1]

# if last_item - 1 in arr:
#     print(last_item - 1)
# else:
#     print(0)


#Task uyga vazifa
#input orqali ism qabul qilsin va uni harfligiga tekshirsin va qoshayotganda bosh harfini katta qilib qoshsin list ga 5 ta ism qabul qilib qoshadi shu royhatdan tasodifiy 3 ta odamni ismini hammasini katta harfda print qilib ekranga chiqaradi

# print([i + i if i in "aiuoe" else i for i in "salom"])
# print("".join([i + i if i in "aiuoe" else i for i in "salom"]))


# a = [i for i in range(10) if i % 2 == 0]
# print(a) # [0, 2, 4, 6, 8]

import datetime
import time
# task 1 
# Taymer qilinadi misol inputdan minut qabul qiladi  5 minut misol 5 minut otgandan kegin vaqt tugadi deb print qilsin har sekund print bolsin nech minut nech sekund qolganligini
# m = 5
# s = m * 60
# for i in range(m):
#     m -= 1
#     sec = 60
#     for x in range(1,60):
#         sec -= 1
#         print(f"{m}:{sec}")
#         time.sleep(1)
# task 2
# Inputdan sana qabul qiladi va u bugungi sanadan katta boladi va inputdan kelgan sanagacha nech kun qolganini nech soat nech minut nech sekund qolganini hisoblasin
# _now = datetime.datetime.now()
# y = int(input("Year"))
# m = int(input("Month"))
# d = int(input("Day"))
# h = int(input("Hour"))
# mi = int(input("Minute"))
# if _now.year < y and _now.month <= m:
#     years = y - _now.year
#     months = m - _now.month
#     current_timeday = datetime.timedelta(days=_now.day, hours=_now.hour,minutes=_now.minute)
#     print(f"{years} years , {months} months and", datetime.timedelta(days=d, hours=h,minutes=mi) - current_timeday)


# date_ = "2024-04-24 , 16:15:30"
# d = date_.split(",")
# years = d[0].split("-")[0] # YYYY
# hours = d[1].split(":")[0] # HH
# print(years, hours)

# task 
# ls = ["python","javascript","cpp","ruby","fortran","assambler"]

# def filter_words(arr):
#     result = []
#     for i in arr:
#         if len(i) > 5:
#             result.append(i)
#     return result

# print(filter_words(ls))

# print(list(filter(lambda word:len(word) > 5, ls)))


# task
# print(input()[::-1])

# s = list(input())
# s.reverse()
# print("".join(s))

# task 
# arr1 = [1,5,4,6,8,7,2,3,1,4,6,9,8]
# arr2 = [5,1,3,6,4,7,9,5,4,1,3,6,5]

# def get_similar_objects(ls1,ls2):
#     result = []
#     for i in ls1:
#         for k in ls2:
#             if i == k:
#                 result.append(i)
#     return list(set(result))

# print(get_similar_objects(arr1,arr2))

# print(list(set([i for i in arr1 if i in arr2])))

# # task 
# input : 52130
# output : [0,3,1,2,5]

# print(list(input()[::-1]))
# res = []
# n = input()
# if len(n) >= 5:
#     for i in n: 
#         res.append(i)
# else:
#     print("5 xona emas")

# res.reverse()
# print(res)

# client = {
#     "name":"John",
#     "age":0,
#     "status":""
# }
# client["age"] = 10
# age = int(input())

# client = {
#     "name":"John",
#     "age":23,
#     "status":"Voyaga yetgan"
# }