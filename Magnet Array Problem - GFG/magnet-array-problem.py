#User function Template for python3

class Solution:
    def nullPoints(self, n, a, getAnswer):
        for i in range(n - 1):
            lo = a[i]
            hi = a[i + 1]
            
            while round(lo, 2) != round(hi, 2):
                mid = (lo + hi) / 2
                force = sum(1 / (x - mid) for x in a)
                if force == 0:
                    lo = mid
                    break
                elif force < 0:
                    lo = mid
                else:
                    hi = mid
            
            getAnswer[i] = round(lo, 2)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        getAnswer = [0]*n
        ob=Solution()
        ob.nullPoints(n, a, getAnswer)
        
        for i in range(0,n-1):
            print("{:.2f}".format(getAnswer[i]), end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends