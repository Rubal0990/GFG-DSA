#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        mx = {}
        cursum = 0
        maxlen = 0
        
        for j, i in enumerate(arr):
            cursum += i
            if i == 0 and maxlen == 0:
                maxlen = 1
            
            if cursum == 0:
                maxlen = j+1
            
            if cursum in mx:
                maxlen = max(maxlen, j-mx[cursum])
            else:
                mx[cursum] = j
        
        return maxlen

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends