#User function Template for python3

class Solution:
    def isPrime(self, n):
        limit = int(n ** 0.5)
        
        for i in range(2, limit + 1):
            if n % i == 0:
                return False
        
        return True
    
    def primeDivision(self, n):
        for i in range(2, n + 1):
            if self.isPrime(i) and self.isPrime(n - i):
                return [i, n - i]
        
        return [1,2]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        p1, p2 = ob.primeDivision(N)
        print(p1,end=" ")
        print(p2)
# } Driver Code Ends