from math import floor, log2

class Solution:
    def noConseBits(self, n : int) -> int:
        if n == 0:
            return n
        
        l = floor(log2(n))
        mask = (1<<l)
        cnt = 0
        
        while mask > 0:
            if mask&n != 0:
                cnt += 1
            
            else:
                cnt = 0
            
            if cnt == 3:
                n = n&(~mask)
                cnt = 0
            
            mask >>= 1
        
        return n


#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.noConseBits(n)
        
        print(res)
        

# } Driver Code Ends