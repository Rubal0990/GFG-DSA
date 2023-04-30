from typing import List

class Solution:
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        d = {}
        for start, end in intervals:
            if start not in d:
                d[start] = 0
            if end+1 not in d:
                d[end+1] = 0
            d[start] += 1
            d[end+1] -= 1
        
        v = -1
        temp = 0
        for el in sorted(d.keys()):
            if d[el] >= 0:
                temp += d[el]
                if temp >= k:
                    v = el
            
            else:
                if temp >= k:
                    v = el - 1
                
                temp += d[el]
        
        return v


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
        
        
        intervals=IntMatrix().Input(n, 2)
        
        
        k = int(input())
        
        obj = Solution()
        res = obj.powerfullInteger(n, intervals, k)
        
        print(res)
        

# } Driver Code Ends