from typing import List

class Solution:
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        ans = 0
        cnt = 0
        for p in range(n):
            if arr[p] == 0:
                if cnt != 0:
                    ans += 1
                    cnt = 0
            
            else:
                cnt += 1
        
        if cnt == n:
            return -1
        
        if cnt != 0:
            ans += 1
        
        return ans


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
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.arrayOperations(n, arr)
        
        print(res)
        

# } Driver Code Ends