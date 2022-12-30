'''Bài 1: Viết chương trình tạo một chuỗi mới gồm ký tự đầu tiên, giữa và cuối cùng của chuỗi đầu vào. Ví du: "James" --> "Jms"'''
User_input = str(input())
a = len(User_input)
b = a//2
c = b - 1
if a % 2 == 0:
    print(User_input[0],User_input[c],User_input[b],User_input[-1])
else: print(User_input[0],User_input)


'''Bài 3: Chuỗi đã cho chứa tổ hợp chữ thường và chữ hoa.
 Viết chương trình sắp xếp các ký tự của một chuỗi sao cho tất cả các chữ cái viết thường sẽ xuất hiện trước.
 Ví du: 'PyNaTive' --> 'yaivePNT'''

str_input=str(input('Please fill the string: '))
inhoa = []
khonginhoa = []
for char in str_input:
    if char.islower():
        khonginhoa.append(char)
    else: 
        inhoa.append(char)
str_output = ''.join(khonginhoa + inhoa)
print('Output: ', str_output)

'''Bài 4: Đếm tất cả các chữ cái, chữ số và ký hiệu đặc biệt từ một chuỗi đã cho. 
Ví dụ: "P@#yn26at^&i5ve" -->

Total counts of chars, digits, and symbols Chars = 8 Digits = 3 Symbol = 4'''

def count_system():
    str_input = input('Please fill the string: ')

    chars_count = 0
    digit_count = 0
    symbol_count = 0
    for char in str_input:
        if char.isalpha():
            chars_count += 1
        elif char.isdigit():
            digit_count += 1
        else:   
            symbol_count += 1
    print('Total counts of chars, digits, and symbols')        
    print('Chars = ' , chars_count ,'Digits = ', digit_count,'Symbol = ', symbol_count)
count_system()

'''Bài 5: Viết chương trình tìm tất cả các lần xuất hiện của “USA” trong một chuỗi đã cho, bỏ qua trường hợp này. 
Ví dụ: "Welcome to USA. usa awesome, isn't it?" --> The USA count is: 2'''

str_input = str(input('Input: '))
s1 = 'usa'

string_lower = str_input.lower()
print('The USA count is: ', string_lower.count(s1))

'''Bai 6: Cho một chuỗi s1, hãy viết chương trình trả về tổng và trung bình cộng của các chữ số xuất hiện trong chuỗi, bỏ qua tất cả các ký tự khác. 
Ví dụ: str1 = "PYnative29@#8496" 
--> Sum is: 38 Average is 6.333333333333333'''

input_str = input('Input:')
Sum = 0
digit_count = 0
for char in input_str:
    if char.isdigit():
        Sum += int(char)
        digit_count += 1
print("Sum: ", Sum, "Average is: ", Sum/digit_count)

'''Bài 7: Viết chương trình đếm số lần xuất hiện của tất cả các ký tự trong một chuỗi .
Ví dụ: str1 = "Apple" --> {'A': 1, 'p': 2, 'l': 1, 'e': 1}'''

'''Bài 8: Viết chương trình tìm vị trí cuối cùng của chuỗi con “Emma” trong một chuỗi đã cho. 
"Emma is a data scientist who knows Python. Emma works at google."'''

'''Bài 9: Viết chương trình tách một chuỗi đã cho trên dấu gạch nối và hiển thị từng chuỗi con. 
Ví dụ: str1 = Emma-is-a-data-scientist --> Emma is a data scientist'''

str_input = input('Input: ')
s1 = str_input.split('-')
s2 = ' '.join(s1)
print(s2)

'''Bài 10: Xóa tất cả các ký tự khỏi một chuỗi ngoại trừ số nguyên.
 Ví dụ: str1 = 'I am 25 years and 10 months old' --> 2510'''


str_input = input('Input: ')
space = ''

for i in str_input:
    if i.isdigit():
        space+=i 
print('Output: ' ,space)
