#User function Template for python3

class Solution:
    def killinSpree (self, n):
  
        def squareSeries(n):
            return (n * (n+1) * (2 * n+1)) // 6
  
        def maxPeople(n):
            low = 0
            high = 1000000000000000
            while low <= high:
                mid = low + ((high - low) // 2)
                value = squareSeries(mid)
                if value <= n:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
  
        return maxPeople(n)



#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ans = ob.killinSpree(N);
        print(ans)




# } Driver Code Ends