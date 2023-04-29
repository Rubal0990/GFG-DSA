#User function Template for python3

class Solution:
    def findNumber(self, N : int) -> int:
        arr = [9, 1, 3, 5, 7]
        curr = 1
        ans = 0
        
        while N > 0:
            ans = arr[N % 5] * curr + ans
            
            if N % 5 == 0:
                N = int(N / 5) - 1
            else:
                N = int(N / 5)
            
            curr *= 10
        
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        obj = Solution()
        res = obj.findNumber(N)
        
        print(res)
        
# } Driver Code Ends