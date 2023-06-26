#User function Template for python3

def reverseWord(s):
    if len(s) <= 1:
        return s
    
    return reverseWord(s[1:]) + s[0]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1

# } Driver Code Ends