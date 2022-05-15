#User function Template for python3

class Solution:
    def subsetsHelper (self, arr, i, n, cur, res):
        if i >= n:
            res.append (cur[:])
            return
        
        curInd = i + 1
        while curInd < n and arr[curInd] == arr[i]:
            curInd += 1
            
        count = curInd - i
        for j in range (0, count+1):
            for k in range (j):
                cur.append (arr[i])  
            self.subsetsHelper (arr, curInd, n, cur, res)
            for k in range (j):
                cur.pop ()
    def AllSubsets (self, arr, n):
        
        res = []
        cur = []
        arr.sort()
        
        self.subsetsHelper (arr, 0, n, cur, res)
        res.sort ()
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        obj  = Solution()
        result = obj.AllSubsets(a,n)
        for i in range(len(result)):
            print("(",end="")
            size = len(result[i])
            for j in range(size-1):
                print(result[i][j],end=" ")
            if(size):
                print(result[i][size-1],end=")")
            else:
                print(")",end="")
        print()


# } Driver Code Ends