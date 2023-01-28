class Solution:
    def solve(self, a : int, b : int) -> int:
        if a == b:
            return 0
        
        temp = a & b
        if temp != a and temp != b:
            return 2
        
        return 1


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.solve(a, b)
        
        print(res)
        

# } Driver Code Ends