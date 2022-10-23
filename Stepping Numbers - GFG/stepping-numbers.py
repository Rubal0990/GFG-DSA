#User function Template for python3


class Solution:
    def steppingNumbers(self, n, m):
        def _solve(v):
            if v > m: 
                return 0
            
            if n <= v <= m:
                ans = 1 
            else:
                ans = 0
            
            last = v % 10
            if last > 0: 
                ans += _solve(v*10 + last-1)
            
            if last < 9: 
                ans += _solve(v*10 + last+1)
            
            return ans
        
        
        if n > 0:
            ans = 0 
        else:
            ans = 1
        
        for i in range(1, 10):
            ans += _solve(i)
        
        return ans




#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N, M = map(int, input().split())
        ans = ob.steppingNumbers(N, M);
        print(ans)




# } Driver Code Ends