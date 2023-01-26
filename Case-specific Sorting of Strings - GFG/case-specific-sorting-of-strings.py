#User function Template for python3

class Solution:
    def caseSort(self, s, n):
        low = []
        high = []
        val = []
        l = 0
        h = 0
        
        for i in s:
            if i.islower():
                low.append(i)
                val.append(True)
            
            else:
                high.append(i)
                val.append(False)
        
        low.sort()
        high.sort()
        x = ""
        for i in range(len(low)):
            x += low[i]
        
        ans = ""
        for i in s:
            if i.islower():
                ans += low[l]
                l += 1
            
            else:
                ans  += high[h]
                h += 1
        
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends