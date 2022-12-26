def extract_digit(s):
    temp_digit=''
    for i in s:
        if i in '0123456789':
            temp_digit+=i
    return temp_digit
str1=input()
a=extract_digit(str1)
print("digits:",a)
