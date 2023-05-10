from typing import List

class Solution:
    def totalCuts(self, N : int, K : int, A : List[int]) -> int:
        maxv, minv = [0]*N, [0]*N
        maxv[0] = A[0]
        for i in range(1, N):
            maxv[i] = max(maxv[i-1], A[i])
        
        minv[-1] = A[-1]
        for i in range(-2, -N-1, -1):
            minv[i] = min(minv[i+1], A[i])
        
        return sum(1 for i in range(1, N) if maxv[i-1]+minv[i] >= K)

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
        
        N = int(input())
        
        
        K = int(input())
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.totalCuts(N,K,A)
        
        print(res)
        

# } Driver Code Ends