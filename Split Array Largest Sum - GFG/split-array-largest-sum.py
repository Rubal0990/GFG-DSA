#User function Template for python3

class Solution:
    def splitArray(self, arr, n, k):
        def cansplit(m):
            nonlocal k, arr
            s = 0
            cnt = 1
            
            for e in arr:
                s += e
                if s > m:
                    cnt += 1
                    s = e
            
            return cnt <= k
        
        lo, hi = max(arr), sum(arr) + 1
        while lo < hi:
            mi = lo + (hi - lo) // 2
            if cansplit(mi):
                hi = mi
            else:
                lo = mi + 1
        
        return lo


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends