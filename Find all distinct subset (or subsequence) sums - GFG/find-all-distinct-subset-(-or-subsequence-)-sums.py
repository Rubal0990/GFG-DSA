#User function Template for python3

class Solution:
	def DistinctSum(self, nums):
		total = sum(nums)
		dp = [True] + [False] * total
		for x in nums:
		    for i in range(total-x, -1, -1):
		        if dp[i]:
		            dp[i + x] = True
		
		return [i for i in range(total + 1) if dp[i]]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.DistinctSum(nums)
		for _ in ans:
		    print(_, end = " ")
		print()

# } Driver Code Ends