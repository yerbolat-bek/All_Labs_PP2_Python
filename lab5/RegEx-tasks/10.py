import re

camel = input()

snake = re.sub(r'([A-Z])',r'_\1',camel).lower()

print(snake)