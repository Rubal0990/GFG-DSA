#User function Template for python3

class Solution:
    def changeBits(self, N):
        bits = 0
        n = N
        
        while n > 0:
            n  >>= 1
            bits += 1
        
        x = (1 << bits) - 1
        return x - N, x

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ans = ob.changeBits(N)
        
        print(ans[0],ans[1])
# } Driver Code Ends