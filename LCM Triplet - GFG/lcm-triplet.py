#User function Template for python3

class Solution:
    def lcmTriplets(self, n):
        if n < 3:
            return n
        
        if n%2 == 0:
            if n%3 == 0:
                return (n-1) * (n-2) * (n-3)
            else:
                return (n-1) * (n-3) * (n)
        else:
            return (n) * (n-1) * (n-2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob=Solution()
        print(ob.lcmTriplets(N))
# } Driver Code Ends