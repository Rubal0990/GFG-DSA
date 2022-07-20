#User function Template for python3

class Solution:
    def findMinInsertions(self, s1):
        dp = [[0 for i in range(len(s1)+1)] for j in range(len(s1)+1)]
        s2 = s1[::-1]
        for i in range(len(s1)+1):
            dp[i][0] = 0

        for i in range(len(s1)+1):
            dp[0][i] = 0

        for i in range(1, len(s1)+1):
            for j in range(1, len(s1)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return len(s1) - dp[len(s1)][len(s1)]

def f(i, j, s1, s2, dp):

    if i < 0:
        return 0
    if j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]

    if s1[i] == s2[j]:
        dp[i][j] = 1 + f(i-1, j-1, s1, s2, dp)
        return dp[i][j]
    else:
        dp[i][j]= max(f(i, j-1, s1, s2, dp), f(i-1, j, s1, s2, dp))
        return dp[i][j]

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):

        S = input().strip()
        ob=Solution()
        print(ob.findMinInsertions(S))