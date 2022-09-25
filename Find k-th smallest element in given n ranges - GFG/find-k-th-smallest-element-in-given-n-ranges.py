from typing import List

class Solution:
    def kthSmallestNum(self, n : int, ranges : List[List[int]], q : int, queries : List[int]) -> List[int]:
        se = set()
        for i in range(n):
            for j in range(ranges[i][0], ranges[i][1]+1):
                se.add(j)
        
        li = list(se)
        li.sort()
        ji = []
        
        for i in queries:
            if i > len(li):
                ji.append(-1)
            else:
                ji.append(li[i-1])
        
        return ji


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


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        ranges=IntMatrix().Input(n, 2)
        
        
        q = int(input())
        
        
        queries=IntArray().Input(q)
        
        obj = Solution()
        res = obj.kthSmallestNum(n, ranges, q, queries)
        
        IntArray().Print(res)
        

# } Driver Code Ends