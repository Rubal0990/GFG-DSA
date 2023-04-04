class Solution:
    def minSteps(self, str : str) -> int:
        c = 1
        ch = str[0]
        
        for i in range(1, len(str)):
            if ch != str[i]:
                c += 1
                ch = str[i]
        
        return c // 2 + 1


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.minSteps(str)
        
        print(res)
        

# } Driver Code Ends