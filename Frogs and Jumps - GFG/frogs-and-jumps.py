#User function Template for python3

class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        leavesArr = [0] * leaves
        frogs = sorted(list(set(frogs)))
        
        for i in frogs:
            mul = 1
            while i <= leaves and mul * i <= leaves:
                curr = mul * i - 1
                if leavesArr[curr] == 0:
                    leavesArr[curr] = 1
                
                mul += 1
        
        ans = 0
        for i in leavesArr:
            if i == 0:
                ans += 1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    
    T = int(input())
    while T > 0: 
        N, leaves = [int(i) for i in input().split()]
        frogs = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.unvisitedLeaves(N, leaves, frogs))
        
        T -= 1
# } Driver Code Ends