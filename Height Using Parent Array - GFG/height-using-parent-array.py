#User function Template for python3

class Solution:
    def findHeight(self, N, arr):
        arr[0] = 1
        max_height = 1
       
        for i in range(N):
            arr[i] = arr[arr[i]] + 1
            max_height = max(max_height, arr[i])
        
        return max_height

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.findHeight(N, arr))
# } Driver Code Ends