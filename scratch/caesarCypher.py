'''
def cypher(key):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    cypher = ''
    for each in alpha:
        letter = (ord(each) - 97 + key) % 26
        letter += 97
        cypher += f'{chr(letter)} '

    return cypher

print(cypher(int(input('Enter a number: '))))
'''
# reverse use of each other

def cypher(key):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    cypher = {}
    for each in alpha:
        letter = (ord(each) - 97 + key) % 26
        letter += 97
        cypher[chr(letter)] = each

    return cypher


def encrypt(phrase, cypher):
    encrypted = ''

    for letter in phrase:
        if letter.isspace():
            encrypted += letter
        else:
            encrypted += cypher[letter]

    return encrypted


def unEncrypt(encryptedPhrase):
    for key in range(26):
        newPhrase = ''

        for letter in encryptedPhrase:
            if letter.isspace():
                newPhrase += letter
            else:
                char = ord(letter) - 97 - key

                if char < 0:
                    char += 26
                newPhrase += chr(char + 97)

        print(newPhrase)


def main():
    key = int(input('Enter the cypher key: '))
    phrase = input('Enter the phrase: ').lower()
    cypherKey = cypher(key)
    encryptedPhrase = encrypt(phrase, cypherKey)

    print(encryptedPhrase)


#main()

encryptedPhrase = 'hello world'
unEncrypt(encryptedPhrase)