import time
import random
from collections import deque
import heapq

# Timer utility
def time_operation(func, *args, repeats=5):
    times = []
    for _ in range(repeats):
        start = time.time()
        func(*args)
        end = time.time()
        times.append(end - start)
    avg = sum(times) / repeats
    return avg

# Stack operations using list
def stack_push(stack, values):
    for val in values:
        stack.append(val)

def stack_pop(stack, count):
    for _ in range(count):
        if stack:
            stack.pop()

def stack_peek(stack):
    return stack[-1] if stack else None

# Queue operations using deque
def queue_enqueue(queue, values):
    for val in values:
        queue.append(val)

def queue_dequeue(queue, count):
    for _ in range(count):
        if queue:
            queue.popleft()

def queue_peek(queue):
    return queue[0] if queue else None

# Priority Queue operations using heapq
def pq_push(pq, values):
    for val in values:
        heapq.heappush(pq, val)

def pq_pop(pq, count):
    for _ in range(count):
        if pq:
            heapq.heappop(pq)

def pq_peek(pq):
    return pq[0] if pq else None

def main():
    size = 100000
    values = [random.randint(1, 10**6) for _ in range(size)]

    print(f"Benchmarking with {size} values")

    # Stack benchmark
    stack = []
    t_push = time_operation(stack_push, stack, values)
    t_peek = time_operation(stack_peek, stack)
    t_pop = time_operation(stack_pop, stack, size)
    print(f"Stack (list) Push: {t_push:.6f} s")
    print(f"Stack (list) Peek: {t_peek:.6f} s")
    print(f"Stack (list) Pop: {t_pop:.6f} s")

    # Queue benchmark
    queue = deque()
    t_enqueue = time_operation(queue_enqueue, queue, values)
    t_peek = time_operation(queue_peek, queue)
    t_dequeue = time_operation(queue_dequeue, queue, size)
    print(f"Queue (deque) Enqueue: {t_enqueue:.6f} s")
    print(f"Queue (deque) Peek: {t_peek:.6f} s")
    print(f"Queue (deque) Dequeue: {t_dequeue:.6f} s")

    # Priority Queue benchmark
    pq = []
    t_push = time_operation(pq_push, pq, values)
    t_peek = time_operation(pq_peek, pq)
    t_pop = time_operation(pq_pop, pq, size)
    print(f"Priority Queue (heapq) Push: {t_push:.6f} s")
    print(f"Priority Queue (heapq) Peek: {t_peek:.6f} s")
    print(f"Priority Queue (heapq) Pop: {t_pop:.6f} s")

if __name__ == "__main__":
    main()
