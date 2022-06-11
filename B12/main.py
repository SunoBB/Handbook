# B1

bookList = ["Toán 10", "Lý 11", "Hóa 12", "Tin 10", "Tin 12"]
print(bookList)
print(len(bookList))
print(bookList[3])
print(bookList[3:5])
print("Tin 11" in bookList)
bookList.insert(4, "Tin 11")
print("Tin 11" in bookList)
bookList.sort()
print(bookList)


# B2

l = list(map(float, input().split()))

for i in l:
    if i < 10:
        print(i, end=" ")
print()

print(min(l))
print(max(l))

# B3

input()
l = list(map(int, input().split()))
l.sort()
print(l)


# 