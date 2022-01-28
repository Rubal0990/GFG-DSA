#User function Template for python3

class Solution:
    def lookandsay(self, n):
        if (n == 1):
            return "1"
        if (n == 2):
            return "11"
     
        s = "11"
        for i in range(3, n + 1):
            s += '$'
            l = len(s)
            
            cnt = 1 
            tmp = ""
     
            for j in range(1 , l):
                if (s[j] != s[j - 1]):
                    tmp += str(cnt + 0)
                    tmp += s[j - 1]
                    cnt = 1
                else:
                    cnt += 1
                    
            s = tmp
            
        return s;

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.lookandsay(n))

# } Driver Code Ends