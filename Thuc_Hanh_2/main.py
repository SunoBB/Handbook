# B1

a, b, c, d = map(int, input().split())

if a <= c <= b or a <= d <= b:
    print("Khong co diem chung")
else:
    print("Co diem chung")


# B2

a, b = map(int, input().split())
if a > b:
    print(a)
else:
    print(b)

# B3

a, b, c = map(int, input().split())
print(max(a, b, c))

# B4

p, q, r = map(int, input().split())
if q // p == r // q:
    print("YES")
else:
    print("NO")

# B5

m, n, k = map(int, input().split())
if len(str(m*n*k)) > 2 and str(m*n*k)[-1] == '0':
    print("YES")
else:
    print("NO")


# B6

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("366")
else:
    print("365")


# B7

month, year = map(int, input().split())

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("31")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30")
elif month == 2:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("29")
    else:
        print("28")

# B8

s = input()
if s.isalpha():
    print("YES")
else:
    print("NO")

# B9


a, b, c = map(int, input().split())
if a == b or a == c or b == c:
    print("Can")
elif a == b == c:
    print("Deu")
elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
    print("Vuong")
else:
    print("Thuong")


