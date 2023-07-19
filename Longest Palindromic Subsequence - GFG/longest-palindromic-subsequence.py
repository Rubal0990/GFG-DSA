#User function Template for python3

class Solution:
    def longestPalinSubseq(self, S):
        s1 = S
        s2 = S[::-1]
        n = len(S)
        dp = [[0 for i in range(len(s1)+1)] for j in range(len(s1)+1)]
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        ans = 0
        for i in dp:
            for j in i:
                ans = max(ans, j)
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends