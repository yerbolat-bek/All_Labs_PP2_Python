import math

num = float(input())
lenght = float(input())

area = (num * lenght**2) / (4 * math.tan (math.pi/num))

print("Output:", round(area,2))