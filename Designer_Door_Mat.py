# Enter your code here. Read input from STDIN. Print output to STDOUT
#N = 9
#M = 31
def doormat(N,M):
    mid_row_index = N//2
    a = '-'
    b = '.|.' #occupies three places
    c = 'WELCOME' #occupies sevel places 

    for i in range(mid_row_index):
        b_occ = 2*i + 1
        a_occ = int((M - (3 * b_occ))/2)
        print((a*a_occ).rjust(a_occ) + (b*b_occ).center(b_occ) + (a*a_occ).ljust(a_occ)) 
        
    a_occ_mid = int((M-7)/2)
    print((a*a_occ_mid).rjust(a_occ_mid) + c + (a*a_occ_mid).ljust(a_occ_mid))

    for i in range(mid_row_index+1, N):
        b_occ = 2*(N-i) - 1
        a_occ = int((M -(3 * b_occ))/2)
        print((a*a_occ).rjust(a_occ) + (b*b_occ).center(b_occ) + (a*a_occ).ljust(a_occ))
#convert input string to N and M
N,M = input().split( )
N,M = int(N), int(M)     
doormat(N,M)
