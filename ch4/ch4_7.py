# Receive the amount
amount = eval(input('Enter an amount, for example, 11.56: '))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
oneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
quarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
dimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
nickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
pennies = remainingAmount

# Display the results
result = f'Your amount ${amount} consists of\n'
result += f'\t{oneDollars} dollars\n'
result += f'\t{quarters} quarters\n'
result += f'\t{dimes} dime\n'
result += f'\t{nickels} nickel\n'
result += f'\t{pennies} pennies\n'

print(result)