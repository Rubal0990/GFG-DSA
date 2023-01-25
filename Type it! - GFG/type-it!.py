#User function Template for python3

class Solution:
    def minOperation(self, s): 
        s = list(s)
        c = 0
        
        while s:
            if len(s)%2 == 0:
                m = len(s) // 2
                if s[:m] == s[m:]:
                    c += m+1
                    return c
                
                else:
                    s.pop()
                    c += 1
            
            else:
                s.pop()
                c += 1
        
        return c



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.minOperation(s)
        print(ans)
# } Driver Code Ends