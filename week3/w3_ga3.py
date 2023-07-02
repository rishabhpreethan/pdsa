# Reverse a linked list

def reverse(root):
    prev = None
    cur = root
    
    while cur is not None:
        n = cur.next
        cur.next = prev
        prev = cur
        cur = n
    return prev