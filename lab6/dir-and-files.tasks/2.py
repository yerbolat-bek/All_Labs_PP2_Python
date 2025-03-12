import os

path = r"C:\Users\erbol\OneDrive - АО Казахстанско-Британский Технический Университет\Құжаттар"

if os.path.exists(path):
    print("Read:", os.access(path, os.R_OK))
    print("Write:", os.access(path, os.W_OK))
    print("Execute:", os.access(path, os.X_OK))
else:
    print("Error")