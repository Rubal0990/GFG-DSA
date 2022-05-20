#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
        if n <= 1:
            return 0
        
        if arr[0] == 0:
            return -1
        
        reach = arr[0]
        jumps = 1
        moves = arr[0]
        
        for i in range(1, n):
            if i == n-1:
                return jumps
           
            reach = max(reach, arr[i]+i)
            moves -= 1
           
            if moves == 0:
                jumps += 1
               
                if i >= reach:
                    return -1
               
                moves = reach - i
           
        return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends