#User function Template for python3

class Solution:
    def nCr(self, n, r):
        if r > n or n == 0:
            return 0
        
        i = 1
        j = 1
        k = 1
        fact_n = 1
        fact_r = 1
        fact_nr = 1
        while i <= n:
            fact_n *= i
            i += 1
        
        while j <= r:
            fact_r *= j
            j += 1
        
        while k <= (n - r):
            fact_nr *= k
            k += 1
        
        factorial = (fact_n) // (fact_r * fact_nr)
        return factorial % (10 ** 9 + 7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends