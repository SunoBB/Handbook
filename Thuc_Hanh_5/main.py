def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


n = int(input())
l = list(map(int, input().split()))
maxx = gcd(l[0], l[1])

for i in range(2, n-1):
    maxx = gcd(maxx, l[i])
print(maxx)


# B2

n = int(input())
check = [0]*(n+1)
for i in range(2, n+1):
    check[i] = True

for i in range(1, n+1):
    if check[i] == True:
        for j in range(2*i, n+1, i):
            check[j] = False

for i in range(2, n+1):
    if check[i] == True:
        print(i, end = "\t")


# B3

n = 1000
l = []
check = [False]*(n+1)
for i in range(2, n+1):
    check[i] = True

for i in range(2, n+1):
    if check[i] == True:
        for j in range(2*i, n+1, i):
            check[j] = False

for i in range(2, n+1):
    if check[i] == True:
        l.append(i)

for i in range(1000-1):
    if l[i+1] - l[i] == 2:
        print(l[i], l[i+1])

# B4



n = int(input())
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(1, n+1):
    if is_prime(i):
        if is_prime(n-i):
            print(i, n-i)