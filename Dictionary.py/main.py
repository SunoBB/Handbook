f=open('hs.inp','r')
n=int(f.readline())
m=float(0)
for i in range(n):
    b={}
    a=[j for j in f.readline().split()]
    b["Họ và tên"]=a[0]
    b["Ngày sinh"]=a[1]
    b["Điểm trung bình"]=a[2]
    if float(b["Điểm trung bình"])>=m:
        m=float(b["Điểm trung bình"])
        b1 = b.copy()

for i in b1:
    print(i,": ",b1[i])

f.close()



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

