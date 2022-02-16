#User function Template for python3
import itertools

class Solution:    
    def ValidCorner(self,matrix): 
        ind = {}
       
        for i in range(len(mat)):
            l = set()
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    l.add(j)
            ind[i] = l
       
        for item in ind:
            a = ind[item]
            for comp in dict(itertools.islice(ind.items(), item+1, len(mat))):
                b = ind[comp]
                if len(a.intersection(b)) >= 2:
                    return True
       
        return False


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		r = int(input())
		c = int(input())
		line = input().strip().split()
		mat = [ [0 for _ in range(c)] for _ in range(r) ]
		for i in range(r):
			for j in range(c):
				mat[i][j] = int( line[i*c+j] )
		ob=Solution()
		if (ob.ValidCorner(mat)): 
			print("Yes") 
		else: 
			print("No") 


# } Driver Code Ends