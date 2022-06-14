#User function Template for python3

class Solution:
    def check(self, p: int, n: int):
        temp = p
        count = 0
        f = 5
        
        while f <= temp:
            count += temp//f
            f *= 5
     
        return count >= n
    
    def findNum(self, n : int):
        if n == 1:
            return 5
        
        low = 0
        high = 5 * n
      
        while low < high:
            mid = (low + high) >> 1
            
            if self.check(mid, n):
                high = mid
            else:
                low = mid + 1
         
        return low

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends