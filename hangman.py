from os import terminal_size
from random import seed
from random import randint
with open('EnglishWords(1).txt') as f:
    words = f.readlines()
hangman= [
    ["  ---"
    ,"  | o"
    ,"  | ^"
    ,"  | ^"
    ,"------"],
    ["  ---"
    ,"  | o"
    ,"  | ^"
    ,"  | /"
    ,"------"],
    ["  ---"
    ,"  | o"
    ,"  | ^"
    ,"  |"
    ,"------"],
    ["  ---"
    ,"  | o"
    ,"  |/|"
    ,"  |"
    ,"------"],
    ["  ---"
    ,"  | o"
    ,"  | |"
    ,"  |"
    ,"------"],
    ["  ---"
    ,"  | o"
    ,"  |"
    ,"  |"
    ,"------"],
    ["  ---"
    ,"  |"
    ,"  |"
    ,"  |"
    ,"------"],
    [""
    ,"  |"
    ,"  |"
    ,"  |"
    ,"------"],
    [""
    ,""
    ,""
    ,""
    ,"------"],
    [""
    ,""
    ,""
    ,""
    ,"---"],
    [""
    ,""
    ,""
    ,""
    ,""]
]
again = True
while again:
    lettersFound = []
    finished = False
    valid = False
    entered=False
    enetredLetters = []
    turns = 10
    difficulty =0
    while not (difficulty == "2" or difficulty == "1" or difficulty == "3"):
        difficulty = input("enter difficulty 1/2/3 :")
    difficulty = int(difficulty)
    word = ""
    while not (len(word) - 2 < difficulty * 4 and len(word) - 2 > (difficulty-1) * 4) or word =="":
        seed()
        word = words[randint(0,len(words)-1)]
    for i in range(len(word)-2):
        lettersFound.append([word[i],False])
    while not finished:
        valid=False
        for i in range(len(lettersFound)):
            if lettersFound[i][1]:
                print(lettersFound[i][0],end="")
            else:
                print("_ ",end="")
        print("")
        for i in range(5):
            print(hangman[turns][i])
        while not valid:
            entered = False
            letter = input("enter letter choice:")
            if len(letter) > 1 or not letter.isalpha():
                print("invalid input")
            else:                
                for i in range(len(lettersFound)):
                    if lettersFound[i][0] == letter and lettersFound[i][1] == False:
                        lettersFound[i][1] = True
                        valid = True
                for i in enetredLetters:
                    if i ==letter:
                        entered = True         
                if not valid and not entered:
                    turns -=1
                    print(letter + " is not in the word, " +str(turns)+ " fails remaining")   
                    valid = True
                elif entered:
                    print("already entered")
                enetredLetters.append(letter)
        finished = True
        for i in range(len(lettersFound)):    
            if not lettersFound[i][1]:
                finished = False
        if turns == 0:
            finished = True
    if turns ==0:
        print("you lose")       
    else:
        print("you win")
    print("the word was " + word[0:len(word)-2])
    againinput = input("do you want to play again y/n")
    again = False
    if againinput == "y":
       again = True     




