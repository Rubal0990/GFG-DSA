#User function Template for python3

class Solution:
    def newIPAdd(self, S):
        strlist = S.split(".")
        
        part = ""
        
        for i in strlist:
            part += "." + str(int(i))
            
        return part[1:]
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.newIPAdd(s)
        print(ans)
# } Driver Code Ends