import random
import os


def getQuestion(questions):
    random.shuffle(questions)
    question = questions.pop().split(',')

    return question
import random


def main():
    myFile = open('questions.txt', 'r')
    questions = myFile.read().split('\n')
    myFile.close()
    print(questions)
    question = getQuestion(questions)
    print(question)

main()