#User function Template for python3
class Solution:
    def stringPartition(ob,S,a,b):
        for i in range(1, len(S)):
            if int(S[:i])%a == 0 and int(S[i:])%b == 0:
                return S[:i] + " " + S[i:]
                
        return -1


#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,a,b=map(str,input().strip().split(" "))
        a=int(a)
        b=int(b)
        ob = Solution()
        print(ob.stringPartition(S,a,b))
# } Driver Code Ends