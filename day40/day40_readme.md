Problem Statement: To design a HashMap without using any built-in hash table libraries. Implement the MyHashMap class

```
Example:

Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]

Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

```

Technique Used: HashMap, Vector

Approach:

To design a hashmap, we start by private initialising a const SIZE of 1000 which would be no. of buckets in hashset. Then, we create a private function `hash()`, which takes the `key` and return `index % SIZE`, making sure index always falls in the range of buckets. In public, we initialise a nested `list` vector, `hashTable`, which would serve as our hashmap structurised as vector with a list of pair of values `key, value`. A hashmap has buckets serving as index which store unique `key-value` pairs. So, we use `.resize()` function, to adjust the no. of buckets as required. Now, we declare `put()` function. It takes `key` as input and runs through the `index` list of the vector `hashTable`. If we find `key` exists in the list, we access the second element and assign the `value` to it. Also, we create a `get()` function. It check if the key exists or not using `for()` loop, if it does, we return the second value. If it does not, we return `-1`. Then, we create a `remove()` function. We calculate index of `key` and remove it from `hashTable` using `.erase()` function. Point to be noted, we use ranged `for()` loop for first two operations, but we use traditional `for()` loop for the third function. This is due to because we need an pointer iterator in order to remove the pair from the vector completely.

Performance:

Time Complexity: 18ms
Space Complexity: 59.20MB

Note: These performances are tracked on online compiler and can vary.
