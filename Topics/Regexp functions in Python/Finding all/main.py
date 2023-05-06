import re

string = input().split()
ls = []
for word in string:
    if re.match('s.*', word):
        ls.append(word.strip('.'))
print(ls)