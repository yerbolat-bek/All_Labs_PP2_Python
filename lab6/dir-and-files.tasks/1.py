import os

path = r"C:\Users\erbol\OneDrive - АО Казахстанско-Британский Технический Университет\Құжаттар"
if os.path.exists(path):
    print(os.listdir(path))
else:
    print("Error")

