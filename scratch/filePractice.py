
myFile = open('data.txt', 'r')
data = []
while True:
    text = myFile.readline()
    if text != '':
        data.append(text)
    else:
        break
myFile.close()
print(data)

myFile = open('data.txt', 'r')
text = myFile.read().split('\n')
myFile.close()
#data = text.split('\n')
print(data)