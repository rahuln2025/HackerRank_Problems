def print_rangoli(size):
    # your code goes here
    n = size #input
    
    import string
    alphabet_string = string.ascii_lowercase
    alphabets = list(alphabet_string)
    alphabets
    
    # letters used in the rangoli
    letters = alphabets[0:n]


    #looping all for all rows from j = 0 to j = 2*n -1
    row_len = 2*(2*n - 1) - 1
    rows = 2*n - 1
    middle_row = rows // 2

    for j in range(0, 2*n-1):
    
        if j <= middle_row:
            l = letters[n-(j+1):n] #valid for first half of all rows i.e. till middle
        elif j> middle_row:
            l = letters[j+1-(n):n] #valid for second half of all rowns i.e. after middle row to last row
    
        char_len = 2*(2*len(l) - 1) - 1
        char_mid = char_len // 2
    
        dash = '-'
        char = ""
        # initialize a variable to traverse through char
        char_travel = 1
   
        #first half
        for i in range(char_mid):
            #print(i)
            if i % 2 == 0:
                char = char + l[len(l) - char_travel]
                char_travel = char_travel + 1
            else:
                char = char + dash

        #later half
        for i in range(char_mid, char_len):
            #print(i)
            if i % 2 == 0:
                char = char + l[len(l) - char_travel]
                char_travel = char_travel - 1
            else:
                char = char + dash
    
        number_of_dashes = int((row_len - char_len)/2)
        dashes = dash*number_of_dashes
    
        # combining all for one single row

        row = dashes + char + dashes
        print(row)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
