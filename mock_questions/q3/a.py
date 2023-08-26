def mergeSortedList(head1, head2):
    d = Node()
    cur = d
    
    while head1 and head2:
        if head1.data < head2.data:
            cur.next = head1
            head1 = head1.next
        else:
            cur.next = head2
            head2 = head2.next
        cur = cur.next
    if head1:
        cur.next = head1 
    if head2:
        cur.next = head2
    return d.next
    