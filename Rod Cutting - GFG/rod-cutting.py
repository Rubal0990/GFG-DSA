#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        arr = [0] * (n+1)
        arr[1] = price[0]
        
        for i in range(2, n+1):
            m = 0
            for j in range(1, i):
                m = max(m, arr[j] + arr[i-j])
            
            m = max(m, price[i-1])
            arr[i] = m
        
        return arr[-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
