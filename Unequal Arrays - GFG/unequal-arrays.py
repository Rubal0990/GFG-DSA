from typing import List

class Solution:
    def solve(self, n : int, a : List[int], b : List[int]) -> int:
        sm, ans, cnt = 0, -1, 0
        odd, even = [], []
        a.sort()
        b.sort()
        
        for i in range(n):
            if b[i] & 1:
                odd.append(b[i])
            else: 
                even.append(b[i])
        
        x = len(odd) - 1
        y = len(even) - 1
        
        for i in range(n-1, -1, -1):
            if a[i] & 1:
                if x < 0: 
                    return ans
                
                sm += (a[i] - odd[x]) // 2
                cnt += max(0, (a[i] - odd[x]) // 2)
                x -= 1
            
            else:
                if y < 0: 
                    return ans
                
                sm += (a[i] - even[y]) // 2
                cnt += max(0, (a[i] - even[y]) // 2)
                y -= 1
        
        if sm != 0: 
            return ans
        
        return cnt



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
        
        
        B=IntArray().Input(N)
        
        obj = Solution()
        res = obj.solve(N, A, B)
        
        print(res)
        

# } Driver Code Ends