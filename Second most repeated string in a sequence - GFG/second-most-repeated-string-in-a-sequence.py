#User function Template for python3
from collections import Counter

class Solution:
    def secFrequent(self, arr, n):
        cnt = Counter(arr)
        return sorted(cnt, key=cnt.get)[-2]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        arr = input().strip().split(" ")
        ob = Solution()
        ans = ob.secFrequent(arr,n)
        print(ans)
# } Driver Code Ends