#User function Template for python3

class Solution:
    def Solve(self, n, a):
        h_map = {}
        ans = []
        
        for ele in a:
            if ele in h_map:
                h_map[ele] += 1
            else:
                h_map[ele] = 1
            
            if h_map[ele] > n/3:
                ans.append(ele)
        
        if ans != []:
            return set(ans)
        else:
            return [-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        res = ob.Solve(n, a)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends