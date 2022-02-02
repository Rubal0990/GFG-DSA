#User function Template for python3

class Solution:
    def findPosition(self, N):
        for i in range(30):
            if 1<<i > N:
                return -1
            elif 1<<i == N:
                return i+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends