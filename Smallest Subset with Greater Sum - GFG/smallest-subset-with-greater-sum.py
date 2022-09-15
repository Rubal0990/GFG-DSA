#User function Template for python3

class Solution:
    def minSubset(self, A,N):
        s = sum(A)
        c = 0
        su = 0
        A.sort()
        A = A[::-1]
        
        for i in range(N):
            if su > s:
                break
            
            else:
                c += 1
                s -= A[i]
                su += A[i]
        
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSubset(A,N)
        print(ans)
# } Driver Code Ends