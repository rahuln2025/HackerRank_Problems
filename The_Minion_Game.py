def minion_game(string):
    # your code goes here
    Kevin = 0;
    Stuart = 0;
    str_len = len(string)
    for i in range(str_len):
        if s[i] in "AEIOU":
            Kevin += (str_len)-i
        else :
            Stuart += (str_len)-i
    
    if Kevin >Stuart:
        print("Kevin", Kevin)
    elif Kevin < Stuart:
        print("Stuart",Stuart)
    elif Kevin == Stuart:
        print("Draw")
    else :
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
