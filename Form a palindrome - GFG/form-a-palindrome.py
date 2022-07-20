# User function Template for python3

class Solution:
    def countMin(self, s):
        l = len(s)
        dp = [[0] * (l + 1) for i in range(l + 1)]

        for i in range(l):
            dp[i][i] = 1

        for i in range(l - 1, -1, -1):
            for j in range(i + 1, l):
                if s[i] == s[j]:  #
                    if i + 1 == j:
                        dp[i][j] = 2
                    elif i != j:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return len(s) - dp[0][l - 1]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.countMin(Str))
# } Driver Code Ends