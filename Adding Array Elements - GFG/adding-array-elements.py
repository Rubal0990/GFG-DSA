from heapq import heapify, heappop, heappush

class Solution:
    def minOperations(self, arr, n, k):
        heapify(arr)
        count = 0
        
        for i in range(len(arr)):
            if arr[0]>=k:
                break
            
            res = heappop(arr) + heappop(arr)
            heappush(arr, res)
            count += 1
        
        return count


#{ 
 # Driver Code Starts

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = Solution().minOperations(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends