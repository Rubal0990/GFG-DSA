#User function Template for python3

class Solution:
	def countTriplets(self, nums):
		n, count = len(nums), 0
		for i in range(n):
		    left, right = 0, 0
		    
		    for j in range(i + 1, n):
		        if nums[j] > nums[i]:
		            right += 1
		    
		    for k in range(i):
		        if nums[k] < nums[i]:
		            left += 1
		            
		    count += left * right
		            
		return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int,input().split()))
		ob = Solution()
		ans = ob.countTriplets(nums)
		print(ans)

# } Driver Code Ends