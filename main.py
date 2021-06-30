# a=int(input("a="))
# if a>0 :
#     print("a=musbat son")
# else:
#     if a==0:
#         print("a nolga teng")
#     else:
#         print("a=manfiy son")
# print(a)

# a=int(input("a="))
# if a%2==0:
#     print("a=juft son")
# else:
#     print("a=toq son")
#     print(a)

# import math
# x=float(input("x koordinatani kiriting="))
# y=float(input("y koordinatani kiriting="))
# r=4
# l=math.sqrt(x**2+y**2)
# if x>0 and y>0:
#     if l<r:
#         print("I-chorak ichkarida")
#     else:
#         print("I-chorak tashqarida")
# elif x<0 and y>0:
#     if l < r:
#         print("II-chorak ichkarida")
#     else:
#         print("II-chorak tashqarida")
# elif x<0 and y<0:
#     if l < r:
#         print("III-chorak ichkarida")
#     else:
#         print("III-chorak tashqarida")
# elif x>0 and y<0:
#     if l < r:
#         print("IV-chorak ichkarida")
#     else:
#         print("IV-chorak tashqarida")
# elif x==0 and y!=0:
#     print("y o'qida yotadi")
# elif x!=0 and y==0:
#     print("x o'qida yotadi")
# elif x==0 and y==0:
#     print("koordinata boshida yotadi")

# a=int(input("a="))
# b=int(input("b="))
# if a==b:
#     print("kvadrat")
# else:
#     print("kvadrat emas")
#
# a=int(input("a="))
# if a>=1000 and a<10000:
#     print("Turt xonali son")
# else:
#     print("Turt xonali son emas")

# import math
# x=float(input("x sonni kiriting="))
# if x<-2 or x>2:
#     y=2*x
# else:
#     y=-3*x
# print(y)

# #  80-bet 1-masala
# x=int(input("x="))
# unlar = x // 10
# birlar = x % 10
# if unlar % 2 == 0:
#     print("unlar xonasidag juft")
# else:
#     print("unlar xonasidag toq")
# if birlar % 2 == 0:
#     print("birlar xonasidag juft")
# else:
#     print("birlar xonasidag toq")

# # Kabisa yili
# yil=int(input("yil=>"))
# if yil%4==0:
#     if yil%100==0 and yil%400!=0:
#         print("kabisa yili emas")
#     else:
#         print("kabisa yili")
# else:
#     print("kabisa yili emas")

# polidrom sonlar 212=212, ...
# x=int(input("x="))
# if x//100==x%10:
#     print("polidrom son")
# else:
#     print("Polidrom emas")


#  80-bet 2-masala
# x=int(input("x="))
# birlar = x % 10
# unlar = x % 100//10
# yuzlar=x//100
# if birlar==unlar or unlar==yuzlar or yuzlar==birlar:
#     print("Bir xil raqam mavjud")
# else:
#     print("Bir xil raqam mavjud emas")

# if unlar % 2 == 0:
#     print("unlar xonasidag juft")
# else:
#     print("unlar xonasidag toq")
# if birlar % 2 == 0:
#     print("birlar xonasidag juft")
# else:
#     print("birlar xonasidag toq")

# polidrom sonlar 4-xonali son uchun 2112=2112, ...
# x=int(input("x="))
# if x//1000==x%10 and x % 100//10 == x % 100//10:
#      print("polidrom son")
# else:
#      print("Polidrom emas")

     # polidrom sonlar 4-xonali son uchun 2112=2112, ...
     # x = int(input("x="))
     # if x // 1000 == x % 10 and x % 100 // 10 == x % 100 // 10:
     #      print("polidrom son")
     # else:
     #      print("Polidrom emas")

# 80-bet 3-masala
# a=int(input("a="))
# b=int(input("b="))
# if a%2==0:
#     print(f"a={a} soni juft")
# if b%2==0:
#     print(f"b={b} soni juft")

# #  Polindromlikka tekshirish
# son=int(input("son="))
# a=son
# xonalarsoni=1
#
# while True:
#     a=a//10
#     if a!=0:
#         xonalarsoni+=1
#     else:
#         break
# print(xonalarsoni)
#
# teskarison=0
# a=son
# xonaindeksi=0
# while True:
#     teskarison+=a//(10**(xonalarsoni-1))%10*(10**xonaindeksi)
#     xonaindeksi+=1
#     xonalarsoni-=1
#     if xonalarsoni==0:
#         break
# print(teskarison)
# if son==teskarison:
#     print("polidrom son")
# else:
#     print("polidrom son emas")

# # 20 dan 1 gacha butun sonlarni chiqarish
# i=20
#
# while i>=2:
#
#     i-=2
#     print(i)

# # 87-bet
# import math
# n=int(input("n="))
# k=int(input("k="))
# n>0
# k>0
# a=math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
# print(a)

# # 1 dan 10 gacha butun sonlar kvadratini chiqarish 64 chiqmasin
# i=0
# while i<10:
#     i+=1
#     if i**2==64:
#         continue
#     print(i**2)

