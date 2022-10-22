#User function Template for python3

class Solution:
    def fillingBucket(self, N):
        mod = 100000000
        fib = [0] * (N+2)
        fib[1] = 1
        fib[2] = 2
        
        for i in range(3, N+1):
            fib[i] = fib[i-1]%mod + fib[i-2]%mod
            
        return fib[N] % mod


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.fillingBucket(N))
# } Driver Code Ends