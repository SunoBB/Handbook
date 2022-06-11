# B1

pi = 1
a = 1
for i in range(1, 1000000):
    a += 2
    if i % 2 == 0:
        pi += 1 / a
    else:
        pi -= 1 / a
print(pi*4)

# B2


from math import factorial
n = int(input())
e = 1

for i in range(1, n+1):
    e += 1/(factorial(i))

print(e)

# B3

n = int(input("Nhap n = "))
l = []

print("n = ", n)
for i in range(1, int(n**0.5)+1):
    if n % i == 0:
        l.append(i)
        if n//i not in l:
            l.append(n//i)
l.sort()

for i in l:
    print(f"chia lam {i}, moi phan co {n//i}")


# ===============//=====================//=====================//=====================

# B1

for i in range(1, 101, 2):
    print(i, end= " ")

# B2

for i in range(1, 11):
    for j in range(i, 101, 10):
        print(j, end="\t")
    print()

# B3

for i in range(100, 0, -10):
    for j in range(i, i-10, -1):
        print(j, end="\t")
    print()


