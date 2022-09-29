# Your task is to complete all these function's
# function should append an element on to the stack

def push(arr, ele):
    arr.insert(len(arr), ele)

# Function should pop an element from stack
def pop(arr):
    if len(arr):
        return arr.pop(-1)
    
    return -1

# function should return 1/0 or True/False
def isFull(n, arr):
    return len(arr) == n

# function should return 1/0 or True/False
def isEmpty(arr):
    return len(arr) == 0

# function should return minimum element from the stack
def getMin(n, arr):
    return min(arr)


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        while(not isEmpty(stack)):
            pop(stack)
            
        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
# contributed by: Harshit Sidhwa

# } Driver Code Ends