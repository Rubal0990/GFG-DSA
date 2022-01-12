#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
		maxi = 0
		for i in range(n):
		    if arr[i] > maxi:
		        maxi = arr[i]
		
		return maxi

#{ 
#  Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends