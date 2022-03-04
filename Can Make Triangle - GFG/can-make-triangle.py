#User function Template for python3
class Solution:
    def Is_Triangle(self, A):
        return all(A) and all(2 * side < sum(A) for side in A)

    def canMakeTriangle(self, A, N):
        result = []
        
        for i in range(0, N - 2):
            if(self.Is_Triangle(A[i:i + 3])):
                result.append(1)
            else:
                result.append(0)
        
        return result


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.canMakeTriangle(A, N)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends