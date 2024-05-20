# 8 lenght, upper case and lowercase, atleast 1 digit
# lenth, digits

import re

lenth_regex = re.compile(r'.{8,}')
upper_case_regex = re.compile(r'[A-Z]')
lower_case_regex = re.compile(r'[a-z]')
digit_regex = re.compile(r'\d')

password = input('Insert your password: ')

mo_lenth = lenth_regex.findall(password)
mo_upper = upper_case_regex.findall(password)
mo_lower = lower_case_regex.findall(password)
mo_digit = digit_regex.findall(password)

if mo_lenth == []:
    print('Weak password: Not lenthy enough')
    print(mo_lenth)
elif mo_upper == []:
    print('Weak password: No uppercase characters')
    print(mo_upper)
elif mo_lower == []:
    print('Weak password: No lowercase characters')
    print(mo_lower)
elif mo_digit == []:
    print("Weak password: Doesn't contain digits")
    print(mo_digit)
else:
    print('This is a good password!')
    print('Good lenth')
    print('Contains uppercase characters')
    print('Contains lowercase characters')
    print('Contain digits')
