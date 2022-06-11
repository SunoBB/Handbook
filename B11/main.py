# B1

print("123"*3)
print(int("123")*3)

# B2

n = int(input())

print("*"*n)
print("*"+ "-" * (n-2) + "*")
print("*"*2)


# B3

n = input()
for i in n:
    print(i)

# B4

s = input().split(".")
if s[1].lower() == "py":
    print("YES")
else:
    print("NO")


# B5
n = input()
print(len(n)*300)