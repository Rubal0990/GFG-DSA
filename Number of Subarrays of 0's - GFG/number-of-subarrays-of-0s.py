#User function Template for python3

class Solution():
    def no_of_subarrays(self, n, arr):
        ans = 0
        cnt = 0
        
        for i in range(n):
            if arr[i] == 0:
                ans += cnt + 1
                cnt += 1
            else:
                cnt = 0
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(Solution().no_of_subarrays(n, arr))
# } Driver Code Ends