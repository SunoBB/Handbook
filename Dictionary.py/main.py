# B1
with open('HS.INP', 'r') as f:
    n = int(f.readline())
    d = []
    for i in range(n):
        d.append(list(map(str, f.readline().strip().split(" "))))

maxx = float(d[0][2])
indexx = 0
for i in range(n):
    if maxx < float(d[i][2]):
        maxx = float(d[i][2])
        indexx = i
print(f"Họ và tên: {d[indexx][0]}")
print(f"Ngày sinh: {d[indexx][1]}")
print(f"Điểm: {d[indexx][2]}")




# B2

f=open('hs.inp','r')
g = open('hs.out','w')
n=int(f.readline())
b={}
for i in range(n):
    a = [j for j in f.readline().split()]
    b[a[2]]=a[0]

ds = sorted(b.items())

for i in range(len(ds)):
    g.write(ds[i][1]+": "+ds[i][0]+"\n")

f.close()
g.close()

# B3
N = int(input())
S1, S2, S3, S4 = 0, 0, 0, 0

for i in range(N):
	A = list(map(int, input().split()))
	S1 += sum(A[:N-i])
	S2 += sum(A[i:])
	S3 += sum(A[:i+1])
	S4 += sum(A[N-i-1:])
	
print(str(S1)+ '\n' +str(S2)+ '\n' + str(S3)+ '\n' +str(S4))