n1, n2, n3 = eval(input('Enter three integers: '))
maximum = max(n1, n2, n3)
minimum = min(n1, n2, n3)
if n1 > n2 and n1 < n3:
    middle = n2
elif n2 > n1 and n2 < n3:
    middle = n2
else:
    middle = n3
print(f'max: {maximum} middle: {middle} min: {minimum}')