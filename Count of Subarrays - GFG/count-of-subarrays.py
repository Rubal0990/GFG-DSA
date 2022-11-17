#User function Template for python3
class Solution:
	def countSubarray(self,arr, n, k):
	    ans = n * (n + 1) // 2
          l = 0
        
          for i in range(n):
              if arr[i] <= k:
                  l += 1
              else:
                  ans -= (l * (l + 1) // 2)
                  l = 0
        
          ans -= (l * (l + 1) // 2)
          return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, k=map(int, input().strip().split())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.countSubarray(arr, n, k)
        print(ans)
        tc=tc-1
# } Driver Code Ends