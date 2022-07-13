import random
from re import I
from tkinter import N

words = []

print("Select difficulty (1 for easy, 2 for hard): ")
while True:
    try:
        guess = int(input("Enter a 1 or 2: "))
        if guess == 1 or guess == 2:
            break
        else:
            print("Not 1 or 2")
    except:
        print("Not an integer")  

if guess == 1:
    print("Easy mode selected")
    with open('EasyWords.txt') as f:
        line = f.readline()
        for line in f:
            words.append(line)

else:
    print("Hard mode selected")
    with open('HardWords.txt') as f:
        line = f.readline()
        for line in f:
            words.append(line)


chosenWord = words[random.randrange(0, len(words))]

answerKey = []
for element in chosenWord:
    answerKey.append(element)
    
answerKey.pop() 


displayString = []
for element in chosenWord:
    displayString.append('_')
displayString.pop()

print("The word is {} letters long.".format(len(chosenWord) - 1))

def checkAnswerKey(answerKey, guess):
    existsIn = []
    i = 0
    for element in answerKey:
        if element == guess:
            existsIn.append(i)
        i += 1
    return existsIn

def printDisplayString(displayString):
    newDisplayString = ""
    #[1] = a [2] = b
    for element in displayString:
        newDisplayString += element
        newDisplayString += " "

    return newDisplayString


#MAIN GAME LOOP

lettersUsed = []
end = False
wrongCount = 0
while not end:
    filteredGuess = ''
    while True:
        guess = input("Enter your guess: ")
        if guess.isalpha():
            if len(guess) == 1:
                used = False
                for letter in lettersUsed:
                    if letter == guess:
                        used = True
                if not used:
                    filteredGuess = guess
                    lettersUsed.append(filteredGuess)
                    break
                else:
                    print("You have already used that letter")
            else:
                print("You can only guess one character")
        else:
            print("Guess must be a letter")
        
    existsIn = checkAnswerKey(answerKey, filteredGuess)

    i = 0
    for number in existsIn:
        displayString[existsIn[i]] = filteredGuess
        i += 1

    if len(existsIn) == 0:
        print("The word does not contain that letter")
        wrongCount += 1
    
    if wrongCount == 6:
        print("Game over: too many incorrect guesses :(")
        print("The word was {}".format(chosenWord))
        break

    answerCheck = ""
    for element in displayString:
        answerCheck += element
    answerCheck += "\n"
    if answerCheck == chosenWord:
        print("Game won! The word is {}".format(chosenWord))
        print (printDisplayString(displayString))
        break
    print()
    print("Incorrect guesses: {}/6".format(wrongCount))
    print("{} is in the {} spot(s)!".format(filteredGuess, existsIn))
    print("Letters used: {}".format(printDisplayString(lettersUsed)))
    print("Current word: {}".format(printDisplayString(displayString)))
    print()
