'''
Given a characters array tasks, representing the tasks a CPU needs to do, 
where each letter represents a different task. Tasks could be done in any order. 
Each task is done in one unit of time. For each unit of time, 
the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks 
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.
Return the least number of units of times that the CPU will take to finish all the given tasks.


Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
'''

'''
Deque Concept:
from collections import deque
d = deque()
d = deque([1, 2, 3])
d.append(4)
d.appendleft(0)
popped_element = d.pop()
popped_element_left = d.popleft()
print(d)
element_at_index = d[2]
length = len(d)
is_empty = not bool(d)
# Rotate the deque to the right
d.rotate(1)
print("Rotate the deque to the right",d)
# Rotate the deque to the left
d.rotate(-1)
print("Rotate the deque to the left",d)
# Clear all elements from the deque
d.clear()
# Create a shallow copy of the deque
d_copy = d.copy()

Logic:
get counts
pop min element and add 1
check when to add the element into the heapq based on the time or n value
use deque to store time
check deque time condition and push into heap
iterate the process until heap and q is empty

import heapq
from collections import Counter, deque
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
count=Counter(tasks)
heapcount=[-i for i in count.values()]
heapq.heapify(heapcount)
print(heapcount)

time=0
q=deque()
while heapcount and q:
    time=time+1
    if heapcount:
        cnt=1+heapq.heappop(heapcount)
        if cnt:
            q.append([cnt,time+n])
    if q and q[0][1]==time:
        heapq.heappush(heapcount,q.popleft()[0])
'''



from ast import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        heapcount=[-i for i in count.values()]
        heapq.heapify(heapcount)

        time=0
        q=deque()
        while heapcount and q:
            time=time+1
            if heapcount:
                cnt=1+heapq.heappop(heapcount)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(heapcount,q.popleft()[0])
        return time
