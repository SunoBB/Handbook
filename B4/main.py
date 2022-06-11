# B1

a = int(input())
b = int(input())
cv = (a+b)*2
dt = a*b
print(cv)
print(dt)

# B2

def f(x):
    return x**10 + x**5 + 1
x = int(input())
print(f(x))

# B3

def summ(a, b):
    return a**3 + b**3 + a*b
a = int(input())
b = int(input())
print(summ(a, b))

# B4
g = 9,8
h = float(input())

v = (2*h*g)**(0.5)
print(v)

# B5

x = int(input())
y = int(input())
# calculate distance from origin to A(x, y)
D = (x**2 + y**2)**(0.5)
print(D)

# B6
a = int(input())
b = int(input())
c = int(input())
p = (a+b+c)/2
S = (p*(p-a)*(p-b)*(p-c))**(0.5)
print(S)