#User function Template for python3

class Solution:
    def countnodes(self, head):
        if head == None:
            return 0
        
        else:
            listofvalues = []
            temp = head
            while temp != None:
                listofvalues.append(temp.data)
                temp = temp.next
            
            return listofvalues
    
    def modify_the_list(self, head):
        vals = self.countnodes(head)
        n = len(vals)
        temp = head
        for i in range(n//2):
            temp.data = vals[n - i - 1] - vals[i]
            temp = temp.next
        
        if n % 2 == 1:
            n -= 1
            temp = temp.next
        
        for i in range(n//2):
            temp.data = vals[n//2 - i - 1]
            temp = temp.next
        
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def modify_the_list(head):
    current = head
    while current is not None:
        if current.next is not None and current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


t = int(input())
while t > 0:
    n = int(input())
    linked_list_arr = list(map(int, input().split()))
    head = None
    temp = None
    for a in linked_list_arr:
        new_node = Node(a)
        if head is None:
            head = new_node
        else:
            temp.next = new_node
        temp = new_node
    head = Solution().modify_the_list(head)
    print_list(head)
    t -= 1
# } Driver Code Ends