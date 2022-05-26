#User function Template for python3

class Solution:
    def reArrange(self, arr, n):
        newArr1 = [0]*(N//2)
        newArr2 = [0]*(N//2)
        count = count1 = count2 = 0
        
        for i in arr:
            if i%2 == 0:
                newArr1[count1] = i
                count1 += 1
            else:
                newArr2[count2] = i
                count2 += 1
                
        for i in range(0, n-1, 2):
            arr[i] = newArr1[count]
            arr[i+1] = newArr2[count]
            count += 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def check(arr, n):
    flag = 1
    c=d=0
    for i in range(n):
        if i%2==0:
            if arr[i]%2:
                flag = 0
                break
            else:
                c+=1
        else:
            if arr[i]%2==0:
                flag = 0
                break
            else:
                d+=1
    if c!=d:
        flag = 0
            
    return flag
        
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ob.reArrange(arr,N)
        
        print(check(arr,N))

# } Driver Code Ends