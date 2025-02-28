import re

a = r'ab{2,3}$'

string = ["a", "ab", "ac", "b" , "abb", "aabb", "abbb"]

for i in string:
    if re.fullmatch(a,i):
        print(i, "- match")
    else:
        print(i,"- dont match")