# =======//=========//======Đệ Quy====//=========//=========





# B1

f = open("dequy1.inp", "r")
g = open("dequy1.out", "w")

m, n = map(int, f.readline().split())
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

g.write(str(gcd(m, n)))
f.close()
g.close()

# B2

f = open("dequy2.inp", "r")
g = open("dequy2.out", "w")

n = int(f.readline())

def nhiphan(n):
    if n > 1: 
        nhiphan(n//2)
    g.write(str(n%2))

nhiphan(n)
f.close()
g.close()

# B3

f = open("dequy3.inp", "r")
g = open("dequy3.out", "w")

x, n = map(int, f.readline().split())

def power(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(x, n//2) * power(x, n//2)
    else:
        return x * power(x, n//2) * power(x, n//2)

g.write(str(power(x, n)))
f.close()
g.close()

# B4

f = open("dequy4.inp", "r")
g = open("dequy4.out", "w")

n = int(f.readline())

def nhanchia(n):
    if n == 1:
        g.write("1")
    elif n % 2 == 0:
        nhanchia(n//2)
        g.write("x2")
    else:
        nhanchia(n*3+1)
        g.write("//3")

nhanchia(n)
f.close()
g.close()


# B5

f = open("dequy5.inp", "r")
g = open("dequy5.out", "w")

n = int(f.readline())

def tong(n):
    if n == 1:
        return 1
    else:
        return tong(n-1) + n

g.write(str(tong(n)))
f.close()
g.close()

# ===========//=========//======Sắp xếp====//=========//=========

# B1

f = open('book.inp', 'r')
g = open('book.out', 'w')
kq = 0
n = int(f.readline())
a = []

for i in range(n):
    a.append(int(f.readline()))
a.sort()
a.reverse()

for i in range(n):
    if i % 3 != 2:
        kq += a[i]

g.write(str(kq))
f.close()
g.close()

# B2

f = open("coffee.inp", "r")
g = open("coffee.out", "w")
n = int(f.readline())
a = []

for i in range(n):
    x, y = map(int, f.readline().split())
    a.append(x*60+y)

a.sort()
maxx = cnt = 1

for i in range(n-1):
    if a[i] == a[i+1]:
        cnt += 1
        maxx = max(maxx, cnt)
    else:
        cnt = 1

g.write(str(maxx))
f.close()
g.close()

# B3


n = int(input())
a = [int(i) for i in input().split()]
def qs(l, r):
    x = a[(l+r)//2]
    i = l
    j = r
    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            if i != j & a[i] != a[j]:
                print(i+1, j + 1)
                i += 1
                j -= 1
    if l < j:
        qs(l, j)
    if i < r:
        qs(i, r)
qs(0, n-1)

#  =======//=========//======Tìm Kiếm====//=========//=========

# B1

f = open('qd.inp', 'r')
g = open('qd.out', 'w')
n = int(f.readline())
s = f.readline()
w = list(map(int, s.split()))

def bs(x):
    dau = 0
    cuoi = m -1
    while dau <= cuoi:
        giua = (dau + cuoi) // 2
        if a[giua] == x:
            return True
        if a[giua] < x:
            dau = giua + 1
        else:
            cuoi = giua - 1
        return False

w.sort()
a = []
for i in range(n):
    if w[i] != w[i-1]:
        a.append(w[i])
m = len(a)
kq = 0
for i in range(m):
    for j in range(i+1, m):
        if bs(a[i] + a[j]):
            kq += 2
ss = str(kq)
g.write(ss)
f.close()
g.close()

