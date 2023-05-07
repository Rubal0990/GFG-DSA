class Solution:
    def stringMirror(self, str : str) -> str:
        ans = ""
        ans += str[0]
        
        for i in range(1, len(str)):
            if ord(str[i-1]) > ord(str[i]) or (i > 1 and str[i-1] == str[i]):
                ans += str[i]
            else:
                break
        
        ans += ans[::-1]
        return ans


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.stringMirror(str)
        
        print(res)
        

# } Driver Code Ends