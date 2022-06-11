# B1

for counter in range(1, 11):
    print(counter, counter + counter)


# B2

maxx = 1e9
Day = 0
vrs = 1
while vrs <= maxx:
    vrs = vrs * 2
    Day += 1
print(Day)

# B3

T = float(input())
Lai = 0.07
VND = 0
for i in range(10):
    T = T + T * Lai
    print(T)
