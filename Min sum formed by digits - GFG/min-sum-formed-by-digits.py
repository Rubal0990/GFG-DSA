
class Solution:
    def minSum(self, arr, n):
        arr.sort()
        a = b = 0
        
        for i, j in enumerate(arr):
            if i%2 == 0:
                a = a*10 + j
            else:
                b = b*10 + j
        
        return a + b
    

#{ 
#  Driver Code Starts

import heapq as hq

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minSum(arr,n))

# } Driver Code Ends