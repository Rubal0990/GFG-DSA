class Solution:
    def binarySearch(self, A, mid, N, M):
        std = 1
        page = 0
        
        for i in range(N):
            if page + A[i] <= mid:
                page = page + A[i]
            
            else:
                std += 1
                if std > M or mid < A[i]:
                    return False
                
                page = A[i]
        
        return True


    def findPages(self, A, N, M):
        l = 0
        r = sum(A)
        sum1 = 0
        mid = (l+r) // 2
        ans = -1
        
        if N < M:
            return -1
        
        while l <= r:
            if self.binarySearch(A, mid, N, M):
                ans = mid
                r = mid - 1 
           
            else:
                l = mid + 1
            
            mid = (l+r) // 2
    
        return ans
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends