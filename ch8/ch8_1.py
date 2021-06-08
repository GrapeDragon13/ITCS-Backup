ssn = input('Enter a social security number: ')

def ssnValidity(ssn):
    if len(ssn) == 9:
        if ssn.isdigit():
            return True
        else:
            return False
    elif len(ssn) == 11:
        if ssn[3] == '-' and ssn[6] == '-':
            if ssn[:3].isdigit() and ssn[4:6].isdigit() and ssn[7:].isdigit():
                return True
            else:
                return False
            return False
    else:
        return False

if ssnValidity(ssn):
    print('Valid SSN')
else:
    print('Invalid SSN')