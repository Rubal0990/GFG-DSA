#User function Template for python3

class Solution():
    def lexicographicallyLargest(self, a, n):
        i = 0
        j = 1
        
        while i < n - 1 and j < n:
            if (a[i] + a[j]) % 2 == 0:
                j += 1
            
            else:
                a[i:j] = sorted(a[i:j], reverse=True)
                i = j
                j += 1 
        
        if j == n:   
            a[i:j] = sorted(a[i:j], reverse=True)
        
        return a


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        ans = Solution().lexicographicallyLargest(a, n)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends