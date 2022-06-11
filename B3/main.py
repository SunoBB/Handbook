# Test

# B1

# a
A = 123
B = 5
C = A*B
print(C)

# b
print("Phép cộng:", A+B)
print("Phép trừ:", A-B)
print("Phép nhân:", A*B)
print("Phép chia:", A/B)
print("Phép chia lấy thương:", A//B)
print("Phép chia lấy dư:", A%B)
print("Phép lũy thừa:", A**B)


# B2
# a

A = 1
B = 2
C = -3
# Delta
D = B**2 - 4*A*C
x1 = (-B + D**0.5)/(2*A)
x2 = (-B - D**0.5)/(2*A)
print(x1)
print(x2)

# b

A = 2
B = 2
C = -4
D = B**2 - 4*A*C
x1 = (-B + D**0.5)/(2*A)
x2 = (-B - D**0.5)/(2*A)
print(x1)
print(x2)

# B3

a = 2
n = 100
p = 2**100
print(p)

# B4

pi = 3,14
r = float(input("Nhap r: "))
print("Dien tich hinh tron:", pi*r**2)

# B5
a, b = map(int, input().split())
c = (a*a + b*b)**(0.5)
print(c)

