

class Solution:
    MOVES = ((0, 1), (1, 0), (0, -1), (-1, 0))
    
    def isBounded(self, x, y):
        if 0<=x<self.M and 0<=y<self.N:
            return True
        return False

	def dfs(self, x, y):
        self.grid[x][y] = 'O'
        
        for delX, delY in Solution.MOVES:
            newX = x + delX
            newY = y + delY
            
            if not self.isBounded(newX, newY):
                continue
            
            if self.grid[newX][newY] == 'O':
                continue
                
            self.dfs(newX, newY)

    def xShape(self, grid):
		self.M, self.N = len(grid), len(grid[0])
		self.grid = grid
		ans = 0
		
		for i in range(self.M):
		    for j in range(self.N):
		        if grid[i][j] == 'X':
		            self.dfs(i, j)
		            ans += 1
		
		return ans



#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = [['#' for i in range(m)] for j in range(n)]
		for i in range(n):
			s = input().strip()
			for j in range(m):
				grid[i][j] = s[j]
		obj = Solution()
		ans = obj.xShape(grid)
		print(ans)
# } Driver Code Ends