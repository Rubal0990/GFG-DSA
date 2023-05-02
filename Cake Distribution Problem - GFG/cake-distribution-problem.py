#User function Template for python3

class Solution():
    def maxSweetness(self, sweetness, n, k):
        def is_valid(val):
            sweet = count = 0
            for s in sweetness:
                sweet += s
                if sweet >= val:
                    count += 1 
                    sweet = 0
                    
            return count >= k + 1
         
        l, h = min(sweetness), sum(sweetness) + 1
        while l < h:
            mid = (l + h) // 2
            if not is_valid(mid):
                h = mid 
            else:
                l = mid + 1 
        
        return l - 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n,k = map(int, input().split())
    sweetness = [int(i) for i in input().split()]
    print(Solution().maxSweetness(sweetness, n,k))
# } Driver Code Ends