# python_core
'''Bài 1: Viết chương nhập 2 số từ bàn phím. Tính và in ra giá trị tổng, tích, hiệu, thương của chúng (có kiểm tra điều kiện)'''

x = int(input())
y = int(input())


print("x + y ="+ str( x + y ))
print("x - y ="+ str( x - y ))
print("x * y ="+ str( x * y ))

if y==0 :
    print("Error")
else: print("x / y ="+ str( x / y ))

'''Bài 3: Viết chương trình nhận một chuỗi từ người dùng và hiển thị các ký tự có ở số chỉ mục chẵn.
Ví dụ: str = "pynative" thì bạn nên hiển thị ‘p’, ‘n’, ‘t’, ‘v’.'''
string_one = ' '
string_two = 'pynative'
print(string_one.join(string_two))

'''Bài 6: Viết chương trình in bảng nhân của một số cho trước
Ví dụ: num = 2 nên đầu ra phải là:
2
4
6
8
10
12
14
16
18
20
'''
n = 2
for i in range(1, 11, 1):
    list = n * i
    print(list)



'''Baif 8: Viết chương trình Hiển thị các số từ -10 đến -1 bằng vòng lặp for.'''
for num in range(-10, 0, 1):
    print(num)



