# === Mo rong 1

# B1

n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

d = 0

for i in range(n):
    for j in range(n):
        d += a[i][j]

print(d)
m = a[0][0]

for i in range(n):
    for j in range(n):
        m = max(a[i][j], m)

print(m)


# B2

n = int(input())
n += 1
a = []
a.append([1])

for i in range(1, n):
    a.append([1])
    for j in range(1, i):
        a[i].append(a[i-1][j] + a[i-1][j-1])
    a[i].append(1)

for i in range(n):
    for j in range(i+1):
        print(a[i][j], end = " ")
    print()


# B3

n = int(input())
a = []

for i in range(list(map(int, input().split()))):
    a.append(list(map(int, input().split())))

d = 0
for i in range(n):
    d += a[i][i]
print(d)

for i in range(n):
    for j in range(i+1, n):
        d += a[i][j]
    
print(d)

m, n = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

maxd = a[1][1]
maxc = a[1][1]

for i in range(n):
    d = 0
    for j in range(m):
        d += a[i][j]
    maxd = max(maxd, d)
print(maxd)

for j in range(m):
    d = 0
    for i in range(n):
        d += a[i][j]
    maxc = max(maxc, d)
print(maxc)

# === Mo rong 2

with open('HS.INP', 'r') as f:
    n = int(f.readline())
    d = []
    for i in range(n):
        d.append(list(map(str, f.readline().strip().split(" "))))

maxx = int(d[0][2])
indexx = 0
for i, x in enumerate(d[0][3]):
    if x > int(maxx):
        indexx = i
        maxx = int(x)
print(x)
