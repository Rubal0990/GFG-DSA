def countRev(s):
    lenn = len(s)
    stk = []
    
    if lenn%2 != 0:
        return -1
    
    for i in range(lenn):
        if s[i] == '}' and len(stk):
            if stk[0] == '{':
                stk.pop(0)
            else:
                stk.insert(0, s[i])
            
        else:
            stk.insert(0, s[i])

    red_len = len(stk)
    n = 0
    while (len(stk)and stk[0] == '{'):
        stk.pop(0)
        n += 1

    return (red_len // 2 + n % 2)


#{ 
 # Driver Code Starts

t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends
