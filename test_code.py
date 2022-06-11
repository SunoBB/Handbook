with open('HS.INP', 'r') as f:
    n = int(f.readline())
    d = []
    for i in range(n):
        d.append(list(map(str, f.readline().strip().split(" "))))
print(d)
maxx = float(d[0][2])
print(maxx)
indexx = 0
for i in range(n):
    

