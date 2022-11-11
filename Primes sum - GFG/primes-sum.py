#User function Template for python3
import math

m = {i:1 for i in range(2, 10**5+1)}
m[1] = 0

for i in range(2, math.floor(math.sqrt(10**5))+1):
    if m[i] == 1:
        j = 2
        while(i*j <= 10**5):
            m[i*j] = 0
            j += 1

class Solution:
    def isSumOfTwo (self, N):
        for i in range(1, N):
            if m[i] == 1 and m[N-i] == 1:
                return 'Yes'
        
        return 'No'


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.isSumOfTwo(N))
# } Driver Code Ends