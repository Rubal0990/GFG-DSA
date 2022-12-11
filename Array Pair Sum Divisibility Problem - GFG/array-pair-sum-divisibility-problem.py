#User function Template for python3
from collections import Counter

class Solution:
	def canPair(self, nuns, k):
		c = Counter(map(lambda num : num % k, nums))
        for num in c:
            if (not num and c[num] & 1) or (num and c[num] != c[k - num]):
                return False
    
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends