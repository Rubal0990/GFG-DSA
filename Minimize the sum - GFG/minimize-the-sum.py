#User function Template for python3
import heapq

class Solution:
    def minimizeSum(self, N, arr):
        sum1 = 0
        heapq.heapify(arr)
        
        while N > 1:
            x, y = heapq.heappop(arr), heapq.heappop(arr)
            sum1 += (x + y)
            heapq.heappush(arr, x + y)
            N -= 1
        
        return sum1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        A = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minimizeSum(n, A))
# } Driver Code Ends