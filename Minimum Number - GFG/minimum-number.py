#User function Template for python3
from math import gcd

class Solution:
    def minimumNumber(self, n, arr):
        a = arr[0]
        for i in range(n):
            a = gcd(a, arr[i])
        
        return a

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.minimumNumber(n,arr))
# } Driver Code Ends