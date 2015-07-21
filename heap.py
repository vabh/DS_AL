import random


class Heap:
    # arr = []

    def __init__(self, arr):
        self.arr = arr

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def max_heapify(self, arr, i):
        l = self.left(i)
        r = self.right(i)
        if l < len(arr) and arr[l] > arr[i]:
            largest = l
        else:
            largest = i

        if r < len(arr) and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.max_heapify(arr, largest)

    def min_heapify(self, arr, i):
        l = self.left(i)
        r = self.right(i)
        if l < len(arr) and arr[l] < arr[i]:
            smallest = l
        else:
            smallest = i

        if r < len(arr) and arr[r] < arr[smallest]:
            smallest = r

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.min_heapify(arr, smallest)

    def make_heap(self, arr):
        length = len(arr) - 1
        for i in range(length / 2, -1, -1):
            self.min_heapify(arr, i)

    def merge_klists(self, arr):

        n = 0
        for list in arr:
            n += len(list)

        '''
	    	add to heap (num, list_id)
	    	implement comprator for heap
	    '''

    def heap_sort(self, arr):
        self.make_heap(arr)
        for i in range(len(arr) - 1, -1, -1):
            print arr[0]
            arr[0] = arr[i]
            arr = arr[0:i]
            self.min_heapify(arr, 0)

arr = [random.randint(-10, 10) for i in range(0, 10)]
# print arr
# make_heap(arr)
# print arr

# arr = [sorted([random.randint(0, 10)
               # for i in range(0, random.randint(1, 5))]) for i in range(0, 5)]

print arr

x = Heap(arr)
x.heap_sort(arr)
print x.arr
# merge_klists(arr)
