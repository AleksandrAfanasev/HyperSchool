import re


# put your regex in the variable template
template = r"(\d{1,2}\/\d{1,2}\/\d{4}|\d{1,2}\.\d{1,2}\.\d{4})"
string = input()
# compare the string and the template
print(string.strip('a') if re.match(template, string) else None)
