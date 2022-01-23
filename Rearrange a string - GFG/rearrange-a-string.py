#User function Template for python3

class Solution:
    def arrangeString(self, s):
        sum_of_num = 0
        alphabet = []
        
        for char in s:
            if char.isdigit():
                sum_of_num += int(char)
            else:
                alphabet.append(char)
        
        return "".join(sorted(alphabet)) + str(sum_of_num)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.arrangeString(s)
        print(ans)
# } Driver Code Ends