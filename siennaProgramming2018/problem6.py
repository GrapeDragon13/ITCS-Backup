alpha = '0123456789'

def convert(num, base):
    converted = ''
    
    while num > 0:
        converted += alpha[num % base]
        num //= base

    if len(converted) == 0:
        return '0'

    return converted[::-1]


number = int(input())
monodigit = True

# custom alpha can be increased and range can be increased to match
for i in range(2, 11):
    converted = convert(number, i)

    if len(set(converted)) == 1:
        print(f'{number} Base {i}: {converted}')

        if monodigit:
            monodigit = False

if monodigit:
    print('NO')