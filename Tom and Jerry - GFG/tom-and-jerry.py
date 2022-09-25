#User function Template for python3

class Solution:
    def numsGame(self, N):
        if N%2 == 0:
            return 1
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.numsGame(N))
# } Driver Code Ends