#coding: UTF-8

def hangman(word):
    wrong = 0
    stages = ["",
              "_____________           ",
              "|            |          ",
              "|            |          ",
              "|            O          ",
              "|          / | \        ",
              "|           / \         ",
              "|                       ",
              "|                       "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "guess 1 charactor"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = '$'
        else:
            wrong += 1
        print ("\n".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("you win!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("you lost! {}.".format(word))

hangman("cat")
