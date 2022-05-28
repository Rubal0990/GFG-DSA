#User function Template for python3

class Solution:
    def shortestPath(self, x, y): 
        d = 0
        
        while x != y:
            if x > y:
                x //= 2
            elif y > x:
                y //= 2
            
            d += 1
        
        return d

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
	t = int(input())
	for _ in range(t):
		x,y = map(int,input().strip().split())
		ob = Solution()
		print(ob.shortestPath(x,y))
# } Driver Code Ends