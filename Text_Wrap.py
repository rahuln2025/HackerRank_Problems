import textwrap

def wrap(string, max_width):
    rem = len(string) % max_width
    lo = 0
    hi = (max_width)
    for i in range(len(string)- 1 - rem):
        print(string[lo:hi])
        lo = hi
        hi = lo +(max_width)
    #print(string[hi:])
    return

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
