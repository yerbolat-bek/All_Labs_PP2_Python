def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y 
    return x, y

print(solve(35,94))