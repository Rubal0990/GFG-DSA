#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def countSubstring(self, S): 
        res = 0
        for i in range(0, len(S)):
            l = 0
            u = 0
            for j in range(i, len(S)):
                if S[j] >= 'a' and S[j] <= 'z':
                    l += 1
                else:
                    u += 1
                
                if l == u:
                    res += 1
        
        return res



#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.countSubstring(S)
        print(ans)

# } Driver Code Ends