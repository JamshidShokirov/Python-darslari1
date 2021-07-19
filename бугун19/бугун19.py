# class Mashina:
#     def __init__(self, rusumi, narxi, chiqqan_yili):
#         self.rusumi = rusumi
#         self.narxi = narxi
#         self.chiqqan_yili = chiqqan_yili
#
#     def haqida(self):
#         if self.narxi > 200000000:
#             print("men juda qimmat mashinaman!")
#         else:
#             print("meni bir amallab sotib olsa bo'ladi")
#
#
# x = Mashina("malibu", 320000000, 2021)
# print(x.__dict__)
# x.haqida()
#
# y = Mashina("Nexia", 97000000, 2021)
# print(y.__dict__)
# y.haqida()

# a=Son() #son klassli konstruktor
# # parametrli konstruktor
# #
# class Son1:
#     def __init__(self,x):
#         self.x=x
#
# b=Son1(7)
# print(b.x)

# parametrli

# class alfa:
#     def __init__(self,z):
#         self.z=z
#
# a=alfa(9)
# print(a.z)

# parametrsiz
# class beta:
#     x=8
#
#
# print(beta.x)

# class gap:
#     def __init__(self):
#         print("Parametr yuq")
#
# z=gap()
# print(gap.z)


"""sanagich o'rnattish yoki obyektlarni sanash"""
# class Student:
#     sanagich=0
#     def __init__(self):
#         Student.sanagich+=1
#
# s1=Student()
# s2=Student()
# Student()
# Student()
# print(Student.sanagich)

# ajdod klass
# class Nokia:
#     def __init__(self, markasi, gaplashish, sms, kamera):
#         self.markasi = markasi
#         self.gaplashish = gaplashish
#         self.sms = sms
#         self.kamera = kamera
#
#
# # voris olamiz:
# class Samsung(Nokia):
#     def yangilik(self, telegram, instagram, hdcamera):
#         self.telegram = telegram
#         self.instagram = instagram
#         self.hdcamera = hdcamera
#
#
# nokia6300 = Nokia('nokia6300', True, True, True)
# print(nokia6300.markasi)
#
#
# samsungJ2 = Samsung("samsungJ2", True, True, True)
#
# samsungJ2.yangilik("telegram bor", "istagram bor", "hd camera bor")
#
#
# print(nokia6300.__dict__)
# print(samsungJ2.__dict__)
#
#
# class SonAjdod:
#     def init(self, x):
#         self.x = x
#
#
# class SonVoris(SonAjdod):
#     pass
#
#
# x = SonVoris(5)
# y = SonAjdod(5)
#
# class TVAjdod:
#         def __init__(self, markasi, kursatish, kanal, ovoz):
#             self.markasi = markasi
#             self.kursatish = kursatish
#             self.kanal = kanal
#             self.ovoz = ovoz
#
#     # voris olamiz:
# class TV(TVAjdod):
#         def yangilik(self, Wi_FI, Youtube, Digital):
#             self. Wi_FI =  Wi_FI
#             self.Youtube = Youtube
#             self.Digital = Digital
#
# ETV = TVAjdod('ETV', True, True, True)
# print(ETV.markasi)
#
# Smart = TV("Smart", True, True, True)
#
# Smart.yangilik("Wi_FI bor", "Youtube bor", "Digital bor")
#
# print(ETV. __dict__)
# print(Smart. __dict__)

# class SonAjdod:
#     def init(self, x):
#         self.x = x
#
#
# class Son1Voris(SonAjdod):
#     pass
#
#
# class Son2Voris(SonAjdod):
#     pass
#
#
# class Son3Voris(SonAjdod):
#     pass
#
#
#
# x1 = Son1Voris(5)
# x2 = Son2Voris(5)
# x3 = Son3Voris(5)
# y = SonAjdod(5)

# xulosa. bitta klasdan xohlagan voris olsa bo'ladi

# ixtiyoriy class tuzib undan voris oling hamda isbotlash uchun ikkalsini ham
# xususiyatlarini chiqaring

""" bitta klass xohlagancha klasslarga voris bo'la oladi """

#
# class Ota:
#     def init(self, x):
#         self.x = x
#
#
# class Ona:
#     def init(self, y):
#         self.y = y
#
#
# class Bola(Ota, Ona):
#     pass
#
#
# bola = Bola(5)
#
# bola.x = 5
# bola.y = 1
#
# print(f"{bola.x} {bola.y}")


# class Bobo:
#     def init(self, x):
#         self.x = x
#
#
# class Ota(Bobo):
#     def init(self, y):
#         self.y = y
#
#
# class Nabira(Ota):
#     def init(self, z):
#         self.z = z
#
#
# bobo = Bobo(1)
# ota = Ota(2)
# bola = Nabira(3)

# """ init """
#
#
# class Ota:
#     def init(self, z):
#         self.z = z
#
#
# class Bola(Ota):
#     def init(self, z, x):
#         self.x = x
#         Ota.init(self, z)
#
#
# x = Bola(5, 1)
# print(x.z)

""" super() """
class Ota:
    def __init__(self, z):
        self.z = z

class Ona:
    def __init__(self, y):
        self.y = y


class Bola(Ota, Ona):
    def __init__(self, x):
        super().__init__(x)


bola = Bola(5)
print(bola.y)
print(bola.z)
