# B1
from turtle import right


n = int(input())

def main():
    a = [0] * (n+1)
    a[0] = 0
    a[1] = 1
    a[2] = 1
    for i in range(3, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]

print(main())


# B2

n = int(input())
l = list(map(int, input().split()))

# a.
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

count = 0
for i in l:
    if is_prime(i) == True:
        count += 1
print(f"- Số lượng số nguyên tố: {count}")

# b.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

bd = gcd(l[0], l[1])
for i in range(2, len(l)):
    bd = gcd(bd, l[i])
print(f"- UCLL: {bd}")


# B3

n = int(input())

def to_binary(n):
    if n == 0:
        return "0"
    s = ""
    while n != 0:
        s = str(n % 2) + s
        n = n // 2
    return s

# B4

n, x = map(int, input().split())
l = list(map(int, input().split()))

l.pop(x)
print(*l)

# B6

n, x, k = map(int, input().split())
l = list(map(int, input().split()))

l.insert(x, k)
print(*l)

# B7

input()
l = list(map(int, input().split()))
l.sort()
print(*l)


# B8

n = int(input())
l = list(map(int, input().split()))

sign = [1 if i > 0 else -1 for i in l]
max = 0
start_max = 0
start = 0
count = 1
for i in range(n-1):
    if sign[i] != sign[i+1]:
        count += 1
    else:
        if count > max:
            max = count
            start_max = start
        count = 1
        start = i + 1
if count > max:
    max = count
    start_max = start
print(max)
print(l[start_max : start_max + max])

# B9


n = int(input())
result = []
def fibonacci():
    a, b = 0, 1
    l = []
    while a < n:
        a, b = b, a + b
        l.append(a)
    return l

l = fibonacci()
l = l[::-1][n == l[-1]:]
while True:
    if n == 0:
        break
    for i in l:
        if n >= i:
            result.append(i)
            n -= i
result.sort()
print(*result)