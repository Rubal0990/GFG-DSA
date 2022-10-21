#User function Template for python3
class Solution:
	def reverseSpiral(self, R, C, a):
		left, right = 0, C
		top, bottom = 0, R
		res = []
		
		while left < right and top < bottom:
		    for i in range(left, right):
		        res.append(a[top][i])
		    
		    top += 1
		    for i in range(top, bottom):
		        res.append(a[i][right-1])
		    
		    right -= 1
		    if not (left < right and top < bottom):
		        break
		    
		    for i in range(right-1, left-1, -1):
		        res.append(a[bottom-1][i])
		    
		    bottom -= 1
		    for i in range(bottom-1, top-1, -1):
		        res.append(a[i][left])
		      
		    left += 1      
		
		return res[::-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C=[int(x) for x in input().split()]
        a=[[0]*C for c in range(R)]
        arr=input().split()
        for i in range(R*C):
            a[i//C][i%C]=int(arr[i])
            
        ob=Solution()
        ans=ob.reverseSpiral(R,C,a)
        for i in range(len(ans)):
            print(ans[i],end=" ")
            
        print()
# } Driver Code Ends