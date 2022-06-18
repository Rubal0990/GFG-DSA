from typing import List

class Solution:
    def longestPath(self, mat : List[List[int]], n : int, m : int, xs : int, ys : int, xd : int, yd : int) -> int:
        ans = -1
        
        def dfs(x, y, visited, dist):
            nonlocal ans
            if mat[x][y] == 0 or (x, y) in visited:
                return

            if (x, y) == (xd, yd): 
                ans = max(dist, ans)
                return

            visited.add((x, y))
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    dfs(nx, ny, visited, dist+1)

            visited.remove((x, y))
        
        dfs(xs, ys, set(), 0)
        return ans
        




#{ 
#  Driver Code Starts


class IntArray:

    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
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
        
        a=IntArray().Input(2)
        
        
        b=IntArray().Input(4)
        
        
        mat=IntMatrix().Input(a[0], a[0])
        
        obj = Solution()
        res = obj.longestPath(mat,a[0],a[1],b[0],b[1],b[2],b[3])
        
        print(res)
        


# } Driver Code Ends