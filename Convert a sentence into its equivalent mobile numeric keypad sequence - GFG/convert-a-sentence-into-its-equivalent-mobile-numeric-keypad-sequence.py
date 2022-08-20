#User function Template for python3

class Solution:
    def printSequence(self, S):
        output = ""
        nums = ["2", "22", "222",
                "3", "33", "333",
                "4", "44", "444",
                "5", "55", "555",
                "6", "66", "666",
                "7", "77", "777", "7777",
                "8", "88", "888",
                "9", "99", "999", "9999"]
        
        for i in range(len(S)):
            if(S[i] == ' '):
                output += "0"
            else:
                val = nums[ord(S[i]) - ord('A')]
                output += val
        
        return output



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        inputStr = input()

        solObj = Solution()

        print(solObj.printSequence(inputStr))
# } Driver Code Ends