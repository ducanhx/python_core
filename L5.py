'''Bài 1. Định nghĩa hàm nhận vào 2 giá trị và trả về tổng, phép chia, phép trừ và phép nhân (sử dụng ngoại lệ cho phép chia).'''

def calc_area_circm(a,b): 
    return a + b, a - b, a * b, a / b
 
a = int(input(" First number: "))
b = int(input(" Second number: ")) 
if b != 0:
    add, difference, product, quotient = calc_area_circm(a, b) 
    print('Add =',add)     
    print('Difference=',difference)
    print('Product =',product)
    print('Quotient =',quotient) 
else: print('Can not calc')


'''Bài 2. Định nghĩa hàm kiểm tra xem một số từ bàn phím có phải là số chính phương hay không.'''

def check_square_number(n):
    x = 0
    if any(i**2 == n for i in range(n+1)):
        x = 1
    return x
n = int(input(" Fill an interger number: "))
check = check_square_number(n)
 
if check == 1:
    print(n,":is a square number")
else:
    print(n,":is not a square number")

'''Bài 3. Xác định hàm nhận vào 3 đối số, sau đó kiểm tra xem có tồn tại tam giác được tạo bởi chúng hay không. Trả lại kết quả.'''

def checkValidity(a, b, c):
     
    if (a + b > c) or (a + c > b) or (b + c > a) :
        return True
    else:
        return False       
a = 3
b = 4
c = 5
if checkValidity(a, b, c):
    print("Valid")
else:
    print("Invalid")

'''Bài 4. Định nghĩa một hàm nhận vào một đối số chuỗi và trả về số lượng nguyên âm và phụ âm.'''

def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']
def countVowels(str):
    count = 0
    for i in range(len(str)):
        if isVowel(str[i]):
            count += 1
    return count
str = 'adfsfsdfervee'
print('So nguyen am la: ',countVowels(str))
print('So phu am la: ', len(str)- countVowels(str))
'''Bài 5. Định nghĩa một hàm nhận vào một số (n) và trả về n số đầu tiên của dãy Fibonacci.'''

def fibonacci(n):  
    f = [0, 1] 
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
    return f[n]
print(fibonacci(9))

'''Bài 6. Định nghĩa một hàm nhận vào đối số bán kính và trả về diện tích và chu vi.'''

def calc_area_circm(r): 
    pi = 3.14
    return pi * r * r, 2 * pi * r 
 
area, circm = calc_area_circm(10) 
print('Area=',area)     
print('Circumference=',circm) 

'''Bài 7. Định nghĩa một hàm nhận vào 2 đối số: đối số thứ nhất là danh sách các số nguyên, đối số thứ hai là một số có giá trị mặc định là 3.
Lặp lại danh sách theo giá trị của tham số thứ 2, sau đó tính giá trị trung bình của tất cả các mục trong danh sách.'''

