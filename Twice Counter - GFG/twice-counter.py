#User function Template for python3

class Solution:
    def countWords(self,List, n):
        s = list(set(List))
        count = 0
        
        for i in range(len(s)):
            if List.count(s[i]) == 2:
                count += 1
        
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        List = input().split()
        ob = Solution()
        print(ob.countWords(List, n))
# } Driver Code Ends