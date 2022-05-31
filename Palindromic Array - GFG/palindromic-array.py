# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr, n):
    for num in arr:
        if num < 0 or (num%10 == 0 and num > 0):
            return 0
            
        rev = 0
        while num > rev:
            rev = rev*10 + num%10
            num //= 10
            
        if num == rev or (num == rev//10):
            continue
        else:
            return 0
        
    return 1


#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends