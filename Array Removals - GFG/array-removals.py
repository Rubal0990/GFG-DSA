#User function Template for python3

class Solution:
	def removals(self, arr, n, k):
        arr.sort()
        start = 0
        end = 0
        max_len = 0
        
        while end < n:
            if arr[end]-arr[start] <= k:
                if max_len < end-start:
                     max_len = end-start
                
                end += 1
            
            else:
                start += 1
            
            ans = n - (max_len + 1)
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.removals(arr, n, k)
        print(ans)
        tc -= 1
# } Driver Code Ends