number = eval(input('Enter a number between 0 and 1000: '))
thousandDisplay = number % 10
thousand = number // 10
hundredDisplay = thousand % 10
hundred = thousand // 10
tenDisplay = hundred % 10
ten = hundred // 10
oneDisplay = ten % 10
one = ten // 10
total = thousandDisplay + hundredDisplay + tenDisplay + oneDisplay
print('The sum of the digits is', total)