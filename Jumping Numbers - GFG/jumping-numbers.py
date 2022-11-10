#User function Template for python3

class Solution:
    def jumpingNums(self, X):
        q = list(range(1, 10))
        ans = float('-inf')
        
        while q:
            x = q.pop()
            if x > X:
                continue
            
            ans = max(ans, x)
            d = x % 10
            
            if d != 9:
                q.append(x*10 + d+1)
            if d != 0:
                q.append(x*10 + d-1)
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.jumpingNums(X))
# } Driver Code Ends