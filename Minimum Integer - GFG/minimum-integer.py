from typing import List

class Solution:
    def minimumInteger(self, N : int, A : List[int]) -> int:
        if N > 1:
            s_arr = sum(A)
            dict = {}
            
            for i in range(N):
                temp = N * A[i]
                if temp >= s_arr:
                   dict[temp] = A[i]
            
            return min(zip(dict.keys(),dict.values()))[1]
        
        else:
            return A[0]


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
        
        
        A=IntArray().Input(N)
        
        obj = Solution()
        res = obj.minimumInteger(N, A)
        
        print(res)
        

# } Driver Code Ends