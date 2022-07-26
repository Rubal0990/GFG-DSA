# your task is to complete this function
# function should return an integer
'''
class node:
    def __init__(self):
        self.data = None
        self.next = Non
'''
class Solution:
    def maxPalindrome(self,head):
        arr = [head.data]
        qe = []
        qo = []
        m = 1
        x = 0
        node = head.next
        
        while node:
            x+= 1
            arr+= [node.data]
            for y in qe:
                if 2 * y < x + 1 or arr[2 * y - x - 1]!=arr[x]:
                    qe.remove(y)
                    continue
                if m < 2 * (x - y) + 2:
                    m = 2 * (x - y) + 2
            
            for y in qo:
                if 2 * y < x or arr[2 * y - x]!=arr[x]:
                    qo.remove(y)
                    continue
                if m < 2 * (x - y) + 1:
                    m = 2 * (x - y) + 1
            
            if arr[x]==arr[x - 1]:
                qe+= [x]
                if m==1:
                    m = 2
            
            if x > 1 and arr[x]==arr[x - 2]:
                qo+= [x - 1]
                if m < 3:
                    m = 3
            
            node = node.next
        
        return m



#{ 
 # Driver Code Starts
# Node Class
class node:
    def __init__(self):
        self.data = None
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        obj=Solution()
        print(obj.maxPalindrome(list1.head))
# Contributed By: Harshit Sidhwa

# } Driver Code Ends