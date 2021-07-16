# import os
#
# # 1. baza.txt faylini bor yo'qligini tekshirish
# if not os.path.exists("baza.txt"):
#     f = open("baza.txt", "x")
#
# n = int(input("Xodimlar sonini kiriting: "))
#
# f = open('baza.txt', 'a')
#
xodimlar = []
xodim = {
    "id": 0,
    "ism": '',
    "fam": '',
    "maosh": '',
    "manzil": ''
}
#
# for i in range(n):
#     print("Xodim ma'lumotlarini kiriting: ")
#     print(f"{i + 1} - xodim")
#     xodim['id'] = i + 1
#     xodim["ism"] = input("ismi: ")
#     xodim["fam"] = input("familiyasi: ")
#     xodim["maosh"] = input("maoshi: ")
#     xodim["manzil"] = input("manzili: ")
#     temp = xodim.copy()
#     xodimlar.append(temp)
#
# f.write(str(xodimlar))
# f.close()

# # yangilash
# print("Yangilamoqchi bo'lgan xodim ismini kiriting: ")
# key = int(input("ismi: "))
# f = open("baza.txt", 'r')
# data = f.read().split('}, {')
#
# for i in range(len(data)):

# # ekranga chiqarish:
# f = open("baza.txt", 'r')
# data = f.read()
# data = data.split(', ')
#
# for i in data:
#     print(i)

f = open("baza.txt", 'w')
username = "Narzullaev"
password = "1234"
f.write(username + '\n' + str(hash(password)))
f.close()

print("Tizimga kirish: ")
username = input("Login: ")
password = input("password: ")

f = open("baza.txt", 'r')
login = username in f.readline()
passw = str(hash(password)) in f.readline()

if login and passw:
    print("tizimdan o'tdingiz!")
else:
    print("login yoki parol xato!")



# kjhkhgit
from random import randint as ri

salt = ri(1, 1000)
f = open("baza.txt", 'w')
username = "Narzullaev"
password = "1234"
f.write(username + '\n' + str(hash(password) + salt))
f.close()

print("Tizimga kirish: ")
username = input("Login: ")
password = input("password: ")

f = open("baza.txt", 'r')

login = username in f.readline()
passw = str(hash(password) + salt) in f.readline()

if login and passw:
    print("tizimdan o'tdingiz!")
else:
    print("login yoki parol xato!")


