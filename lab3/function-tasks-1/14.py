import random

def guess_the_number():
    print("Hello! What is your name?")
    n = input()

    a = random.randint(1, 20)
    print("Well,", n, "I am thinking of a number between 1 and 20.")

    cnt = 0

    while True:
        cnt += 1
        q = int(input("Take a guess.\n"))

        if q == 0:
            print("Number is", a)
            break

        if q < a:
            print("Your guess is too low.")
        elif q > a:
            print("Your guess is too high.")
        else:
            print("Good job,", n, "! You guessed my number in", cnt, "guesses!")
            break



def palindrom(t):
    t = t.lower()

    return t == t[::-1]







def unq(a):
    b = []
    
    for i in a: 
        if i not in b:
            b.append(i)
    
    return b



if __name__ == "__14__":
    print("\n Угадай число")
    guess_the_number()

    print("\n Палиндрома")
    a = input()
    if palindrom(a):
        print("Yes")
    else:
        print("No")

    print("\n Уникальные элементы списка")
    numbers = [1, 2, 2, 3, 4, 3, 5, 1]
    print(numbers)
    q = unq(numbers)
    print(q)

