import re

t = "What is this.Computer,science"

a = re.sub(r'[ ,.]', ':', t)

print(a)
