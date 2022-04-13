#User function Template for python3

class Solution:
	def MinCoin(self, nums, amount):
		dp = [0] * (amount + 1)
		
        for i in range(1, amount + 1):
            cnt = float('inf')
            for n in nums:
                if i - n >= 0:
                    cnt = min(cnt, dp[i-n])
            dp[i] = cnt + 1
            
        return dp[amount] if dp[amount] != float('inf') else -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, amount = input().split()
		n = int(n)
		amount = int(amount)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.MinCoin(nums, amount)
		print(ans)
# } Driver Code Ends