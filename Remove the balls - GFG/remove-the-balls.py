from typing import List

class Solution:
    def finLength(self, N : int, color : List[int], radius : List[int]) -> int:
        stack = [(color[0], radius[0])]
        count = 0
        
        for i in range(1, N):
            if stack and stack[-1] == (color[i], radius[i]):
                stack.pop()
                count += 2
            
            else:
                stack.append((color[i], radius[i]))
        
        return N - count



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
        
        
        color=IntArray().Input(N)
        
        
        radius=IntArray().Input(N)
        
        obj = Solution()
        res = obj.finLength(N, color, radius)
        
        print(res)
        

# } Driver Code Ends