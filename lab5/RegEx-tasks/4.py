import re

a = r'\b[A-Z][a-z]+\b'

string = ["Yerbolat", "waaw", "Pp", "PP"]

for i in string:
    if re.fullmatch(a,i):
        print(i, "- match")
    else:
        print(i,"- dont match")