# B1

l = list(map(int, input().split()))

print("Tổng:", sum(l))
tbc = sum(l) / len(l)
print("Trung bình cộng:", tbc)
check = []
for i in l:
    if i > tbc:
        check.append(i)
print("Các tháng nhiều hơn trung bình cộng:", *check)


# B2

countryList =[
    ["Hoa Kỳ", 9525067],
    ["Nga", 17098246],
    ["Việt Nam", 331212],
]

print(countryList[2])
countryList.insert(2, ["Singapore", 752.7])
print(countryList)

for i in range(len(countryList)):
    print(countryList[i][0])

countryList.append(["Trung Quốc", 9596961])
countryList.append(["Nhật Bản", 377975])
countryList.append(["Ý", 301340])

for x, y in countryList:
    if y > 1_000_000:
        print(x)


