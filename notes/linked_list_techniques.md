# Linked list techniques

## Common routines
Be familiar with the following routines because many linked list questions make use of one or more of these routines in the solution:
- Counting the number of nodes in the linked list
- Reversing a linked list in-place
- Finding the middle node of the linked list using two pointers (fast/slow)
- Merging two linked lists together

## Techniques
### Sentinel/dummy nodes
- Adding a sentinel/dummy node at the head and/or tail might help to handle many edge cases where operations have to be performed at the head or the tail. The presence of dummy nodes essentially ensures that operations will never be done on the head or the tail, thereby removing a lot of headache in writing conditional checks to dealing with null pointers. Be sure to remember to remove them at the end of the operation.

### Two pointers
Two pointer approaches are also common for linked lists. This approach is used for many classic linked list problems.

- Getting the kth from last node - Have two pointers, where one is k nodes ahead of the other. When the node ahead reaches the end, the other node is k nodes behind
- Detecting cycles - Have two pointers, where one pointer increments twice as much as the other, if the two pointers meet, means that there is a cycle
- Getting the middle node - Have two pointers, where one pointer increments twice as much as the other. When the faster node reaches the end of the list, the slower node will be at the middle

#### slow fast tip
- if odd then fast = NULL , if even then fast = NODE if not cycle at END
- while fast and fast.next
- slow = fast = ListNode()
- slow.next = head
- slow = slow.next
- fast = fast.next.next