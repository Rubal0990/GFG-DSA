#User function Template for python3

class Solution:
	def find_median(self, v):
	    v.sort()
	    
        if len(v)%2 == 0:
            n = len(v) // 2
            x = len(v) // 2 + 1
            return int((v[n-1]+v[x-1])//2)
        elif len(v)%2 != 0:
            m = (len(v)+1) // 2
            return v[m-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends