# B1

n = input()
if n == n[::-1]:
    print("YES")
else:
    print("NO")


# B2

s = input().split()

for i in s:
    if i == "Covid-19":
        print("YES")
        exit()

print("NO")

# B3

print(len(input()))

# B4

money = int(input("So du tai khoan: "))
print(money // 300)

# =============//=========================//=========================//=========================


# B1

zero="""
###
#.#
#.#
#.#
###
"""

towo =''''
###
..#
.#.
#..
###'''

print(zero)
print(towo)
print(zero)
print(towo)

# B2

s = input()
print(s[::-1])

# B3

d = {'0' : 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for i in input():
    if i.isnumeric():
        d[i] += 1
for i in range(10):
    print(f"So chu so '{i}': {d[str(i)]}")

# B4

for i, ch in enumerate(input()):
    if ch == " ":
        print(i)
        break

# B5
count = 0
for i, ch in enumerate(input()):
    if ch == 'a':
        print(i, end = "\t")
        count += 1
print(count)

# B6

s = input().split()
print(len(s))
for i in s:
    print(i)

# B7

name = input()
print(name.upper())

# B8

s = input().strip()
print(" ".join(s.split()))


# B9

a = input()
b = input()

if a[::-1] == b:
    print("YES")
else:
    print("NO")

