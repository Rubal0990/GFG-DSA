#User function Template for python3
import math

class Solution:        
    def primeRange(self,M,N):
        res = []
        
        for i in range(M, N+1):
            flag = -1
            
            if i in [2,3]:
                res.append(i)
            
            for j in range(2, int(math.sqrt(i))+1):
                if i % j == 0:
                    flag = 1
                    break
                
                flag = 0
                    
            if flag == 0:
                res.append(i)
            
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
# } Driver Code Ends