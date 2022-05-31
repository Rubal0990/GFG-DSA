class Solution:
    def smallestSubWithSum(self, a, n, x):
        index = n+1
        sums = 0
        start, end = 0, 0
        
        while end < n:
            while sums <= x and end < n:
                sums += a[end]
                end += 1
               
            while sums > x and start < n:
                if end - start < index:
                    index = end - start
                sums -= a[start]
                start += 1
               
        return index 
        


#{ 
#  Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends