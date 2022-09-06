#User function Template for python3

class Solution:
    def findMinSum(self, A,B,N):
        A.sort()
        B.sort()
        s = 0
        for i in range(N):
            s += abs(A[i] - B[i])
        
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMinSum(A,B,N)
        print(ans)
# } Driver Code Ends