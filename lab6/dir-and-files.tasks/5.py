def writesome(list_of_elements):
    path = r"C:\Users\erbol\OneDrive - АО Казахстанско-Британский Технический Университет\Жұмыс үстелі\PythonLabs\Labs\lab6\dir-and-files.tasks\example\1.txt"
    
    with open(path, 'a', encoding='utf-8') as f:
        text = "\n" + " ".join(map(str, list_of_elements))
        f.write(text)

writesome([79553, 23552, 131, "bababab", "fffff", 39])
