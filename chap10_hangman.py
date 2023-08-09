def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|       |       ",
              "|       O       ",
              "|      /|＼     ",
              "|       /＼     ",
              "|               ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) -1 :
        print("\n")
        msg = ("一文字を予想してね！")
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            print(" ".join(board))
        else:
            wrong += 1
            print(" ".join(board))
            e = wrong + 1
            print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}".format(word))




words_list = ["MONSTERHUNTER",
              "GENSHINIMPACT",
              "NieR:Automata",
              "地獄楽",
              "MonsterStrike"
              ]
'''
while True:
    num = input("0から4で好きな数字を入力:")
    try:
        num = int(num)
    except ValueError:
        print("数字を入力してください")
    if num in range(0, 5):
        Q_word = str(words_list[num])
        break
'''

import random

num = random.randint(0, 5)
Q_word = str(words_list[num])

hangman(Q_word)
        
