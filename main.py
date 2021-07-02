# ruyxat list almashtirish
# mashinalar=["Nexia", 'Lacetti', "Malibu"]
# mashinalar[0]="Cobalt"
# print(mashinalar)

# ruyxat list uzunligi
# mashinalar=["Nexia", 'Lacetti', "Malibu"]
# print(len(mashinalar))

# # ruyxat list qo'shish ->append  ro'yxat oxiriga element qo'shadi
# mashinalar=["Nexia", 'Lacetti', "Malibu"]
# mashinalar.append("Damas")
# print(mashinalar)

"""Ro'yxatni tozalash-> hamma elementlarni o'chirish"""
# sonlar=[1, 2, 3, 4]
# sonlar.clear()
# print(sonlar)

"""Bir ro'yxatni boshqasiga nusxalash copy() metodi"""
# sonlar=[1, 2, 3, 4]
# sonlar1=sonlar.copy()
# print(sonlar1)

"""Rro'yxatda bir xil elementlarni sanash->count() metodi"""
# sonlar=[1, 2, 3, 4, 4, 0, 5, 4]
# print(sonlar.count(4))

"""Rro'yxatga qo'shish->extend() metodi"""
# sonlar=[1, 2, 3, 4, 4, 0, 5, 4]
# sonlar1=[7, 8, 9]
# sonlar.extend(sonlar1)
# print(sonlar)

"""index->ruyxatdagi element indeksini qaytaradi"""
# sonlar=[1, 2, 3, "Salom", True, [1, 2.4]]
# print(sonlar.index((3)))

# """insert -> bu elementni hohlagan ruyxat indeksiga kiritish"""
# sonlar=[9, 8, 2]
# sonlar.insert(2,5)
# print(sonlar)

# # 1 - masala.
# # 1. o'quvchilar ro'yhatini e'lon qiling unga oxiriga yangi o'quvchi qo'shing (print qiling) append
# # 2. keyin o'rtasiga yangi o'quvchi qo'shing (print qiling) insert
# # 3. o'quvchilar sonini toping (print qiling) len
# # 4. o'quvchilar ro'yhatiga yana bor ismlardan birini kiriting
# #    va shu ismli o'quvchi nechtaligini toping (print qiling) append yoki insert , count
# # 5. yangi o'quvchilar ro'yhatini e'lon qilib eski ro'yhatga ulang
# #    va eski ro'yhatni (print qiling) extend
# # 6. ixtiyoriy o'quvchini indeksini topib bering (print qiling) index
# # 7. ro'yhatni tozalang (print qiling) clear

# Uquvchi=["Ali", "Vali", "Soli", "Xoli"]
# Uquvchi1=["Salim", "Karim", "Olim", "Xoli"]
# Uquvchi.append("G`ani")
# print(Uquvchi)
# print(len(Uquvchi))
# Uquvchi.insert(4,"Ali")
# print(Uquvchi)
# print(Uquvchi.count("Ali"))
# Uquvchi.extend(Uquvchi1)
# print(Uquvchi)
# Uquvchi.clear()
# print(Uquvchi)

# sonlar=[1, 2, 3, 4, 5, 6, 7]
# element=int(input("yangi element->"))
# element=int(input("yangi element joylashadigan indeks->"))
# a=str(sonlar)
# a=

"""pop -> berilgan indeksdagi elementni o'chirish"""
# sonlar=[9, 8, 2]
# sonlar.pop(1)
# print(sonlar)

"""remove -> berilgan indeksdagi elementni o'chirish"""
# mashinalar=["Nexia", 'Lacetti', "Malibu", 'Lacetti']
# for i in range(mashinalar.count('Lacetti')):
#     mashinalar.remove('Lacetti')
# print(mashinalar)

# 2 masala butun sonlardan iborat ruyxat berilgan  juftlarini chiqaring
# 2 masala butun sonlardan iborat ruyxat berilgan Oldin juftlarini keyin toqlarini ekranga chiqarib
# yangi ruyxatga o'zlashtirib konsolga chiqaring

# sonlar=[1, 2, 3, 4, 5, 6, 7]
#
# for son in sonlar:
#     if son%2==0:
#         print(son)

 # 2 masala butun sonlardan iborat ruyxat berilgan  juftlarini chiqaring
# 2 masala butun sonlardan iborat ruyxat berilgan Oldin juftlarini keyin toqlarini ekranga chiqarib
# yangi ruyxatga o'zlashtirib konsolga chiqaring

# sonlar=[1, 2, 3, 4, 5, 6, 7]
# sonlar1=[]
# for son in sonlar:
#     if son%2==0:
#         sonlar1.append(son)
#
#         print(son*2)
#     else:
#         sonlar1.append(son)
#         print(son**2)

# 5-masala Fibonachi sonlarini chiqarish
#
# index=int(input("=>"))
# a=[]
# for i in range(index+1):
#     if i==0 or i==1:
#         a.append(1)
#     else:
#         a.append(a[i-1]+a[i-2])
#
# print(a)

# sonlar=[1, 2, 3, 4, 5, 6, 7]
# sonlar1=[]
# for son in sonlar:
#     if son%2==0:
#         sonlar1.append(son)
#         son.revers()
#         print(son*2)
#     else:
#         sonlar1.append(son)
#         print(son**2)

# 6-masala Ro'yxat berilgan. Har bir elementini o'zidan keyingi elementiga almashtiring.
# oxirgi elementni nolga tenglang.
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(a)):
    if i==len(a)-1:
        a[i]=0
    else:
        a[i]=a[i+1]
print(a)