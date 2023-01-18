if __name__ == '__main__':
    N = int(input())
    
    list = []
    commands = []
    for j in range(N):
        command = input().split()
        commands.append(command)
    #print(commands)
    
    def operate(N, list):
        for j in commands:
            
            if j[0] == 'insert':
                i, e = int(j[1]), int(j[2])
                #print(i, e)
                list.insert(i, e)
                #print(list)
            elif j[0] == 'print':
                print(list)
            elif j[0] == 'remove':
                e = int(j[1])
                list.remove(e)
                #print(list)
            elif j[0] == 'append':
                e = int(j[1])
                list.append(e)
                #print(list)
            elif j[0] == 'sort':
                list.sort()
                #print(list)
            elif j[0] == 'pop':
                list.pop()
                #print(list)
            elif j[0] == 'reverse':
                list.reverse()
                #print(list)
    
    operate(N, list)
