import psycopg2
import csv
from tabulate import tabulate

# Деректер базасына қосылу
conn = psycopg2.connect(
    host="localhost",
    dbname="lab102",
    user="postgres",
    password="postgres",
    port=5432
)
cur = conn.cursor()

# Егер phonebook кестесі жоқ болса, құру
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL, 
    phone VARCHAR(255) NOT NULL
)
""")
conn.commit()

# Бағдарламаны іске қосу
running = True

while running:
    print("""
Командалар тізімі:
1. "i" - деректерді енгізу (қолмен немесе CSV арқылы)
2. "u" - деректерді жаңарту
3. "q" - деректерді іздеу
4. "d" - телефон бойынша өшіру
5. "a" - барлық деректерді өшіру
6. "s" - барлық деректерді көрсету
7. "f" - бағдарламадан шығу
""")
    command = input("Команда енгізіңіз: ").strip().lower()

    # Дерек енгізу
    if command == "i":
        option = input('"csv" (файлдан) немесе "con" (қолмен) таңдаңыз: ').strip().lower()
        if option == "con":
            name = input("Аты: ")
            surname = input("Тегі: ")
            phone = input("Телефон: ")
            cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)",
                        (name, surname, phone))
            conn.commit()
            print("Дерек сәтті енгізілді.\n")

        elif option == "csv":
            filepath = input("CSV файл жолын енгізіңіз: ")
            try:
                with open(filepath, 'r') as f:
                    reader = csv.reader(f)
                    next(reader)
                    for row in reader:
                        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)",
                                    (row[0], row[1], row[2]))
                conn.commit()
                print("CSV файлдан деректер жүктелді.\n")
            except Exception as e:
                print("Қате орын алды:", e)

    # Деректерді жаңарту
    elif command == "u":
        phone = input("Қай пайдаланушыны өзгерткіңіз келеді? Оның телефон нөмірін енгізіңіз: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
        result = cur.fetchone()
        if result:
            print("Қазіргі дерек:", result)
            new_name = input("Жаңа аты (Enter бассаңыз өзгермейді): ").strip()
            new_surname = input("Жаңа тегі (Enter бассаңыз өзгермейді): ").strip()
            new_phone = input("Жаңа телефон (Enter бассаңыз өзгермейді): ").strip()

            if new_name:
                cur.execute("UPDATE phonebook SET name = %s WHERE phone = %s", (new_name, phone))
            if new_surname:
                cur.execute("UPDATE phonebook SET surname = %s WHERE phone = %s", (new_surname, phone))
            if new_phone:
                cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", (new_phone, phone))
            conn.commit()
            print("Деректер жаңартылды.\n")
        else:
            print("Мұндай телефонмен пайдаланушы табылмады.\n")

    # Деректерді іздеу
    elif command == "q":
        field = input("Қай баған бойынша іздейсіз? (id, name, surname, phone): ").strip().lower()
        value = input(f"{field} мәнін енгізіңіз: ")
        if field in ["id", "name", "surname", "phone"]:
            cur.execute(f"SELECT * FROM phonebook WHERE {field} = %s", (value,))
            rows = cur.fetchall()
            if rows:
                print(tabulate(rows, headers=["ID", "Аты", "Тегі", "Телефон"], tablefmt="grid"))
            else:
                print("Дерек табылмады.\n")
        else:
            print("Баған атауы қате.\n")

    # Бір телефонды өшіру
    elif command == "d":
        phone = input("Өшіргіңіз келетін телефон нөмірін енгізіңіз: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        conn.commit()
        print("Дерек өшірілді (егер табылса).\n")

    # Барлық деректерді өшіру
    elif command == "a":
        confirm = input("Барлық деректерді өшіруге сенімдісіз бе? (yes/no): ").strip().lower()
        if confirm == "yes":
            cur.execute("DELETE FROM phonebook")
            conn.commit()
            print("Барлық деректер өшірілді.\n")
        else:
            print("Операция тоқтатылды.\n")

    # Барлық деректерді көрсету
    elif command == "s":
        cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()
        if rows:
            print(tabulate(rows, headers=["ID", "Аты", "Тегі", "Телефон"], tablefmt="fancy_grid"))
        else:
            print("Кестеде деректер жоқ.\n")

    # Бағдарламадан шығу
    elif command == "f":
        running = False
        print("Бағдарлама жабылды.")

    else:
        print("Қате команда. Қайтадан көріңіз.\n")

# Байланысты жабу
cur.close()
conn.close()
