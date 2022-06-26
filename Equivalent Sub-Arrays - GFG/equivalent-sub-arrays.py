#User function Template for python3
from collections import Counter

class Solution:
    def countDistinctSubarray(self,arr, n): 
        cnt = len(Counter(arr))
        
        left, ans = 0, 0
        m = Counter()
        
        for i, e in enumerate(arr):
            
            m[e] += 1
            while len(m) == cnt and left < n:
                ans += n-i
                m[arr[left]] -= 1
                if m[arr[left]] == 0:
                    del m[arr[left]]
                
                left += 1
                
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.countDistinctSubarray(a,n))




# } Driver Code Ends