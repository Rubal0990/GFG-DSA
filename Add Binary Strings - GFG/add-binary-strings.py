#User function Template for python3
class Solution:
	def addBinary(self, A, B):
	    while A and A[0] == '0':
                A = A[1:]
            while B and B[0] == '0':
                B = B[1:]
        
            res = ""
            carry, i, j = 0, len(A)-1, len(B)-1
            
            while i >= 0 or j >= 0 or carry > 0:
                if i >= 0:
                    x = int(A[i])
                else:
                    x = 0
            
                if j >= 0:
                    y = int(B[j])
                else:
                    y = 0
                
                v = x + y + carry
                carry = v // 2
                v %= 2
                res += str(v)
                i, j = i-1, j-1
        
            return res[: :-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		a,b = input().split(" ")
		ob = Solution()
		answer = ob.addBinary(a,b)
		
		print(answer)


# } Driver Code Ends
