class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None

        prev, curr = None, head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
