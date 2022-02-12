#User function Template for python3
import heapq

class Solution:
    def maxEvents(self, start, end, N):
        events = []
        
        for s1, e1 in zip(start, end):
            events.append([s1, e1])
        
        events.sort(key=lambda x:(x[0],x[1]))
        idx = 0
        n = len(events)
        heap = []
        res = 0
        d = events[idx][0]
        
        while heap or idx < n:
            if not heap:
                d = events[idx][0]
        
            while idx < n and events[idx][0] <= d:
                heapq.heappush(heap, events[idx][1])
                idx += 1
                
            heapq.heappop(heap)
            res += 1
            d += 1
            
            while heap and heap[0] < d:
                heapq.heappop(heap)
                
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        start=list(map(int,input().split()))
        end=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxEvents(start,end,N))
# } Driver Code Ends