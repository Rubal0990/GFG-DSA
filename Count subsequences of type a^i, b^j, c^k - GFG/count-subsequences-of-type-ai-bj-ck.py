#User function Template for python3

class Solution:
    def fun(self,s):
        c = 0
        bc = 0
        ans = 0
        l = len(s)
     
        for i in range(l - 1, -1, -1):
            if s[i] == 'c':
                c = 2 * c + 1
            elif s[i] == 'b':
                bc = 2* bc + c
            elif s[i] == 'a':
                ans = 2 * ans + bc
     
        return ans % (1000000007)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#Position this line where user code will be pasted.

t=int(input())
for _ in range(t):
    s=input()
    print(Solution().fun(s))
# } Driver Code Ends