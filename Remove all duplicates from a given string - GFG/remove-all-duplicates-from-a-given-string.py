#User function Template for python3

class Solution:
	def removeDuplicates(self, str):
	    res = ""
	    
	    for i in str:
	        if i not in res:
	            res += i
	            
	    return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        str = input().strip()
        ob = Solution()
        ans = ob.removeDuplicates(str)
        print(ans)
        tc -= 1

# } Driver Code Ends