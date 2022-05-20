#User function Template for python3

class Solution:
    def findTime(self, S1, S2):
        curr = 0
        sum = 0
        
        for i in S2:
            sum += abs(S1.index(i)-curr)
            curr = S1.index(i)
        
        return sum

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S1=input()
        S2=input()
        
        ob = Solution()
        print(ob.findTime(S1,S2))
# } Driver Code Ends