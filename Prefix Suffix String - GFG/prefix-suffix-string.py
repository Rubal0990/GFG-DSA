#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Node:
    def __init__(self):
        self.nod = dict()

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, val):
        tem = self.root
        for i in val:
            if i not in tem.nod:
                tem.nod[i] = Node()
            
            tem = tem.nod[i]
    
    def search(self, val):
        tem = self.root
        for i in val:
            if i not in tem.nod:
                return False
            
            tem = tem.nod[i]
        
        return True   

class Solution:
    def prefixSuffixString(self, s1, s2) -> int:
        root1 = Trie()
        root2 = Trie()
        for word in s1:
            root1.insert(word)
            root2.insert(word[::-1])
        
        ans = 0
        for word in s2:
            if root1.search(word) or root2.search(word[::-1]):
                ans += 1
        
        return ans 
    
    

#{ 
 # Driver Code Starts.

if __name__=="__main__":
    for _ in range(int(input())):
        s1 = list(map(str, input().split()))
        s2 = list(map(str, input().split()))
        obj=Solution()
        print(obj.prefixSuffixString(s1, s2))
# } Driver Code Ends