#User function Template for python3

class Solution:
	def longestIncreasingPath(self, matrix):
		n, m = len(matrix), len(matrix[0])
     
        dp = [[0 for _ in range(m)] for _ in range(n)]
        vis = [[False for _ in range(m)] for _ in range(n)]
       
        def dfs(r, c):
            if vis[r][c] : 
                return dp[r][c]
            
            vis[r][c] = True
            for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                if r+dr>=0 and r+dr<n and c+dc>=0 and c+dc<m and matrix[r][c]<matrix[r+dr][c+dc]:
                    dp[r][c] = max(dp[r][c], dfs(r+dr, c+dc))
       
            dp[r][c] += 1
            return dp[r][c]
        
        res = 0
        for r in range(n):
            for c in range(m):
                res = max(res, dfs(r, c))
         
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.longestIncreasingPath(matrix)
		print(ans)

# } Driver Code Ends