#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        dic = {}
        for ele in words:
            arr = [0] * 26
            for gle in ele:
                a = ord(gle) - 97
                arr[a] += 1
            
            ar = tuple(arr)
            if ar in dic:
                dic[ar].append(ele)
            else:
                dic[ar] = [ele]
        
        return dic.values()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends