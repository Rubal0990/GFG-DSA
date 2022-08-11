from functools import lru_cache

class Solution:
    def maxCoins(self,arr, n):
        
        @lru_cache(None)
        def max_coin(i, j):  
            if i == j:
                return arr[i], 0
            
            f1, s1 = max_coin(i+1, j)
            f2, s2 = max_coin(i, j-1)
            x = arr[i] + s1
            y = arr[j] + s2
            
            if x > y:
                return x, f1
            else:
                return y, f2
        
        return max_coin(0, n-1)[0]
 


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxCoins(arr, n))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends