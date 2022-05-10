class Solution:
	def sortedArrayToBST(self, nums):
	    start = 0
        end = len(nums) - 1
        root = self.makingtree(nums, start, end, [])
        
        return root
        
    def makingtree(self, nums, start, end, ans):
        if start > end:
            return
        
        mid = (start + end) // 2
        root = (nums[mid])
        ans.append(root)
        self.makingtree(nums, start, mid-1, ans)
        self.makingtree(nums, mid+1, end, ans)
        
        return ans

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.sortedArrayToBST(nums)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends