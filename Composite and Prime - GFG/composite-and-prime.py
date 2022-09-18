#User function Template for python3

class Solution:
	def Count(self, L, R):
		pri = [0] * (R+1)
        for i in range(2, R+1):
            if pri[i] == 0:
                for j in range(i*i, R+1, i):
                    pri[j] = 1
        
        c = 0
        p = 0
        for i in range(L, R+1):
            if pri[i] == 1:
                c += 1
            
            if pri[i] == 0:
                p += 1
    
        if L == 1:
            return ((c - p) + 1)
        else:
            return (c - p)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		L, R = input().split()
		L = int(L); R = int(R)
		ob = Solution()
		ans = ob.Count(L, R)
		print(ans)

# } Driver Code Ends