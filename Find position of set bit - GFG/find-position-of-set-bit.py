#User function Template for python3

class Solution:
    def findPosition(self, N):
        n = bin(N).replace("0b","")
        count = 0
        
        for i in n:
            if i == "1":
                count += 1
        
        if count == 1:
            return len(n)
        else:
            return -1

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
