def findSum(start, stop):
    total = 0
    for i in range(start, stop):
        total += i
    return total
print(findSum(1, 6))
print(findSum(20, 26))
print(findSum(35, 41))