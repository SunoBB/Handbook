# B1

A = 3
B = 4
C = 5

def Area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

    print("Biến toàn cục A, B, C:", A, B, C)
    print("Tham số a, b, c:", a, b, c)
    print("Biến cục bộ p, s:", p, s)

print(Area(5, 5, 8))


# B2

xa, ya, xb, yb = map(float, input().split())

def AB(xa, ya, xb, yb):
    return ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
print(AB(xa, ya, xb, yb))

# B3

a = int(input())
def drawBox(a):
    print("*" * 10)
    for i in range(a - 2):
        print("*" + " " * (10 - 2) + "*")
    print("*" * 10)

drawBox(a)

# B4

Ax, Ay = map(float, input().split())
Bx, By = map(float, input().split())
Cx, Cy = map(float, input().split())
Dx, Dy = map(float, input().split())

AB = ((Bx - Ax) ** 2 + (By - Ay) ** 2) ** 0.5
BC = ((Cx - Bx) ** 2 + (Cy - By) ** 2) ** 0.5
CD = ((Dx - Cx) ** 2 + (Dy - Cy) ** 2) ** 0.5
AD = ((Dx - Ax) ** 2 + (Dy - Ay) ** 2) ** 0.5
AC = ((Cx - Ax) ** 2 + (Cy - Ay) ** 2) ** 0.5

def area(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(area(AB, BC, AC) + area(CD, AD, AC))


