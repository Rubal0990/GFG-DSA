from typing import List
from bisect import bisect_left
from math import inf

class Solution:
    def maxCoins(self, n : int, ranges : List[List[int]]) -> int:
        ranges.sort(key=lambda x: (x[1], x[0], x[2]))
        end = [(0, 0)]
        res = 0
        
        for si, ei, ci in ranges:
            j = bisect_left(end, (si, inf)) - 1
            ej, cj = end[j]
            res = max(res, ci + cj)
            end.append((ei, max(ci, end[-1][1])))
        
        return res


#{ 
 # Driver Code Starts
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
        
        n = int(input())
        
        
        ranges=IntMatrix().Input(n, 3)
        
        obj = Solution()
        res = obj.maxCoins(n, ranges)
        
        print(res)
        

# } Driver Code Ends