word = input()
amount = int(input())
#targets = int(input() - 1 for i in range(amount)
targets = list(set(int(input()) for i in range(amount)))
targets.sort(reverse = True)

for target in targets:
    #word = word.replace(word[target], '')
    word = word[:target - 1] + word[(target):]

print(word)

# if not in add to newWord