from typing import List
import math 

class Solution:
    def findMinTime(self, N : int, L : int, A : List[int]) -> int:
        A.sort()
        tmp = math.ceil(N / L)
        l, r = 1, (1+tmp) * tmp//2 * A[-1]
        
        while l <= r:
            max_time = (l+r) // 2
            cnt = 0
            for rank in A:
                cnt += max(0, math.floor(math.sqrt(2*max_time / rank+0.25) - 0.5))
            
            if cnt < N: 
                l = max_time + 1
            else: 
                r = max_time - 1
        
        return l
        



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
        
        n = int(input())
        
        
        l = int(input())
        
        
        arr=IntArray().Input(l)
        
        obj = Solution()
        res = obj.findMinTime(n, l, arr)
        
        print(res)
        

# } Driver Code Ends