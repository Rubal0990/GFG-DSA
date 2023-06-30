#User function Template for python3
class Solution:
	def isDivisible(self, s):
		odd, even, flag = 0, 0, True
        
        for i in s:
            if i == "1":
                if flag:
                    odd += 1
                
                else:
                    even += 1
            
            flag = not flag
        
        return 1 if not abs(odd-even)%3 else 0


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.isDivisible(s)
		print(ans)

# } Driver Code Ends