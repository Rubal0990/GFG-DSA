#User function Template for python3

class Solution():
    def solve(self, a, b, c):
        if (a+b)*2+2 < c or (a+c)*2+2 < b or (b+c)*2+2 < a:
            return -1
        else:
            return a + b + c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import Counter
for _ in range(int(input())):
    a, b, c=map(int,input().split())
    obj = Solution()
    res = obj.solve(a, b, c)
    
    print(res)
# } Driver Code Ends