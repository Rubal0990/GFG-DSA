#User function Template for python3
class Solution:
	def leafNodes(self, arr, N):
        ans = []
        
        def leaf(si, ei):
            if si > ei:
                return
            
            if si == ei:
                ans.append(arr[si])
                return
            
            x = -1
            for i in range(si+1, ei+1):
                if arr[i] > arr[si]:
                    x = i
                    break
            
            if x == -1:
                leaf(si+1, ei)
            else:
                leaf(si+1, x-1)
                leaf(x, ei)
        
        leaf(0, len(arr)-1)
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        ans = ob.leafNodes(arr,N)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
# } Driver Code Ends