Problem Statement: To design a HashSet without using any built-in hash table libraries. Implement MyHashSet class

```
Example:

Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)

```

Technique Used: HashSet, Vector

Approach:

To design a hashset, we start by private initialising a const SIZE of 1001 which would be no. of buckets in hashset. Then, we create a private function `hash()`, which takes the `key` and return `index % SIZE`, making sure index always falls in the range of buckets. In public, we initialise a nested `list` vector, `hashVec`, which would serve as our hashset. A hashset has buckets serving as index which store unique `key-value` pairs. So, we use `.resize()` function, to adjust the no. of buckets as required. Now, we declare `contains()` function. It takes `key` as input and runs through the `index` list of the vector `hashVec`. If we find `key` exists in the list, we return `true`, else we return `false` after the loop. Also, we create a `add()` function. It check if the key exists or not using `contains()` function, if it does, we return. If it does not, we calculate index using `hash()` function, and store the key on that index in `hashVec`. Similarly, we create a `remove()` function. It checks if `key` exists or not, if it does not, we return. Else, we calculate index of `key` and remove it from `hashVec` using `.remove()` function.

Performance:

Time Complexity: 11ms
Space Complexity: 46.83MB

Note: These performances are tracked on online compiler and can vary.
