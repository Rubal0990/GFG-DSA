class Solution:
	def sortedArrayToBST(self, nums):
	    s = 0
        e = len(nums) - 1
        root = self.makingtree(nums, s, e, [])
        
        return root
        
    def makingtree(self, nums, s, e, ans):
        if s > e:
            return
        
        mid = (s + e) // 2
        root = (nums[mid])
        ans.append(root)
        self.makingtree(nums, s, mid-1, ans)
        self.makingtree(nums, mid+1, e, ans)
        
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