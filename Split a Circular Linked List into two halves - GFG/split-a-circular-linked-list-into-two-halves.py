#User function Template for python3

'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def splitList(self, head, head1, head2):
        if not head:
            return None
       
        fast, slow = head, head
        while fast.next.next != head and fast.next != head:
            slow = slow.next
            fast = fast.next.next
           
        head2 = slow.next
        if fast.next == head:
            fast.next = head2
        else:
            fast.next.next = head2
       
        head1 = head
        slow.next = head
        return head1, head2


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:
    def __init__(self):
        self.data = None
        self.next = None

def printCircularLinkedList(head):
    tmp = head
    while True:
        print(tmp.data, end = " ")
        tmp = tmp.next
        if tmp == head:
            break
    print()
    
if __name__ == "__main__":
    for i in range(int(input())):
        head = Node()
        head1 = Node()
        head2 = Node()
        tmp = head
        n = int(input())
        for i in input().split():
            tmp.next = Node()
            tmp = tmp.next
            tmp.data = int(i)
        head = head.next
        tmp.next = head
        obj = Solution()
        head1,head2 = obj.splitList(head,head1,head2)
        printCircularLinkedList(head1)
        printCircularLinkedList(head2)


# } Driver Code Ends