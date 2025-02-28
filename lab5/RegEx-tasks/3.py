import re

a = r'\b[a-z]+_[a-z]+\b'

string = ["a_b", "ab", "ac", "b" , "abb", "aabb", "yerbolat_bek", 'AV', "Yerbolat"]

for i in string:
    if re.fullmatch(a,i):
        print(i, "- match")
    else:
        print(i,"- dont match")