a, b, c = eval(input('Enter a, b, c: '))
discriminant = b ** 2 - (4 * a * c)
#d is positive
if discriminant > 0:
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    print(f'The roots are {root1:.2f} and {root2:.2f}')
#d is negative
elif discriminant < 0:
    print('The equation has no real roots.')
#d is zero
else:
    root = -b / (2 * a)
    print(f'The root is {root:.2f}')