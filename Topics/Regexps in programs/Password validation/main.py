import re

password = input()
# your code here
print('Thank you!' if re.match('[A-Za-z\d+]{6,15}', password) else 'Error!')