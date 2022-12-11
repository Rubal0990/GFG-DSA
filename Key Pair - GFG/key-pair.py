#User function Template for python3
class Solution:
	def hasArrayTwoCandidates(self, arr, n, x):
		h_map = {}
        
        for i in range(n):
            h_map[arr[i]] = i
                
        for i in range(n):
            complement = x - arr[i]
            if complement in h_map and h_map[complement] != i:
                return True
        
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends