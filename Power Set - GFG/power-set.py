#User function Template for python3
from itertools import combinations

class Solution:
	def AllPossibleStrings(self, s):
		z = []
		for i in range(1, len(s)+1):
		    z.append([list(j) for j in combinations(s, i)])
        
        f = []
		for i in z:
		    for j in i:
		        s = ""
		        if len(j) == 1:
		            s += str(j[0])
		            f.append(s)
		        else:
		            for k in j:
		                s += k
		            f.append(s)

		return sorted(f)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends