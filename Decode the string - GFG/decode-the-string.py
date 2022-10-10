#User function Template for python3

class Solution:
    def decodedString(self, s):
        integerstack = []
        stringstack = []
        temp = ""
        result = ""
        i = 0
        while i < len(s):
            count = 0
            if s[i] >= "0" and s[i] <= "9":
                while s[i] >= "0" and s[i] <= "9":
                    count = count * 10 + ord(s[i])-ord("0")
                    i += 1
                
                i -= 1
                integerstack.append(count)
            
            elif s[i] == "]":
                temp = ""
                count = 0
                if (integerstack):
                    count = integerstack.pop()
                while stringstack and stringstack[-1] != "[":
                    temp = stringstack.pop() + temp
                
                if stringstack and stringstack[-1] == '[':
                    stringstack.pop()
                
                for j in range(count):
                    result += temp
                
                for j in range(len(result)):
                    stringstack.append(result[j])
                
                result = ""
            
            elif s[i] == "[":
                if s[i-1] >= "0" and s[i-1] <= "9":
                    stringstack.append(s[i])
                
                else:
                    stringstack.append(s[i])
                    integerstack.append(1)
            
            else :
                stringstack.append(s[i])
            
            i += 1
        
        while stringstack:
            result=stringstack.pop()+result
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends