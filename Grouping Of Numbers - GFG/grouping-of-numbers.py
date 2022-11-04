#User function Template for python3

class Solution:
    def maxGroupSize(self, arr, N, K):
        a = [0] * (K)
        for i in range(N):
            a[arr[i] % K] += 1
        
        ans = 0
        for i in range(1, K//2+1):
            if i != K-i:
                ans += max(a[i], a[K-i])
            
            else:
                if a[i] != 0:
                    ans += 1
        
        if a[0] != 0:
            ans += 1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxGroupSize(arr,N,K))
# } Driver Code Ends