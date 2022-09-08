#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		res = 0
        
        if k in arr:
            res += arr.index(k)
        else:
            res -= 1
        
        return res


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends