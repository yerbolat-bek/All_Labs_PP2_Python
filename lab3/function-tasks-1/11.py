def palindrom(t):
    t = t.lower()

    return t == t[::-1]

a = input()

if palindrom(a):
    print("Yes")
else:
    print("No")
