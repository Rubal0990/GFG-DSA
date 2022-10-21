#User function Template for python3
class Solution:
    def minimumNumberOfSwaps(self, S):
        opn, close, unbal, swap = 0, 0, 0, 0
        
        for i in S:
            if i == '[':
                opn += 1
                if unbal > 0:
                    swap += unbal
                    unbal -= 1
            else:
                close += 1
                unbal = close - opn
        
        return swap


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        ob = Solution()
        print(ob.minimumNumberOfSwaps(S))
# } Driver Code Ends