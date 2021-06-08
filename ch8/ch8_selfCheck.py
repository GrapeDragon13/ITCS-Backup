s1 = 'Welcome'
s2 = 'welcome'

isEqual = s1 == s2
print(isEqual)

isEqual = s1.lower() == s2.lower()
print(isEqual)

b = s1.startswith('AAA')
print(b)

b = s1.endswith('AAA')
print(b)

x = len(s1)
print(x)

x = s1[0]
print(x)

s3 = s1 + s2
print(s3)

print(s1[1:])

print(s1[1:4])

s3 = s1.lower()
print(s3)

s3 = s1.upper()
print(s3)

print(s1.strip())

print(s1.replace('e', 'E'))

x = s1.find('e', 1)
print(x)

x = s1.find('abc', -1)
print(x)