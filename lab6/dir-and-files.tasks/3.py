import os

path = r"C:\Users\erbol\OneDrive - АО Казахстанско-Британский Технический Университет\Құжаттар"

if os.path.exists(path):
    print("Catalog:", os.path.dirname(path))
    print("File name:", os.path.basename(path))
else:
    print("Error")