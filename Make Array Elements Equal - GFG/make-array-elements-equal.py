#User function Template for python3

class Solution:
    def minOperations(self, N):
        n = N // 2
        
        if N % 2 != 0:
            s = n * (n + 1)
        
        else:
            s = n * n
        
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N =int(input())
        ob = Solution()
        print(ob.minOperations(N))
        
        T -= 1

# } Driver Code Ends