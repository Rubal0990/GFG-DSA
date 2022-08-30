#User function Template for python3
from typing import List
from collections import defaultdict

class Solution:
    def mergeDetails(self, details : List[List[str]]) -> List[List[str]]:
        g = defaultdict(set)
        
        for _, *emails in details:
            first, *rest = emails
            for o in rest:
                g[first].add(o)
                g[o].add(first)
        
        seen = set()
        def dfs(email, c):
            nonlocal seen, g
            
            if email in seen:
                return
            
            seen.add(email)
            c.append(email)
            for nbr in g[email]:
                dfs(nbr, c)
        
        ans = []
        for name, *emails in details:
            email, *emails = emails
            
            if email not in seen:
                c = []
                dfs(email, c)
                ans.append([name] + sorted(c))
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

   
if __name__=="__main__":
    T = int(input())
    for t in range(T):
        
        n = int(input())
        details = []
        for i in range(n):
            detail = []
            name, m = map(str, input().strip().split())
            m = int(m)
            detail.append(name)
            l = list(map(str, input().strip().split()))
            detail.extend(l)
            details.append(detail)

        obj = Solution()
        ans = obj.mergeDetails(details)
        ans.sort()
        print('[', end = '')
        for i in range(len(ans)):
            print('[', end = '')
            for j in range(len(ans[i])):
                if j != len(ans[i]) - 1:
                    print(ans[i][j], end = ', ')
                else:
                    print(ans[i][j], end = '')
            if i != len(ans) - 1:
                print(end = '], ')
            else:
                print(end = ']')
        print(']') 

        
# } Driver Code Ends