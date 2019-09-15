#!/bin/python
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print("Start guessing...")
word = "secret"
g=input()
turns = 10
while turns > 0:
    failed = 0
    for ch in word:
        if ch in g:
            print(ch)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You won")
        break
    guess = input("guess a character:")
    g += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
    print("You have", + turns, "more guesses")
    if turns == 0:
        print("You Loose")