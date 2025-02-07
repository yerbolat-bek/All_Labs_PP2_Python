import itertools

def per(s):
    permutation = itertools.permutations(s)
    
    for perm in permutation:
        print(''.join(perm))

s = input()
per(s)
