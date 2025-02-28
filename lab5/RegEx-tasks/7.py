import re

snake = input()

words = snake.split("_")

camel = words[0] + ''.join(i.capitalize() for i in words[1:])

print(camel)