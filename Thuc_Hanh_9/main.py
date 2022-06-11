# B1

a = open("DISTANCE.INP", "r")
b = open("DISTANCE.OUT", "w")

n = int(a.readline())
n = int(n)

x = []
y = []
f = []
ff = []

for i in range(0, n):
    x.append(0)
    y.append(0)
    f.append(0)
    ff.append(0)
    s = a.readline()
    x[i], y[i] = map(int, s.split())
    f[i] = x[i] + y[i]
    ff = x[i] - y[i]

f.sort()
ff.sort()

kq = max(abs(f[n-1] - f[0]), abs(ff[n-1] - ff[0]))

b.write(str(kq))
a.close()
b.close()

# B2

a = open("SUMX.INP", "r")
b = open("SUMX.OUT", "w")

n = int(a.readline())
inp = a.readline()

s = [inp(x) for x in inp.split()]

x = int(a.readline())
dem = 0
k = []

for i in range(1000000):
    k.append(0)

for i in s:
    k[i] += 1
for i in s:
    dem += k[x - i]

b.write(str(dem/2))
a.close()
b.close()

# B3

a = open('index.inp', 'r')
b = open('index.out', 'w')
n = int(a.readline())
inp = a.readline()
s = [inp(x) for x in inp.split()]
for i in range(len(s)):
    if s[i] % 2 == 0:
        b.write(str(i+1) + ' ')
a.close()
b.close()

