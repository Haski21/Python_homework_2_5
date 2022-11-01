"""
Дана строка из символов(латинские буквы + цифры), без других символов
Нужно вывести новой строкой только цифры, если они есть или написать, что их нет.
Пример: 
In: 'antuh1ouou21au3'
Out: 1213
"""


first_str = input('Input str:')
FOO = 0

for i in range(len(first_str)):
#     а можно ли как-то одним условием указать, а не писать столько раз?
    if  first_str[i] == '0' or first_str[i] == '1' or first_str[i] == '2' or first_str[i] == '3' or first_str[i] == '4' or first_str[i] == '5' or first_str[i] == '6' or first_str[i] == '7' or first_str[i] == '8' or first_str[i] == '9':
        print(first_str[i], end = '')
        FOO = 1
if FOO != 1: print('There are not numbers')