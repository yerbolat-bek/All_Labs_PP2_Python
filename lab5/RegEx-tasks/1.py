import re

a = r'ab*'

string = ["a", "ab", "ac", "b" , "abb", "aabb"]

for i in string:
    if re.fullmatch(a,i):
        print(i, "- match")
    else:
        print(i,"- dont match")