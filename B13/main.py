f = open("MULTI_FILE.INP", "r")
g = open("MULTI_FILE.OUT", "w")

s = f.read()
p, q, r = map(int, s.split())

if r*p == q*r:
    g.write("YES")
else:
    g.write("NO")

f.close()
g.close()

# B3

f = open("FPRIME.INP", "r")
g = open("FPRIME.OUT", "w")
N = int(f.read())

i = 2

while N > 1:
    while N % i == 0:
        g.write(str(i) + " ")
        N /= i
    i += 1

f.close()
g.close()

# B4

f = open("GCDSEQ.INP", "r")
g = open("GCDSEQ.OUT", "w")

N = int(f.read())
a = [int(x) for x in f.readline().split()]

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

res = a[0]
for i in a:
    res = gcd(res, i)

g.write(str(res))

f.close()
g.close()

# B5


f = open("MIXED.INP", "r")
g = open("MIXED.OUT", "w")

N = int(f.readline())
a = [int(x) for x in f.readline().split()]

cur = res = right = 1

for i in range(1, N):
    if a[i] * a[i-1] < 0:
        cur += 1
        if cur > res:
            res = cur
            right = 1
    else:
        cur = 1
g.write(str(res) + "\n")
for i in range(right - res, right + 1):
    g.write(str(a[i]) + " ")

f.close()
g.close()

# B6

f = open("3SEQ.INP", "r")
g = open("3SEQ.OUT", "w")

N = int(f.readline())
a = [int(x) for x in f.readline().split()]
b = [int(x) for x in f.readline().split()]
c = [int(x) for x in f.readline().split()]

res = 0

for i in range(0, N):
    tong = a[i] + b[i] + c[i]
    if tong > res:
        res = tong

f.write(str(res))

f.close()
g.close()

