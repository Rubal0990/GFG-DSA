#User function Template for python3
class Solution:
    def swapBitGame (self, N):
        o = 0
        xo = 0
        
        while N:
            if N%2 and o:
                xo ^= o
            
            if N%2 == 0:
                o += 1
            
            N //= 2
        
        return 1 if xo else 2


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
        

        ob = Solution()
        print(ob.swapBitGame(N))
# } Driver Code Ends