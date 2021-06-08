import random

score = 0
def math():
    global score
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    symbol = random.randint(1,3)

    if symbol == 1:
        question = input("What is " + str(num1) + "+" + str(num2) + "?")
        answer = num1 + num2
        if question == answer:
            score = score + 1

    elif symbol == 2:
        question = input("What is " + str(num1) + "-" + str(num2) + "?")
        answer = num1 - num2
        if question == answer:
            score = score + 1

    elif symbol == 3:
        question = input("What is " + str(num1) + "*" + str(num2) + "?")
        answer = num1 * num2
        if question == answer:
            score = score + 1

for i in range(10):
    math()

print("Your score was " + str(score))