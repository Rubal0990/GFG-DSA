class Solution:
    def leaders(self, A, N):
        maxi = [A[N-1]]
        
        for i in range(N-2, -1, -1):
            if (A[i] >= maxi[-1]):
                maxi.append(A[i])
        
        return maxi[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends