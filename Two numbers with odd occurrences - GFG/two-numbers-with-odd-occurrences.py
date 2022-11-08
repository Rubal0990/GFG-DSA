#User function Template for python3
from collections import Counter

class Solution:
    def twoOddNum(self, Arr, N):
        d = Counter(Arr)
        l = []
        
        for i in d:
            if d[i]%2 != 0:
                l.append(i)
        
        ans = sorted(l)
        res = ans[::-1]
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends