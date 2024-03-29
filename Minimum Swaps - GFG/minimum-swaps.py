from typing import List
class Solution:
    def minimumSwaps(self,c : List[int], v : List[int],n : int,k : int,b : int, T : int) -> int:
        diff = 0
        swaps = 0
        sheeps = 0
        slowsheeps = 0
        
        for i in range(n-1, -1, -1):
            diff = b - c[i]
            if T*v[i] >= diff:
                swaps += slowsheeps
                k -= 1
            
            else:
                slowsheeps += 1
            
            if k == 0:
                return swaps
        
        return -1



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
        
        a=IntArray().Input(4)
        n,k,b,t = a[0],a[1],a[2],a[3]
        
        c=IntArray().Input(a[0])
        
        
        v=IntArray().Input(a[0])
        
        obj = Solution()
        res = obj.minimumSwaps(c,v,n,k,b,t)
        
        print(res)
        

# } Driver Code Ends