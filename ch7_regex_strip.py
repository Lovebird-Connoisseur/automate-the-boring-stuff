import re


def string_strip(value, to_remove):
    if to_remove != '':
        return str(value).replace(to_remove, '')
    else:
        return str(value).replace(mo.group(), '')


string_value = '   test foo bar   '
to_replace = input('Value to replace: ')

strip_regex = re.compile(r'^(\s+)')
mo = strip_regex.search(string_value)

print(string_strip(string_value, to_replace))
