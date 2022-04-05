#User function Template for python3

class Solution:
    def countShare(self,B):
        n = B // 2 -1
        return n * (n + 1) // 2

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        b=int(input().strip())
        obj=Solution()
        print(obj.countShare(b))
        
# } Driver Code Ends