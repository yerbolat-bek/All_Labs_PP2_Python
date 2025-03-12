s = input()
up = 0
low = 0
for i in s:
    if i.isupper():
        up+=1
    elif i.islower():
        low+=1

print(up)
print(low)