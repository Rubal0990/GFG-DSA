class Solution:
    def findSum(self, A, N): 
        mini = float('inf')
        maxi = float('-inf')
        
        for i in A:
            mini = min(mini, i)
            maxi = max(maxi, i)
        
        return mini + maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends