def merge_the_tools(string, k):
    # your code goes here
    i = 0
    U = []
    while i<len(string):
        u = string[i:i+k]
        U.append(u)
        i = i+k

    
    #removing duplicates
    
    def remove_duplicates(str, n):
        St = "".join(dict.fromkeys(str))
        return St

    for block in U:
        line_output = remove_duplicates(block, k)
        print(line_output)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
