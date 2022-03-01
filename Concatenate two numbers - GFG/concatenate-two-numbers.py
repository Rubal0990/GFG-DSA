#User function Template for python3
class Solution:
    def countPairs(self, N, X, numbers): 
        X = str(X)
        ans = 0
        d = {}
        
        for i in numbers:
            z = str(i)
            if X.startswith(z) or X.endswith(z):
                d[z] = d.get(z, 0) + 1
        
        for i,j in d.items():
            if X == 2 * i:
                ans += j * (j - 1)
            elif X.endswith(i) and X[:-len(i)] in d :
                ans += j * d[X[:-len(i)]]
        
        return ans


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,X = map(int,input().strip().split())
        numbers = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countPairs(N, X, numbers)
        print(ans)


# } Driver Code Ends