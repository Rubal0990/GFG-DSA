#User function Template for python3
from typing import List
from collections import deque

class Solution:
    def chefAndWells(self, n : int, m : int, c : List[List[str]]) -> List[List[int]]:
        res = [[10 ** 9] * (m) for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if c[i][j] == "W":
                    q.append((i, j))
                    res[i][j] = 0
        
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        
        while q:
            curx, cury = q.popleft()
            
            for i in range(4):
                x, y = curx + dx[i], cury + dy[i]
                
                if x >= 0 and x < n and y < m and y >= 0 and c[x][y] != "N"and res[x][y] > res[curx][cury] + 1:
                    q.append((x, y))
                    res[x][y] = res[curx][cury] + 1
        
        for i in range(n):
            for j in range(m):
                if c[i][j] == ".":
                    res[i][j] = 0
                
                elif res[i][j] == 10 ** 9 and c[i][j] != "N":
                    res[i][j] = -1
                
                elif res[i][j] == 10 ** 9 and c[i][j] != "H":
                    res[i][j] = 0
                
                else:
                    res[i][j] *= 2
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List

class StringMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([i for i in input().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m= map(int,input().split())
    
        
        
        c=StringMatrix().Input(n, m)
        
        obj = Solution()
        res = obj.chefAndWells(n, m, c)
        
        for el in res:
            for c in el:
                print(c, end=" ")
            print()

# } Driver Code Ends