#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)

dirs = [ [ 0, -1 ],
        [ -1, 0 ],
        [ 0, 1 ],
        [ 1, 0 ] ]

def dfs(grid, x0, y0, i, j, v):
    rows = len(grid)
    cols = len(grid[0])

    if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] <= 0:
        return
    
    grid[i][j] *= -1
    v.append( (i - x0, j - y0) )
    
    for dir in dirs:
        dfs(grid, x0, y0, i + dir[0], j + dir[1], v)
    

class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        coordinates = set()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 1:
                    continue
                
                v = []
                dfs(grid, i, j, i, j, v)
                coordinates.add(tuple(v))
        
        return len(coordinates)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
# } Driver Code Ends