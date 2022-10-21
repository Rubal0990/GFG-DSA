#User function Template for python3

class Solution:
    def lcs(self, sizeA, sizeB, strA, strB):
        T = [[None]*1001 for _ in range(1001)]
        ranger = max(sizeA, sizeB)
        
        for i in range(ranger + 1):
            T[0][i] = 0
        
        for i in range(ranger + 1):
            T[i][0] = 0

        for i in range(1, sizeA + 1):
            for j in range(1, sizeB + 1):
                if(strA[sizeA - i] == strB[sizeB-j]):
                    T[i][j] = 1 + T[i-1][j-1]
                
                else:
                    A = T[i-1][j]
                    B = T[i][j-1]
                    T[i][j] = max(A, B)

        return T[sizeA][sizeB]


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
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends