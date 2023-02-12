from typing import Optional
import math
"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

You can also use the following for printing the link list.
printList(node)
"""

class Solution:
    def isPrime(self,x):
        if x<2:
            return False
        
        if x==2 or x==3:
            return True
        
        if x%2==0 or x%3==0:
            return False
        
        for i in range(5, int(math.sqrt(x))+1,6):
            if (x%i==0) or (x%(i+2)==0):
                return False
        
        return True

    def makePrime(self,x):
        if self.isPrime(x):
            return x
        
        if x == 1: 
            return 2
        
        else:
            for i in range(1,x):
                if self.isPrime(x-i):
                    return (x-i)
                
                elif self.isPrime(x+i):
                    return (x+i)
        
        return x
    
    def primeList(self, head : Optional['Node']) -> Optional['Node']:
        temp = head
        while temp!=None:
            temp.data = self.makePrime(temp.data)
            temp = temp.next
        
        return head
        



#{ 
 # Driver Code Starts
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

def printList(node):
    while (node != None):
        print(node.data,end=" ")
        node = node.next
    print()
def inputList():
    n=int(input())#lenght of link list
    data=[int(i) for i in input().strip().split()]#all data of linked list in a line
    head = Node(data[0])
    tail = head;
    for i in range(1,n):
        tail.next = Node(data[i]);
        tail = tail.next;
    return head;

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        head = inputList()
        
        obj = Solution()
        res = obj.primeList(head)
        
        printList(res)
        

# } Driver Code Ends