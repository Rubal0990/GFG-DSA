#User function Template for python3

class Solution:
    def remove (self, s):
        news = ""
        n = len(s)
       
        while True:
            news = ""
            oldn = n
            s += "1"
            p1 = 0
           
            for i in range(1, n+1):
                if s[i] != s[i-1]:
                    p2 = i
                    if p2 - p1 <= 1:
                        news += s[i-1]
                    p1 = p2
                    
            n = len(news)
            
            if n == oldn:
                 return news
            
            s = news

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.remove(S))


# } Driver Code Ends