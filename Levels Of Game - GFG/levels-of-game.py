from typing import List


class Solution:
    def maxLevel(self, h:int,m:int) -> int:
        # code here
        a = max(int((4 * h - m) / 75), 0)
        h1 = 4 * h - 60 * a
        m1 = m + 15 * a
        n = (max(min(h1, m1), h1 - 60) - 1) // 8
        
        return 2 * n + 1



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
        h,m = a[0],a[1]
        obj = Solution()
        res = obj.maxLevel(h,m)
        
        print(res)
        

# } Driver Code Ends