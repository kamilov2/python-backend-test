# function - kod bo'lagi , dasturni istalgan joyidan istalgan marta ishga tushirish mumkin 

# def funktsia_nomi(funktsiya qqabul qiluvchi qiymatlar):
#     funktsiyani tanasi 
#     return funktsiya qaytaruvchi natijani 

# def plus(number_1,number_2):
#     """Return summ of two numbers """
#     result = number_1 + number_2
#     return result

# for i in range(1,11):
#     print(plus(1,i)) 
    
# print(plus.__doc__) # Return summ of two numbers 
# print(plus(5,10)) # 15

# def minus(a,b):
#     return a - b 

# print(minus(10,2)) # 8


# def test(x=1,y=0,z=10):
#     return x

# print(test()) # missing 1 required positional argument: 'x
# print(test(2)) # 2
# print(test()) # 1

# def main_pow(x,y):
#     return x ** y
 
# print(main_pow(2,2)) # 4
# arr = [1,2,3,4,5,6,7,8,9,10]

# def main_pow(*args):
#     print(type(args)) # <class 'tuple'>
#     for i in args:
#         print(i)
        
# print(main_pow(1,2,3,4,"salom",True,7,[1,2,3],9,10))
    

# def check_kwargs(**kwargs):
#     print(type(kwargs)) # <class 'dict'>
#     for i in kwargs.items():
#         print(i)
#     print(kwargs.get("a")) # 1

# print(check_kwargs(a=1,b=2,c=3))

# def super_func(*args,**kwargs):
#     print(type(kwargs)) # <class 'dict'>
#     for i in kwargs.items():
#         print(i)
        
#     print(type(args)) # <class 'tuple'>
#     for i in args:
#         print(i)

# super_func(1,2,3,a=4,b=5)

# args = arguments 
# kwargs = keyword arguments 


# lambda - bir qatorli , nomsiz funksiya , 1 yoki 2 ta amalni bajarish uchun qollaniladi 

# x = lambda a,b: a + b
# print(x(1,2)) # 3

# map , zip , filter 

# map - korsatilgan funksiyani berilgan ketma-ketlik elementlarini barchasiga qollaydi 
# arr = [1,2,3,4,5]
# res = [3,4,5,6,7]
# def plus_two(num):
#     return num + 2
# res = []
# for i in arr:
#     res.append(plus_two(i))
# print(res) # [3, 4, 5, 6, 7]

# print(map(plus_two,arr))  # <map object at 0x000002108FC59A50>
# print(list(map(plus_two,arr))) # [3, 4, 5, 6, 7]

# print(list(map(lambda x: x + 2, arr))) # [3, 4, 5, 6, 7]


# lst = ["python","javascript","ruby","go"]

# print(list(map(lambda elem: elem.capitalize() ,lst))) # ['Python', 'Javascript', 'Ruby', 'Go']

# zip - berilgan ketma-ketliklardan baravar miqdorda element olib alohida qilib qaytaradi

# letters = "abc"
# nums = [1,2,3]
# symbols = "!@#"
# bools = [True,False,None]
# print(list(zip(letters,nums,symbols,bools))) 
# [('a', 1, '!', True), ('b', 2, '@', False), ('c', 3, '#', None)]
# d = {}
# for k,v in zip(letters,nums):
#     d.update({k:v})
# print(d) # {'a': 1, 'b': 2, 'c': 3}

# print({k:v for k,v in zip(letters,nums)}) # {'a': 1, 'b': 2, 'c': 3}

# d = dict(zip(letters,nums))
# print(d) # {'a': 1, 'b': 2, 'c': 3}


# filter - korsatilgan funksiyadagi shart boyicha ketma-ketlik elementlari filterlaydi 

nums = [1,4,5,9,78,6,2,1,5,4,8,9,3]
print(list(filter(lambda x: x > 5, nums))) # [9, 78, 6, 8, 9]

words = ["python","javascript","ruby","go"]
print(tuple(filter(lambda word : "o" in word,words))) # ('python', 'go')

students = [
    {
        "name":"Bob",
        "point":7
    },
        {
        "name":"Sara",
        "point":8
    },
        {
        "name":"Mike",
        "point":3
    },
        {
        "name":"David",
        "point":9
    },
        {
        "name":"Miguel",
        "point":4
    },
]

# Ushbu malumotlarni filterlab o'quvchilar orasida faqat 5 balldan yuqori olganlarni chiqaring