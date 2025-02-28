import re

t = input()


a = re.findall(r'[A-Z][a-z]*', t)

print(a)
