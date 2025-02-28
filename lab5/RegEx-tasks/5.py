import re

a = r'a.*b$'

string = ["ab", "acb", "a-b", "ac", "ad", "abb", "aabb"]

for i in string:
    if re.fullmatch(a,i):
        print(i, "- match")
    else:
        print(i,"- dont match")