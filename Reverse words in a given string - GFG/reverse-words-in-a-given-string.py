
# User function Template for python3

class Solution:
    def reverseWords(self,S):
        res = S.split(".")
        n = len(res)
            
        return ".".join(res[::-1])

#{ 
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends