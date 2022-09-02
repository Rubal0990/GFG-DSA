
from typing import List
class Solution:
    def minimumCostOfBreaking(self,X : List[int], Y : List[int],M : int, N : int) -> int:
        cost, i, j = 0, 0, 0
        X.sort(reverse=True)
        Y.sort(reverse=True)
        
        while i < len(X) or j < len(Y):
            if i < len(X) and (j >= len(Y) or X[i] > Y[j]):
                cost += X[i] * (j + 1)
                i += 1
            else:
                cost += Y[j] * (i + 1)
                j += 1
        
        return cost



#{ 
 # Driver Code Starts

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
        
        a=IntArray().Input(2)
        m = a[0]
        n = a[1]
        
        tmp=IntArray().Input(a[0]-1) + IntArray().Input(a[1]-1)
        X = tmp[:m-1]
        Y = tmp[m-1:]
        
        obj = Solution()
        res = obj.minimumCostOfBreaking(X, Y,m,n)
        
        print(res)
        

# } Driver Code Ends