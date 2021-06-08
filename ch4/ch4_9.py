package1Weight, package1Price = eval(input('Enter the weight and price for package 1: '))
package2Weight, package2Price = eval(input('Enter the weight and price for package 2: '))
package1 = package1Price / package1Weight
package2 = package2Price / package2Weight
print(f'Package 1: ${package1:.2f}')
print(f'Package 2: ${package2:.2f}')
if package1 < package2:
    print('Package 1 has the better price.')
elif package2 < package1:
    print('Package 2 has the better price.')
else:
    print('They are the same price.')