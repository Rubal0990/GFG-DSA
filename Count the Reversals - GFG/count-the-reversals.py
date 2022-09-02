def countRev(s):
    ans = 0
    right = 0
    
    for i in s:
        if i == "{":
            right += 1
        
        else:
            if right != 0:
                right -= 1
            
            else:
                ans += 1
                right += 1

    if right%2 != 0:
        return -1
    else:
        ans += right // 2
        return ans


#{ 
 # Driver Code Starts

t = int (input ())
for tc in range (t):
    s = input ()
    print (countRev (s))

# Contributed By: Pranay Bansal

# } Driver Code Ends