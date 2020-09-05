def minion_game(string):
    stuart = 0
    kevin = 0
    ls = len(string)
    for i,s in enumerate(string):
        if s in 'AEIOU':
            kevin+= ls-i
        else:
            stuart+= ls-i
    if kevin==stuart:
        print("Draw")
    elif kevin>stuart:
        print(f"Kevin {kevin}")
    else:
        print(f"Stuart {stuart}")

if __name__ == '__main__':
    s = input()
    minion_game(s)
