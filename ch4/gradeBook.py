while True:
    grade = eval(input('Enter your number grade: '))
    if grade > 100:
        print('Don\'t fuck with my code.')
    elif grade >= 90:
        print('A is your letter grade.')
        break
    elif 80 <= grade < 90:
        print('B is your letter grade.')
        break
    elif 70 <= grade < 80:
        print('C is your letter grade.')
        break
    elif 65 <= grade < 70:
        print('D is your letter grade.')
        break
    else:
        print('F is your letter grade.')
        break