#User function Template for python3
import re

class Solution:
    def smallestSubstring(self, S):
        x1 = re.findall('[0][1]+[2]', S)
        x2 = re.findall('[0][2]+[1]', S)
        x3 = re.findall('[1][0]+[2]', S)
        x4 = re.findall('[1][2]+[0]', S)
        x5 = re.findall('[2][0]+[1]', S)
        x6 = re.findall('[2][1]+[0]', S)
        
        a = x1 + x2 + x3 + x4 + x5 + x6
        a = sorted(a, key=len)
        
        if len(a) == 0:
            return -1
        else:
            return len(a[0])

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends