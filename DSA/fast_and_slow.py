

def fs(head):
    slow = head
    fast = head
    circular = True

    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return circular
