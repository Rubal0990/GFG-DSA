#User function Template for python3

class Solution:
    def findK(self, a, n, m, k):
        l, r = 0, m - 1
        u, d = 0, n - 1
        
        while l <= r and u <= d:
            for i in range(l, r + 1):
                if k == 1:
                    return a[u][i]
                k -= 1
            
            u += 1
            for i in range(u, d + 1):
                if k == 1:
                    return a[i][r]
                k -= 1
            
            r -= 1
            if u <= d:
                for i in range(r, l - 1, -1):
                    if k == 1:
                        return a[d][i]
                    k -= 1
                d -= 1
            
            if l <= r:
                for i in range(d, u - 1, -1):
                    if k == 1:
                        return a[i][l]
                    k -= 1
                l += 1


#{ 
 # Driver Code Starts

#Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int,input().split())
    a = [
            list(map(int,input().split()))
            for _ in range(n)
        ]
    
    ob = Solution()
    print(ob.findK(a,n,m,k))
    
# } Driver Code Ends