# B1

a = float(input())
b = float(input())
print("a =", a)
print("b =", b)
print("Nghiệm của pt là:", -b/a)

# B2

a = float(input())
b = float(input())
c = (-b/a)**(0.5)
print(c)

# # b3
n = int(input())
x = sum(int(z) for z in str(n))
print(f"Tổng các chữ số của số {n} là: {x}")

# # B4

n = int(input())
x = sum(int(z) for z in str(n))
print(x)

# B5
n = int(input())
s = n*(n+1)//2
print(s)

# B6
'''Đề sai rồi nhé ...'''
m = int(input())
n = int(input())

print(sum(2**i for i in range(m*n)))