#User function Template for python3
class Solution:
	def convert(self, arr, n):
		a = []
		for i in range(len(arr)):
		    a.append((arr[i], i))
		
		a.sort(key = lambda x:x[0])
		for i in range(len(a)):
		    ind = a[i][1]
		    arr[ind] = i
		
		return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.convert(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends