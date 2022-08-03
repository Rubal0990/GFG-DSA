#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.data = val
'''

class Solution():
    def rotateDLL(self, start, p):
        if p == 0: 
            return
        
        curr = start
        while p:
            curr = curr.next
            p -= 1
        
        tail = curr.prev
        NewHead = curr 
        tail.next = None
        curr.prev = None
  
        while curr.next: 
            curr = curr.next
  
        curr.next = start
        start.prev = curr 
        return NewHead 


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.data = val


if __name__ == "__main__":
    for _ in range(int(input())):
        
        n,p = map(int, input().split())
        start = None
        cur = None
        temp = [int(i) for i in input().split()]
        for i in range(n):
            a = temp[i]
            ptr=Node(a)
            ptr.data=a
            if(start==None):
                start=ptr
                cur=ptr
            else:
                cur.next=ptr
                ptr.prev=cur
                cur=ptr

        obj = Solution()
        str=obj.rotateDLL(start,p)
        while(1):
            print(str.data, end = " ")
            if str.next==None: break
            str=str.next
        
        while(str!=None):
            print(str.data, end = " ")
            str=str.prev
        
        print()
# } Driver Code Ends