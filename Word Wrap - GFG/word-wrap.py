#User function Template for python3
import math

class Solution:
    def solveWordWrap(self, nums, k):
        n = len(nums)
        dp = [[-1] * (k+1) for _ in range(n+1)]
        
        def recurse(index, cur_limit):
            if index == n:
                return 0
            
            if dp[index][cur_limit] != -1:
                return dp[index][cur_limit]
            
            if nums[index] <= cur_limit:
                take = recurse(index + 1, cur_limit - nums[index] - 1)
                not_take = (cur_limit + 1) * (cur_limit + 1) + recurse(index + 1, k - nums[index] - 1)
                dp[index][cur_limit] = min(take, not_take)
            else:
                not_take = (cur_limit + 1) * (cur_limit + 1) + recurse(index + 1, k - nums[index] - 1)
                dp[index][cur_limit] = not_take
            
            return dp[index][cur_limit]
        
        return recurse(0, k)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		k = int(input())
		obj = Solution()
		ans = obj.solveWordWrap(nums, k)
		print(ans)


# } Driver Code Ends