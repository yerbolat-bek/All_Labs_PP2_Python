import json

with open("c:/Users/erbol/OneDrive - АО Казахстанско-Британский Технический Университет/Жұмыс үстелі/PythonLabs/Labs/lab4/json/sample-data.json", "r") as file:
    data = json.load(file)

print("Interface status")
print("=" * 80)
print("DN", " " * 40, "Description ", "speed", " " * 10, "MTU")
print("-" * 41, "-" * 12, "-" * 13, "\t", "-" * 4)
for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]:
            print(imdata[i][j]["dn"],"\t", "\t\t\t"  , imdata[i][j]["speed"] ,"\t\t" , imdata[i][j]["mtu"])