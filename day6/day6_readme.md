Problem Statement: Linked List implementation

```
Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3
```

Technique Used: Linked List

Approach:

We start by declaring `Node()` class and the constructor. We use `temp` Node throughout to traverse the Linked List. The functions were created accordingly, as requested.

Performance:

Time Complexity: 34ms
Space Complexity: 24.73MB

Note: These performances are tracked on online compiler and can vary.
