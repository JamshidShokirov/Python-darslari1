# numbers=(10, 2, 3, 4, 5, 6)
# print(any(numbers))
# print(max(numbers))
# print(min(numbers))
# print(len(numbers))
# print("sorted:")
# print(sorted(numbers))
# print("sum:")
# print(sum(numbers))

# n=(10, 4, 3, 8, 5, 6)
# print("kortejni max", max(n))
# print("kortejni min", min(n))
# print(max(n)+min(n))

# n=(10, 4, 3, 8, 5, 6)
# print("kortejni sum", sum(n))
# print("kortejni len", len(n))
# print(sum(n)/len(n))

# 2-usul
# n=(10, 4, 3, 8, 5, 6)
# urta_arifmetik=sum(n)/len(n)
# print(urta_arifmetik)

# 3-usul
# n=(10, 4, 3, 8, 5, 6)
# i=0
# Summa=0
# for number in n:
#     i+=1
#     Summa+=number
#     urta_arifmetik=Summa/i
# print(urta_arifmetik)
#
#
# a=(1, 4, 10, 6, 7)
# print(a[0::2])
# print(a[1::2])

# 4-masala avval juft o'rindagilarini keyin toq o'rindagilarini chiqarish
# a=(1, 4, 10, 6, 7)
# juft=[]
# toq=[]
# for i in range(len(a)):
#     if (i+1)%2==0:
#         juft.append(a[i])
#     else:
#         toq.append(a[i])
# print(juft)
# print(toq)

# 5-masala kortejni toq indeksli elementlarini kvadratini chiqaruvchi dastur tuzing
# a = (1, 2, 3, 4, 5, 6)  # (1, 6, 2, 5, 3, 4) bu faqat juft sonli uchun
# b = list(a)
# c = []
# for i in range(len(b)):
#     c.append(b[0])
#     c.append(b[-1])
#     b.pop(0)
#     b.pop(-1)
#     if not b:
#         break
# a = tuple(c)
# print(a)

# maxsus masala 2

# a = (1, 2, 3, 4, 5, 6, 7, 8)
# b = list(a)
# c = []
# for i in range(len(b)):
#     c.append(b[0])
#     if b[0] == b[-1]:
#         break
#     c.append(b[-1])
#     b.pop(0)
#     b.pop(-1)
#     if not b:
#         break
# a = tuple(c)
# print(a)

# Maxsus masala
a=(1,2,3,4,5,6,8)
b=list(a)
mk=[]
k=len(b)-1
for i in range(len(b)//2):
    mk.append(b[i])
    mk.append(b[k])
    k-=1
print(mk)


