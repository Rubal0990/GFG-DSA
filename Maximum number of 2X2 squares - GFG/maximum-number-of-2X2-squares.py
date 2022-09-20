#User function Template for python3

class Solution:
    def numberOfSquares(self, base):
        if base < 4:
            return 0
        
        if base%2 != 0:
            base -= 1
        
        x = (base-2) // 2
        y = ((x) * (x+1)) // 2  
        
        return y


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        
        n=int(input())
        ob=Solution()
        print(ob.numberOfSquares(n))
        
# } Driver Code Ends