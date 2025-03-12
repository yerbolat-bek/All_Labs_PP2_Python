import os

path = r"C:\Users\erbol\OneDrive - АО Казахстанско-Британский Технический Университет\Жұмыс үстелі\PythonLabs\Labs\lab6\dir-and-files.tasks\example\1.txt"

with open(path, 'r', encoding='utf-8') as f:
    data = f.read()

print(len(data.split("\n")))