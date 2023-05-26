# Queues (double ended queue)
"""
In dequeue we can append and pop from left side unlike array (stack) 
"""
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)            # O/P => deque([1, 2])

queue.popleft() 
print(queue)            # O/P => deque([2])

queue.appendleft(1)
print(queue)            # O/P => deque([1, 2])


queue.pop()
print(queue)            # O/P => deque([1])

