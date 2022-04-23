#User function Template for python3

class Solution:
    def searchInsertK(self, Arr, N, k):
        lo, hi = 0, N
        
        while lo < hi:
            mi = lo + (hi - lo) // 2
            
            if Arr[mi] >= k:
                hi = mi
            else:
                lo = mi + 1
        
        return lo

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends