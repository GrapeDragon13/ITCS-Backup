weight = eval(input('Enter your weight in pounds: '))
height = eval(input('Enter your height in inches: '))
KG_PER_POUND = 0.45359237   #constant
M_PER_INCH = 0.254          #constant
#compute BMI
weightSI = weight * KG_PER_POUND
heightSI = height * M_PER_INCH
bmi = weightSI / (heightSI ** 2)
#display BMI
print(f'BMI is {bmi: .2f}')
if bmi < 18.5:
    print('underweigt')
elif bmi < 25:
    print('normal')
elif bmi < 30:
    print('overweight')
else:
    print('obese')
#bmi not correct