#User function Template for python3

class Solution:
    def waysToBreakNumber(self, n):
        n += 1
        return int((n*(n+1)//2) % 1000000007)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        print(ob.waysToBreakNumber(n))
        
# } Driver Code Ends