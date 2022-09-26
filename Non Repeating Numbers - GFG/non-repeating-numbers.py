#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		xor = 0
		for i in range(len(nums)):
		    xor ^= nums[i]
		
		rightMostBit = xor & ~(xor-1)
		x, y = 0, 0
		
        for i in range(len(nums)):
            if nums[i] & rightMostBit:
                x ^= nums[i]
            else:
                y ^= nums[i]
        
        if x > y:
            x, y = y, x
        
        return [x, y]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends