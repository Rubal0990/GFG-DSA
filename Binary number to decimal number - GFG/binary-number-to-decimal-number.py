#User function Template for python3

class Solution:
	def binary_to_decimal(self, str):
		char1 = []
		res = 0
		
		for char in str:
		    char1.append(int(char))
		    
	    for i in range(len(char1)):
	        res += char1.pop() * (2**i)
	    
	    return res
	    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution();
		ans = ob.binary_to_decimal(str)
		print(ans)
# } Driver Code Ends