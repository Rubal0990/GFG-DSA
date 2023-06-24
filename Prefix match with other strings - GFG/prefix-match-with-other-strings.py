#User function Template for python3

class Solution:
    def klengthpref(self, arr, n, k, s):
        cnt = 0
        for i in arr:
            if len(i) >= k and s[0:k] == i[0:k]:
                    cnt += 1
        
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr = []
        for x in range(n):
            s1 = input()
            arr.append(s1)
        k = int(input())
        s = input()
        obj = Solution()
        print(obj.klengthpref(arr,n,k,s))
        
        
# } Driver Code Ends