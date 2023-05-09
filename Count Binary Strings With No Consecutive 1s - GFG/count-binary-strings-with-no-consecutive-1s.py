#User function Template for python3
class Solution: 
    def countStrings(self, N): 
        M = 10 ** 9 + 7
        
        def matrix_multiply(a, b):
            nonlocal M
            c = [[0, 0], [0, 0]]
            
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % M
            
            return c
        
        def matrix_power(a, n):
            nonlocal M
            ans = [[1, 0], [0, 1]]
            
            while n > 0:
                if n % 2 == 1:
                    ans = matrix_multiply(ans, a)
                
                a = matrix_multiply(a, a)
                n //= 2
            
            return ans
        
        return matrix_power([[1, 1], [1, 0]], N+1)[0][0]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        
        ob = Solution()
        print(ob.countStrings(int(input())))
        
        T -= 1
# } Driver Code Ends