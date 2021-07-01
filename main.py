# # Tasodifiy sonlar
#
# import random
# import math
# for i in range(10):
#     print(random.random())
#
# for i in range(10):
#     print(round(random.random(),2))
#
# for i in range(10):
#     print(math.ceil(random.random()*10))

# # randint
# import random
# print(random.randint(1,10))
# # 1-. 1 dan 10 gacha bo'lgan butun son kiriting
# # va randint bilan generatsiya qilingan son bilan solishtiring
# kiritilganson=int(input("son="))
# tasodifiyson=(random.randint(1,10))
# if kiritilganson==tasodifiyson:
#     print(tasodifiyson)
#     print("yutdingiz")
# else:
#     print(tasodifiyson)
#     print("Dam oling")

# import random
# a=int(input("a ni kiriting"))
# b=(random.randint(1,10))
# print(b)
# if a==b:
#     print("OK")
# else:
#     print("NO")

# # 1-. 1 dan 10 gacha bo'lgan butun son kiriting
# # va randint bilan generatsiya qilingan son bilan solishtiring
# va bu dasturda yutmaguningizcha siklni to'xtatmang
# import random
# imkoniyat=1
# Yutdimi=False
# while imkoniyat<=5:
#     tasodifiyson = (random.randint(1, 10))
#     kiritilganson=int(input("son="))
#     if kiritilganson==tasodifiyson:
#         print("yutdingiz")
#         Yutdimi=True
#         break
#     imkoniyat+=1
#
# if not Yutdimi:
#     print("Yutqazdingiz")