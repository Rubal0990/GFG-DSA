#Back-end complete function Template for Python 3

class Solution:
    def maxSubStr(self, str):
        count0 = 0
        count1 = 0
        cnt = 0
        
        for i in str:
            if i == '0':
                count0 += 1
            elif i == '1':
                count1 += 1
            
            if count0 == count1:
                cnt += 1
        
        if count0 != count1:
            return -1
        
        return cnt



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        obj=Solution()
        ans=obj.maxSubStr(s)
        print(ans)
# } Driver Code Ends