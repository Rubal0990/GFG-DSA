#User function Template for python3

class Solution:
    def LCP(self,arr,n):
        s = ""
        p1 = 10000
        p = ""
    
        for i in arr:
            if len(i) < p1:
                p = i
                p1 = len(p)
    
        for i in p:
            c = 0
            for j in range(n):
                if arr[j][0][0] == i:
                    arr[j] = arr[j][1:]
                    c += 1
                    continue
                else:
                    break
                
            if c < n:
                break
            s += i
    
        if s == "":
            return -1
    
        return s 

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tcs =int(input())
    for _ in range(tcs):
        n=int(input())
        arr=[ x  for x in input().split()]
        obj=Solution()
        print(obj.LCP(arr,n))
# } Driver Code Ends