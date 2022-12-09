#User function Template for python3

def numOfWays(M, N):
    tot, sqr = 0, N * M

    for x in range(N):
        for y in range(M):
            temp = sqr - 1
            
            if -1 < x-2 < N:
                if -1 < y-1 < M:
                    temp -= 1
                
                if -1 < y+1 < M:
                    temp -= 1
            
            if -1 < x-1 < N:
                if -1<y-2<M:
                    temp -= 1
                
                if -1<y+2<M:
                    temp -= 1
            
            if -1 < x+1 < N:
                if -1 < y-2 < M:
                    temp -= 1
                
                if -1 < y+2 < M:
                    temp -= 1
            
            if -1 < x+2 < N:
                if -1 < y-1 < M:
                    temp -= 1
                
                if -1 < y+1 < M:
                    temp -= 1
            
            tot = (tot + temp) % (10**9 + 7)

    return tot


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m,n = map(int,input().strip().split())
        print(numOfWays(m,n))

# } Driver Code Ends