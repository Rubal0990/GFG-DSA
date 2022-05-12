class Solution:
    def rec_traverse(self, grid, i, j, n, mem, visited):
        if i<0 or i>=n or j<0 or j>=n:
            return False
        
        if grid[i][j] == 2:
            mem[i][j] = True
            return mem[i][j]
        
        if grid[i][j] == 0:
            mem[i][j] = False
            return mem[i][j]
        
        if mem[i][j] != -1:
            return mem[i][j]
        
        if visited[i][j] == 0:
            return False
        
        visited[i][j] = 0
        up = self.rec_traverse(grid, i-1, j, n, mem, visited)    
        down = self.rec_traverse(grid, i+1, j, n, mem, visited)
        right = self.rec_traverse(grid, i, j+1, n, mem, visited)    
        left = self.rec_traverse(grid, i, j-1, n, mem, visited)
        mem[i][j] = (up or down or right or left)
        visited[i][j] = -1
        
        return mem[i][j]
        
    def is_Possible(self, grid):
        n = len(grid)
        mem = [[-1]*n for i in range(n)]
        visited = [[-1]*n for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    return self.rec_traverse(grid, i, j, n, mem, visited)

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.is_Possible(grid)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends