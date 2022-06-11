# B1

s = input()
print(len(s))
print(sum(map(int, list(s))))


# B2

def Fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


n = int(input())
print(Fibonacci(n))


# B3

def pt_so(n):
    i = 2
    nums = []
    while n > 1:
        if not n % i:
            n = n//i
            nums.append(i)
        else:
            i += 1
    if not(nums):
        nums.append(n)
    return nums

n = int(input())
print(*pt_so(n))


# B4


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if is_prime(int(input())):
    print("YES")
else:
    print("NO")

# B5
# ==== Cách 1 =====

n = int(input())
i = 2
while i <= n:
    if is_prime(i):
        print(i, end = "\t")
    i += 1

# ==== Cách 2 =====
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


# B6

a,b = map(int, input().split())
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(a,b))
print((a*b)//gcd(a,b))

# B7

def giai_thua(n):
    if n == 0:
        return 1
    return n*giai_thua(n-1)

print(giai_thua(int(input())))

# B8

a, n = map(int, input().split())
print(a**n)

# B9

s = input()
if s == s[::-1]:
    print("YES")
else:
    print("NO")

# B10

# convert positive integers to binary
def to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return to_binary(n//2) + str(n%2)

print(to_binary(int(input())))

# B11
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i)+"*"*(2*i-1))