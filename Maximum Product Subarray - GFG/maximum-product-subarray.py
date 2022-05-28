#User function Template for python3
class Solution:
	def maxProduct(self, arr, n):
		current_max = current_min = maxi = arr[0]
		
		for i in range(1, n):
		    if arr[i] > 0:
		        current_max = max(arr[i], current_max * arr[i])
		        current_min = min(arr[i], current_min * arr[i])
	        else:
	            temp = current_max
		        current_max = max(arr[i], current_min * arr[i])
		        current_min = min(arr[i], temp * arr[i])
	        
	        maxi = max(maxi,current_max)
	    
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
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends