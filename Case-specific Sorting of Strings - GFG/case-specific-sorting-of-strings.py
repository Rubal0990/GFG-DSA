#User function Template for python3

class Solution:
    def caseSort(self,s,n):
        su = []
        sl = []
        
        for i in s:
            if i.isupper():
                su.append(i)
            
            else:
                sl.append(i)
        
        su.sort()
        sl.sort()
        ans = ""
        j, k = 0, 0
        
        for i in range(len(s)):
            if s[i].isupper():
                ans += su[j]
                j += 1
            
            else:
                ans += sl[k]
                k += 1
        
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