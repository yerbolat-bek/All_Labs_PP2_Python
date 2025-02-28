import re

t = input()

a = re.sub(r'(?<!^)([A-Z])',r' \1',t)

print(a)