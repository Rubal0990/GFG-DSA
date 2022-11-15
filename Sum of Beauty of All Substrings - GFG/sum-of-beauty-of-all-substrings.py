#User function Template for python3

class Solution:
    def beautySum(self, s):
        ans = 0
        
        for i in range(len(s)):
            d = {}
            
            for j in range(i, len(s)):
                if s[j] in d:
                    d[s[j]] += 1
                else:
                    d[s[j]] = 1
                
                mf = max(d.values())
                lf = min(d.values())
                ans += (mf - lf)
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.beautySum(s))
# } Driver Code Ends