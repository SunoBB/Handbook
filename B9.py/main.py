'''
B1:
a.

- Có tên gọi là Hàm hoặc thủ tục

- Có tham số truyền vào

- Mục đích của hàm là giúp ta thực hiện một tác vụ nào đó

'''

# b

def Hello(n):
    for i in range(1, n+1):
        print("Python xin chào các bạn")

Hello(5)
Hello(10)

# B2

def api(n):
    pi = 1
    a = 1
    for i in range(1, n):
        a += 2
        if i % 2 == 0:
            pi += 1 / a
        else:
            pi -= 1 / a
    return pi*4

print(api(123456))

# B3

def one():
    print('''
..#
.##
#.#
..#
..#
..#
''')

def three():
    print('''
###
..#
###
..#
###
''')

one()
three()

def _2021():
    print('''
####    ####    ####    ..#
#..#    #..#    #..#    #.#
..#.    #..#    ..#.    ..#
.#..    #..#    .#..    ..#
####    ####    ####    ..#
''')

def _2023():
    print('''
####    ####    ####    ###
#..#    #..#    #..#    ..#
..#.    #..#    ..#.    ###
.#..    #..#    .#..    ..#
####    ####    ####    ###
''')


# B4

def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua(n-1)
print(giai_thua(10))
print(giai_thua(20))