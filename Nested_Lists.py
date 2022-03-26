if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        student = []
        name = input()
        score = float(input())
        scores.append(score)
        student = [name, score]
        records.append(student)
        

    #remove min score
    k = float(min(scores))
    scores_min_removed = [i for i in scores if i != k]
    #the min score in scores_min_removed will be second lowest score
    m = min(scores_min_removed)
    #collect all names with score equal to m
    second_lowest_names = [record[0] for record in records if record[1] == m]
    second_lowest_names = sorted(second_lowest_names)
    
    #print names, one in one line
    for i in second_lowest_names:
        print(i)
