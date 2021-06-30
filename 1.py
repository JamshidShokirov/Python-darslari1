# a=int(input("a="))
# a=int(input("a="))
# P=2*(a+b)
# S=a*b
# print(f"P={P}, S={S}")

import math
a=3
b=4
c=5
P=(a+b+c)/2
S=math.sqrt(P*(P-a)*(P-b)*(P-c))
print(f"P={P}, S={S}")