// Leetcode Solution:

// class MyHashMap {

// private:
//     const int SIZE = 1000;

//     int hash(int key)
//     {
//         return key % SIZE;
//     }

//     vector<list<pair<int,int>>> hashTable;

// public:
//     MyHashMap() {
//         hashTable.resize(SIZE);
//     }

//     void put(int key, int value) {
//         int index = hash(key);
//         for( auto& kv : hashTable[index])
//         {
//             if(kv.first==key)
//             {
//                 kv.second=value;
//                 return;
//             }
//         }
//         hashTable[index].push_back({key,value});
//     }

//     int get(int key) {
//         int index = hash(key);
//         for(auto& kv : hashTable[index])
//         {
//             if(kv.first==key)
//             {
//                 return kv.second;
//             }
//         }
//         return -1;
//     }

//     void remove(int key) {
//         int index = hash(key);
//         for(auto it = hashTable[index].begin(); it !=hashTable[index].end();++it)
//         {
//             if(it->first==key)
//             {
//                 hashTable[index].erase(it);
//                 return;
//             }
//         }
//     }
// };