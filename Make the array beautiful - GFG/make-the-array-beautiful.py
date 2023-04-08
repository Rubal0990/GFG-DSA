#User function Template for python3

from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        size = len(arr)
        stack = []
        
        for i in range(size):
            if stack:
                if (stack[-1]>=0 and arr[i]<0) or (stack[-1]<0 and arr[i]>=0):
                    stack.pop()
                else: 
                    stack.append(arr[i])
            else: 
                stack.append(arr[i])
        
        return stack


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        arr = list(map(int,input().split()))
        
        obj = Solution()
        res = obj.makeBeautiful(arr)
        print(*res)
# } Driver Code Ends