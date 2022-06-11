# B1

A = float(input("A = "))
B = float(input("B = "))
C = float(input("C = "))

delta = B**2 - 4*A*C
if delta < 0:
    print("Vo nghiem")
elif delta == 0:
    print("Nghiem kep:", -B/(2*A))
else:
    print("PT 2 nghiem phan biet")
    print("Nghiem 1:", (-B + delta**0.5)/(2*A))
    print("Nghiem 2:", (-B - delta**0.5)/(2*A))

# B2

n = int(input())
if n <= 100:
    print("Ban da nhap dung")
else:
    print("Ban da nhap vao so qua lon")

# B3

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if not ((a > 0) and (b >0) and (c > 0) and (a + b > c) and (a + c > b) and (b + c > a)):
    print("Khong phao la ba canh cua tam giac")
elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
    print("Tam giac vuong")
else:
    print("La 3 canh cua mot tam giac")


# B4

def f(x, y):
    if x > y:
        return x*x
    elif x == y:
        return x + y
    return y*y
x = int(input())
y = int(input())

# B5

n = int(input())
if n % 2 == 0:
    print("So nhap vao la mot so chan")
else:
    print("So nhap vao la mot so le")

# B6

score = float(input())

if score >= 8:
    print("Gioi")
elif score >= 6.5:
    print("Kha")
elif score >= 5:
    print("Trung binh")
else:
    print("Yeu")


# B7

Kw = int(input())

if Kw > 400:
    print(Kw*2.927)
elif Kw > 300:
    print(Kw*2.834)
elif Kw > 200:
    print(Kw*2.536)
elif Kw > 100:
    print(Kw*2.014)
elif Kw > 50:
    print(Kw*1.734)
else:
    print(Kw*1.678)

