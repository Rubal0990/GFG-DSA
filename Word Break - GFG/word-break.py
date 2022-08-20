#User function Template for python3

def wordBreak(s, wdict):
    dp = [False] * (len(s)+1)
    dp[len(s)] = True
    
    for i in range(len(s)-1, -1, -1):
        for v in wdict:
            if (i+len(v)<=len(s)) and (s[i:i+len(v)])==v:
                dp[i] = dp[i+len(v)]
            
            if dp[i]:
                break
    
    return dp[i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends