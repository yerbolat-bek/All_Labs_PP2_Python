def rw(sentence):
    return ' '.join(sentence.split()[::-1])

s = input()
print(rw(s))
