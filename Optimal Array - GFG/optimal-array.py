from typing import List

class Solution:
    def optimalArray(self, n : int, a : List[int]) -> List[int]:
        currAns = 0
        res = []
        
        for i in range(n):
            currAns += (a[i] - a[i // 2])
            res.append(currAns)
        
        return res


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
        
        
        a=IntArray().Input(n)
        
        obj = Solution()
        res = obj.optimalArray(n, a)
        
        IntArray().Print(res)
        

# } Driver Code Ends