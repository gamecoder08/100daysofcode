Problem Statement: Given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

```
Example:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

```

Technique Used: Linked List

Approach:

We start by checking if any of the list is empty or `NULL`. If yes, we directly return the other list. We start by creating a dummy node() and a new `head`, to become the head and also track the latest node of the new linked list. We create two new temp nodes, `temp1` and `temp2`, for traversal in each list. We start a `while()` loop until both of the lists are not `NULL`. We compare the values. If `temp1->val` is `<=` to `temp2->val`. We add `temp1` to `head` and move `temp1` to next node. `Else`, we add `temp2` to `head`, and move `temp2` to next node. We then move head to the latest node, so that future nodes can be added easily. After the `while()` loop exits. We check if any of the lists are remaining, if yes we directly merge them to the `head`. We then move `head` pointer to `dummy->next`, and delete `dummy` node. Then, we simply return `head`.

Performance:

Time Complexity: 0ms
Space Complexity: 19.69MB

Note: These performances are tracked on online compiler and can vary.