# 1 dan 10 gacha butun sonlarni 8 ning ikkilanganigacha chiqarish
# i=0
# while i<10:
#     i+=1
#     print(i * 2)
#     if i*2==8*2:
#         break
#     print(i*2)

# # 9-sinf 88 - bet 2 - masala
#
# while True:
#     n=int(input("n="))
#     k = int(input("k="))
#     if k<=n:
#         break
#     else:
#         print(" k soni n ga teng yoki kichik bo'lsin")
# print(f"{n} {k}")
#
# i=0
# nFaktorial=1
# while i<n:
#     i+=1
#     nFaktorial*=i
#
# i=0
# kFaktorial=1
# while i<k:
#     i+=1
#     kFaktorial*=i
#
# i=0
# nkFaktorial=1
# while i<(n-k):
#     i+=1
#     nFaktorial*=i
# print(kFaktorial)
#
# javob=nFaktorial/(kFaktorial*nkFaktorial)
# print(javob)

# 9-sinf 88 bet 3 masala
# a=int(input("a="))
# b = int(input("b="))
# i=a
# while i<b:
#     i+=1
#     if i%2==1:
#         continue
#
#     print(i)

# # 9-sinf 88 bet 3 masala
# a=int(input("a="))   #a ni kiritamiz
# b = int(input("b=")) #b ni kiritamiz
# i=a  # i ni vaqtincha a ga o\zlashtiramiz
#
# if i%2==0: # agar a juft bo\lsa o\z holida qoldirilsin
#     pass
# elif i%2==0: # agar a toq bo\lsa o\zidan keyingi i ni tenglaymiz
#     i=a+1
#
# while i<b:  # i soni b sonida kichik bo\lsa davom etsin
#     if i%2==0:
#         print(i) #i ni chiqarsin
#         i+=2 # i ni qiymati har safar 2 ga orttirilsin

# # 9-sinf 88 bet 4 masala
# n=int(input("n="))
# i=int(input("i="))
# while i<n:
#     print(i**2)
#     i+=1

# # 9-sinf 88 bet 4 masala
# n=int(input("n="))
# i=0
#
# while i**2<n:
#     i += 1
#     print(i)

# # maxsus masala 1
# # ism familiya kiritish bundaagar kiritgan satrda probel bulmasa qayta kiritsin
# while True:
#     fullName=input("Ism familiya:  ")
#     fNameArray=fullName.split(' ')
#     if len(fNameArray)==2:
#         break
#     elif len(fNameArray)>2:
#             print("Faqat ism familiya kerak!")
#     else:
#         print("Ism familiya kiriting!")
# while True:
#     age=int(input("Yoshingizni kiriting:"))
#     if int(age)>=18:
#         break
#     else:
#         print("18 yoshdan katta bo'lsin")

# for loop haqida
# ism='Jamshid'
# index=0
# while index<len(ism):
#     print(ism[index])
#     index+=1

# ism = 'Jamshid'
# for i in ism:
#     print(i)

#  for yordamida 1 dan 10 gacha sonlarni chiqaring

# sonlar=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# kunlar=("Du", "Se", "Chor", "Pay", "Juma", "Sh", "Yak")
#
# for son in sonlar:
#      print(son)
#
# for kun in kunlar:
#      print(kun)

#  0-9 sonlari
# for son in range(2,10):
#      print(son)

#  2-7 sonlari
# for son in range(2,7):
#      print(son)

#  2 dan -15 gacha  sonlarni 2 tadan chiqarish
# for son in range(2,15,2):
#      print(son)

#  10-22 juft sonlari
# for son in range(10,22, 2):
#      print(son)

# 1-10 gacha sonlarni chiqarish faqat 7 chiqmasin
# for son in range(1, 11, 1):
#      if son==7:
#           continue
#      print(son)

# 1-10 gacha sonlarni chiqarish faqat 7 va 9 chiqmasin
# for son in range(1, 11, 1):
#      if son==7 or son==9:
#           continue
#      print(son)

# 1-30 gacha sonlarni chiqarish faqat 18 dan 22 gacha bo'lganlari chiqmasin
# for i in range(1, 31):
#      if i>=18 and i<=22:
#           continue
#      print(i)

# 1-100 gacha sonlarni chiqarish faqat 0,1,2,3,4,5 bilan tugaydiganlari chiqmasin
# for i in range(1, 101):
#      if i%10<=5 and i//10>0:
#           continue
#      print(i)

# 84 bet 2 masala
# a=int(input("a="))
# b=int(input("b="))
# if a<b:
#     for i in range(a, b, 1):
#         print(i)
# else:
#         for i in range(a, b, -1):
#             print(i)

# # # 1 da 20 gacha bo\lgan sonlarni chiqarish
# qidirilayotgan_son=int(input("qidirayotgan soningizni kiriting:="))
# for i in range(1,20):
#     if qidirilayotgan_son==i:
#         print("bor")
#         break
#     else:
#         continue





