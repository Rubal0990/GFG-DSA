#User function Template for python3

class Solution:
    def rearrange(self,arr, n):
        pos = [i for i in arr if i>=0][::-1]
        neg = [i for i in arr if i<0][::-1]
        arr.clear()
        
        for i in range(n):
            if len(pos) > 0:
                arr.append(pos.pop())
            
            if len(neg)>0:
                arr.append(neg.pop())


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends