

class Solution:
	def findMaxArea(self, grid):
		global area
        area = 0
        dx = [0, 0, -1, 1, 1, -1, -1, 1]
        dy = [1, -1, 0, 0, 1, 1, -1, -1]
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        
        def dfs(i,j,visited):
            global area
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0 or visited[i][j]:
                return
            
            area += 1
            visited[i][j] = True
            for k in range(8):
                dfs(i+dx[k], j+dy[k], visited)
        
        res = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]==1:
                    dfs(i, j, visited)
                
                res = max(res, area)
                area = 0
        
        return res


#{ 
 # Driver Code Starts


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(map(int, input().split()))
            grid.append(a)
        obj = Solution()
        ans = obj.findMaxArea(grid)
        print(ans)

# } Driver Code Ends