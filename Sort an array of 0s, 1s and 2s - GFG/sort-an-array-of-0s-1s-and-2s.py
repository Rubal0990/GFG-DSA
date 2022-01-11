#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        count0 = 0
        count1 = 0
        count2 = 0
        for i in range(0,n):
            if (arr[i] == 0):
                count0=count0+1
            if (arr[i] == 1):
                count1=count1+1
            if (arr[i] == 2):
                count2=count2+1
         
     
        # Putting the 0's in the array in starting.
        for i in range(0,count0):
            arr[i] = 0
         
        # Putting the 1's in the array after the 0's.
        for i in range( count0, (count0 + count1)) :
            arr[i] = 1
         
        # Putting the 2's in the array after the 1's
        for i in range((count0 + count1),n) :
            arr[i] = 2


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends