#User function Template for python3

import heapq

class custom_object:
    def __init__(self,node):
        self.node = node
        self.val = self.node.data
        self.next = self.node.next
    
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,K):
        result = []
        for i in range(K):
            result.append(custom_object(arr[i]))
            
        heapq.heapify(result)
        dummy = Node(-1)
        head = dummy
        
        while result:
            op = heapq.heappop(result)
            dummy.next = Node(op.val)
            dummy = dummy.next
            
            if op.next:
                heapq.heappush(result,custom_object(op.next))
        
        return head.next

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add(self,x):
        if self.head is None:
            self.head=Node(x)
            self.tail=self.head
        else:
            self.tail.next=Node(x)
            self.tail=self.tail.next
    
def printList(head):
    walk = head
    while walk:
        print(walk.data, end=' ')
        walk=walk.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        line=[int(x) for x in input().strip().split()]
        
        heads=[]
        index=0
        
        for i in range(n):
            size=line[index]
            index+=1
            
            newList = LinkedList()
            
            for _ in range(size):
                newList.add(line[index])
                index+=1
            
            heads.append(newList.head)
        
        merged_list = Solution().mergeKLists(heads,n)
        printList(merged_list)

# } Driver Code Ends