#User function Template for python3

class Solution:
    def extendPalindrome(self, S, low, high, length):
        while low >= 0 and high < length:
           
            if S[low] == S[high]:
                low -= 1
                high += 1
            else:
                break
            
        return (high-low-1);
       
    def longestPalin(self, S):
        lenS = len(S)
        vMaxLength = 1
        vCurrLength =- 1
        vTup = (0, 0)

        for i in range(0, lenS, 1):
            vCurrLength = self.extendPalindrome(S, i, i, lenS)
            if vCurrLength > vMaxLength:
                vMaxLength = vCurrLength
                vTup = ((i - (vCurrLength // 2)), (i + (vCurrLength // 2)))
        
        for i in range(0, lenS, 1):
            vCurrLength = self.extendPalindrome(S, i, i+1, lenS)
            if vCurrLength > vMaxLength:
                vMaxLength = vCurrLength
                vTup =  ((i - (vCurrLength // 2) + 1), (i + (vCurrLength // 2)))
               
        vOut = S[vTup[0]:vTup[1] + 1]
        return vOut
       

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
# } Driver Code Ends