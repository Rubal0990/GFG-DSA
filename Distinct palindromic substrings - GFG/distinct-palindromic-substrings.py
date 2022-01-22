#User function Template for python3

class Solution:
    def palindromeSubStrs(self, Str):
        palindromes = set()
        #Loop through each index
        for i in range(len(Str)):
            #find all odd length substring palindrome with s[i] as mid point
            self.find(Str, i, i, palindromes)
           
            #find all even length substring palindrome with s[i] and s[i+1] as mid point
            self.find(Str, i, i+1, palindromes)
       
        return len(palindromes)
           
       
    def find(self,Str,low,high,palindromes):
        while(low>=0 and high<=len(Str)-1 and Str[low]==Str[high]):
            #add palindrome to set
            palindromes.add(Str[low:high+1])
           
            #expand in both directions
            low = low-1
            high = high+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.palindromeSubStrs(Str))
# } Driver Code Ends