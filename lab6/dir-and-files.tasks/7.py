def copier():
    s = input("Enter the name of the file: ").strip()
    
    with open(s, 'r', encoding='utf-8') as file:
        data = file.read()

    # Правильное добавление "_1" перед расширением
    if "." in s:
        copy_path = s.rsplit(".", 1)  # Разделение по последней точке
        copy_path = copy_path[0] + "_1." + copy_path[1]
    else:
        copy_path = s + "_1"

    with open(copy_path, "w", encoding='utf-8') as file_copy: 
        file_copy.write(data)

    print(copy_path)

copier()
