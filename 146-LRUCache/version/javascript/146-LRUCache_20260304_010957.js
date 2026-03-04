// Last updated: 3/4/2026, 1:09:57 AM
// O(1) TIME COMPLEXITY
1class LRUCache {
2    constructor(capacity) {
3        this.capacity = capacity
4        this.map = new Map()
5
6        //dummy nodes
7        this.head = { key: 0, value: 0, next: null, prev: null }
8        this.tail = { key: 0, value: 0, next: null, prev: null }
9
10        //connect dummy nodes
11        this.head.next = this.tail
12        this.tail.prev = this.head
13
14    }
15    removeNode(node) {
16        node.prev.next = node.next
17        node.next.prev = node.prev
18    }
19
20    addToNode(node) {
21        node.next = this.head.next
22        node.prev = this.head
23        this.head.next.prev = node
24        this.head.next = node
25    }
26    get(key) {
27        if (!this.map.has(key)) return -1
28        const node = this.map.get(key)
29        this.removeNode(node)
30        this.addToNode(node)
31        return node.value
32    }
33    put(key, value) {
34        // if key exists
35        if (this.map.has(key)) {
36            const node = this.map.get(key)
37            node.value = value
38            this.removeNode(node)
39            this.addToNode(node)
40        } else {
41            if (this.map.size === this.capacity) {
42                const lru = this.tail.prev
43                this.removeNode(lru)
44                this.map.delete(lru.key)
45            }
46            const newNode = {
47                key: key,
48                value: value,
49                head: null,
50                tail: null
51            }
52            this.addToNode(newNode)
53            this.map.set(key, newNode)
54        }
55    }
56}