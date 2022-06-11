# B1

A = 5
B = 10

print("A < B:", A < B)
print("A+5 <= B:", A + 5 <= B)
print("A*A +B*B <= 200", A*A + B*B <= 200)
print("3*A > B", 3*A > B)
print("2*A == B", 2*A == B)
print("A+5 != B", A + 5 != B)

# B2

A = 5
B = 10

print("(A < B) and (A+B > 20):", (A < B) and (A+B > 20))
print("(A+5 <= B) or (3*A > B):", (A + 5 <= B) or (3*A > B))
print("(A*A+B*B <= 200):", A*A + B*B <= 200)
print("(A+5 != B) or (A*2 == 10):", (A + 5 != B) or (A*2 == 10))

# B3

a = int(input("a = "))
print("Giá trị tuyệt đối bằng", abs(a))

# B4

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a > 0 and b > 0 and c > 0:
    print("Ca 3 so deu duong")

# B5

n = int(input())
m = int(input())

if n % m == 0:
    print("YES")
else:
    print("NO")

# B4_p2

a, b, c = float(input("a = ")), float(input("b = ")), float(input("c = "))
if a + b > c and a + c > b and b + c > a:
    print("YES")
else:
    print("NO")