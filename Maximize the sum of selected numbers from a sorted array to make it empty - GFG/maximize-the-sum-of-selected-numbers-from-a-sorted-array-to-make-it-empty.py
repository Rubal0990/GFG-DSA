#User function Template for python3
from collections import defaultdict

class Solution:
    def maximizeSum (self, arr, n) : 
        ans = defaultdict(int)
        a = [False] * n
        sumi = 0
        
        for i in arr:
            ans[i] += 1
        
        for i in range(n-1, -1, -1):
            if a[i] == False:
                a[i] = True
                sumi += arr[i]
                if ans[arr[i]-1] > 0:
                    a[i-ans[arr[i]]] = True
                    ans[arr[i]-1] -= 1
        
        return sumi



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    ob=Solution()
    
    ans = ob.maximizeSum(arr, n)
    print(ans)

    





# } Driver Code Ends