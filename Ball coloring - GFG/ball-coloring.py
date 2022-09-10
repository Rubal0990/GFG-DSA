#User function Template for python3
class Solution:
    def noOfWays (self, n):
        return n*(n-1) + 2


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.noOfWays(n))
# } Driver Code Ends