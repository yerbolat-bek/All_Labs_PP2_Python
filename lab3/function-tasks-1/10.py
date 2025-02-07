def unq(a):
    b = []
    
    for i in a: 
        if i not in b:
            b.append(i)
    
    return b

numbers = [1, 2, 2, 3, 4, 3, 5, 1]
result = unq(numbers)
print(result)
