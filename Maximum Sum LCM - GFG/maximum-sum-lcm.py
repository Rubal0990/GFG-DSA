#User function Template for python3
import math

class Solution:
    def maxSumLCM (self, n):
        c = 0
        i = 1
        
        while i <= math.sqrt(n):
            if n%i == 0:
                if n/i == i:
                    c += i
                
                else:
                    c += i + (n // i)
            
            i += 1
        
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.maxSumLCM(n))
# } Driver Code Ends