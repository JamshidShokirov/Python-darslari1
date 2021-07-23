# class Son:
#     x = 1
#     y = 2
#
#
# son1 = Son()   # son1 -> bu obyekt, Son() -> klass
# print(son1.y, son1.x)
# son2 = Son()
# print(son2.x, son2.y)
#
# # xulosa. Bitta klassdan hohlagancha obyekt olish mumkin
#
# """ def __init__() funksiyasi: """
#
#
# class Son:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# son3 = Son(4, 5)
# print(son3.x, son3.y)
# son4 = Son(6, 7)
# print(son4.x, son4.y)

# class Avtomobil:
#     def __init__(self, rusumi, yili, rangi, firmasi):
#         self.rusumi = rusumi,
#         self.yili = yili,
#         self.rangi = rangi,
#         self.firmasi = firmasi
#
#
# malibu = Avtomobil("Malibu", 2022, "qora", "Chevrolet")
# lacetti = Avtomobil("lacetti", 2020, "oq", "Chevrolet")
#
# print(malibu.rusumi, malibu.rangi)

# class Xodim:
#     def __init__(self, ismi, kasbi, toifasi, staji):
#         self.ismi = ismi,
#         self.kasbi = kasbi,
#         self.toifasi = toifasi,
#         self.staji = staji
#
#
# uqituvchi = Xodim("Alijon", "Uqituvchi", "oliy", "20 yil")
#
# print(uqituvchi.ismi, uqituvchi.kasbi)
#
# quruvchi = Xodim("Alijon", "Quruvchi", "oliy", "20 yil")
#
# print(quruvchi.ismi,quruvchi.kasbi)
# print(quruvchi.__dict__)

# """ xususiyatni o'chirish"""
#
# class Son:
#     def __init__(self, x, y):
#         self.x=x
#         self.y = y
#
# son1=Son(1,2)
# son1.x=3
# print(son1.__dict__)
#
# del son1.x  # son1.x ni uchirish
# print(son1.__dict__)
#
# # # #  obyektni o'zini o'chirish
# # del son1
# # print(Son)

""" classda metodlar"""

# class Avtomobil:
#     def __init__(self, rusumi):
#         self.rusumi=rusumi
#     def signal(self):
#         print("Biiib!!!")
#
# malibu=Avtomobil("Malibu")
# malibu.signal()



# class Shaxs:
#     def __init__(self, ism, fam):
#         self.ism=ism
#         self.fam = fam
#
#     def tuliq_ism(self):
#         return self.ism+self.fam
#
# sh1=Shaxs("Alijon", " Valiyev")
# print(sh1.tuliq_ism())

# class Shaxs:
#     def __init__(self, ism, fam, shahri, mahallasi):
#         self.ism=ism
#         self.fam = fam
#         self.shahri = shahri
#         self.mahallasi = mahallasi
#
#     def tuliq_ism(self):
#         return self.ism+self.fam
#
#     def tuliq_manzil(self):
#         return self.shahri + self.mahallasi
# sh1=Shaxs("Alijon", " Valiyev", "Jizzax shahri", " Hamza mahallasi")
# print(sh1.tuliq_ism())
# print(sh1.tuliq_manzil())

# 1-masala. Xodim degan class yaratasi unda 5 ta obyekt olasiz
# Xodim class ida ->ismi, manzili, maoshi
# maoshi 2mlndan kamlarini ismini chiqarasiz

# class Xodim:
#     def __init__(self, ism, manzili, maoshi):
#         self.ism=ism
#         self.manzili = manzili
#         self.maoshi = maoshi
#
#
#     def tuliq_malumot(self):
#         return self.ism+self.manzili+ self.maoshi
#
#     def tuliq_manzil(self):
#         return self.shahri + self.mahallasi
# xodimlar=[]
# x1=Xodim("Alijon", " Jizzax shahri", 1800000)
# xodimlar.append(x1)
# x2=Xodim("Solijon", " Jizzax shahri", 3000000)
# xodimlar.append(x2)
# x3=Xodim("Xolijon", " Jizzax shahri", 4000000)
# xodimlar.append(x3)
# x4=Xodim("Valijon", " Jizzax shahri", 1900000)
# xodimlar.append(x4)
#
# for Xodim in xodimlar:
#     if Xodim.maoshi<2000000:
#         print(Xodim.ism)


# 1-masala. Xodim degan class yaratasi unda 5 ta obyekt olasiz
# Xodim class ida ->ismi, manzili, maoshi
# maoshi 2mlndan kamlarini ismini chiqarasiz

# class Xodim:
#     def __init__(self, ismi, manzili, maoshi):
#         self.ismi = ismi
#         self.manzili = manzili
#         self.maoshi = maoshi
#
#     def gap(self):
#         print(f"Mening ismi {self.ismi}; maoshim {self.maoshi}")
#
#
# xodimlar = []
# x1 = Xodim("Bunyod", "Lalmikor", 4000000)
# xodimlar.append(x1)
# x2 = Xodim("Sunnat", "Lalmikor", 400000)
# xodimlar.append(x2)
# x3 = Xodim("Doston", "Lalmikor", 3000000)
# xodimlar.append(x3)
# x4 = Xodim("Ilyos", "Lalmikor", 1500000)
# xodimlar.append(x4)
# x5 = Xodim("Shoxzod", "Lalmikor", 9000000)
# xodimlar.append(x5)
#
# for xodim in xodimlar:
#     xodim.gap()


# 1. dastlab xodimlar sonini kiriting.
# 2. Har bir xodim ma'lumotlarini input qilib obekt yarating
# 3 gap() metodida agar oyligi 1mln dan kam bulsa
# "mening oyligim kam degan yozuv ham chiqsin"
# 4.barcha xodim ma'lumotlarini gap metodi orqali konsolga chiqaring

class Xodim:
    def __init__(self, ismi, manzili, maoshi):
        self.ismi = ismi
        self.manzili = manzili
        self.maoshi = maoshi

    def gap(self):
        print(f"Mening ismim {self.ismi}; maoshim {self.maoshi}")
        if self.maoshi<1000000:
            print("Maoshim kam")

xodimlar = []
n = int(input("n="))
for i in range(n):
    print(f"{i+1}")
    ism=input("ismi: ")
    manzili = input("manzili: ")
    maoshi = int(input("maoshi: "))
    xodimlar.append(Xodim(ismi=ism, manzili=manzili, maoshi=maoshi))

for xodim in xodimlar:
    xodim.gap()

    # uquvchilar = []
    #
    # n = int(input("O'quvchilar sonini kiriting: "))
    # for i in range(n):
    #     uquvchilar.append(input(f"{i + 1}) ismi:"))
    #
    # for i in uquvchilar:
    #     print(i)