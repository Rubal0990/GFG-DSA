from typing import List

class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        d = {}
        ind = 0
        
        for i in arr:
            if i in d:
                d[i].append(ind)
            else:
                d[i] = [ind]
            
            ind += 1
        
        res = [0 for i in range(n)]
        prev = 0
        for i in sorted(d.keys()):
            for j in d[i]:
                res[j] = prev
            
            prev += i * len(d[i])
        
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
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.smallerSum(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends