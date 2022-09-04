#User function Template for python3

class Solution:
    def pattern(self, n):
        count = n * (n + 1)
        
        return self.output([], n, 1, count-n+1, 0)
    
    def output(self, ans, n, left, right, offset):
        if n == 0:
            return ans
        
        line = "-" * offset
        line += "*".join(str(left + i) for i in range(n))
        line += "*" + "*".join(str(right + i) for i in range(n))
        ans.append(line)
        return self.output(ans, n-1, left+n, right-n+1, offset+2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.pattern(n)
        for i in range(n):
            print(ans[i])
# } Driver Code Ends