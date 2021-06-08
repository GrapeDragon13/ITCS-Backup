subTotal, rate = eval(input('Enter the subtotal and gratuity rate: '))
gratuity = subTotal * rate / 100
total = subTotal + gratuity
print(f'The gratuity is {gratuity:.2f}',f'and the total is {total:.2f}')