anagram1 = input().lower()
anagram2 = input().lower()
filtered1 = ''.join(sorted(filter(str.isalnum, anagram1)))
filtered2 = ''.join(sorted(filter(str.isalnum, anagram2)))

if filtered1 == filtered2:
    print('YES')
else:
    print('NO')

'''
# this works and I'm scared
print('YES') if ''.join(sorted(filter(str.isalnum, input().lower()))) == ''.join(sorted(filter(str.isalnum, input().lower()))) else print('NO')
'''