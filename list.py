def llist(head,val):
    for i reversed(head):
        if i==val:
            head.pop(head[i])
            print(head)
llist([1,2,3,4,5,6],4)
