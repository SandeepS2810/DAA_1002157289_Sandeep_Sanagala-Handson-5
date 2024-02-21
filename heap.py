import timeit
import random

class Build_Heap:
    def __init__(self):
        self.heap = []

    def Build_Min_Heap(self, arr):
        self.heap = arr
        l = len(arr)
        for i in range(l // 2 - 1, -1, -1):
            self.Heapify(i)

    def Heapify(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        s = i

        if left < len(self.heap) and self.heap[left] < self.heap[s]:
            s = left

        if right < len(self.heap) and self.heap[right] < self.heap[s]:
            s = right

        if s != i:
            self.heap[i], self.heap[s] = self.heap[s], self.heap[i]
            self.Heapify(s)

    def push(self, val):
        self.heap.append(val)
        ix = len(self.heap) - 1

        while ix > 0:
            par_ix = (ix - 1) // 2
            if self.heap[par_ix] > self.heap[ix]:
                self.heap[par_ix], self.heap[ix] = self.heap[ix], self.heap[par_ix]
                ix = par_ix
            else:
                break

    def pop(self):
        if not self.heap:
            return None

        root = self.heap[0]
        last = self.heap.pop()
        
        if self.heap:
            self.heap[0] = last
            self.Heapify(0)

        return root


# Taking user inputs for initial values
arr = list(map(int, input("Enter the values separated by space: ").split()))

# Building and printing the initial heap
heap = Build_Heap()
heap.Build_Min_Heap(arr)
print("Initial Heap:", heap.heap)

# Taking user input for the number to push
num = int(input("Enter the number for performing push operation: "))
heap.push(num)
print("Heap after push operation:", heap.heap)

# Pop the root node and print the heap after performing pop operation
root = heap.pop()
print("Popped root:", root)
print("Heap after pop operation:", heap.heap)

# Function to benchmark the heap operations
def benchmark_heap_operations():
    heap = Build_Heap()
    data = [random.randint(1, 1000) for _ in range(1000)]

    
    heap.Build_Min_Heap(data)

    # Push new numbers to the heap
    for _ in range(100):
        heap.push(random.randint(1, 1000))

    # perform pop operation from the heap
    for _ in range(100):
        heap.pop()

# Measure the execution time
execution_time = timeit.timeit(benchmark_heap_operations, number=1000)
print(f"Total Execution Time: {execution_time} seconds")


'''System Specifications:

CPU: 

8-core CPU with 4 performance cores and 4 efficiency cores, 8-core GPU, 16-core Neural Engine, 100GB/s memory bandwidth.

RAM:

8.0GB.

Operating System:

MacOs.
'''