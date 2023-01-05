#User function Template for python3

class Solution():
    def longestString(self, arr, n):
        hash = set(arr)
        res = ""
        for i in range(len(arr)):
            have = True
            for j in range(len(arr[i])):
                if arr[i][0:j+1] not in hash:
                    have = False
                    break
            
            if have:
                if len(res) < len(arr[i]):
                    res = arr[i]
                
                elif len(res) == len(arr[i]):
                    if arr[i] < res:
                        res = arr[i]
        
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [i for i in input().split()]
        print(Solution().longestString(arr,n))
# } Driver Code Ends