import random
import time


def merge(left, right, inversions=0):

    len_l = len(left)
    len_r = len(right)

    merged = [0 for i in range(0, len_l + len_r)]
    i = 0
    j = 0
    for k in range(0, len_l + len_r):

        if i < len_l and j < len_r:
            if left[i] < right[j]:
                merged[k] = left[i]
                i += 1
            else:
                merged[k] = right[j]
                j += 1
                inversions += len_l - i
        else:
            if i < len_l:
                merged[k] = left[i]
                i += 1
            elif j < len_r:
                merged[k] = right[j]
                j += 1

    return merged, inversions


def merge_sort(arr):

    l = len(arr)
    if l <= 1:
        # print type(arr)
        return arr, 0
    else:
        left, inversions_l = merge_sort(arr[0:l / 2])
        right, inversions_r = merge_sort(arr[l / 2:l])
        return merge(left, right, inversions_l + inversions_r)

left = [random.randint(-100, 100) for i in range(0, 5)]
right = [random.randint(-100, 100) for i in range(0, 5)]

arr = [random.randint(0, 100) for i in range(0, 10)]

left = sorted(left)
right = sorted(right)

arr = []
with open('inv.txt', 'r') as f:
    for line in f:
        num = int(line)
        arr.append(num)
arr1 = arr

t1 = time.time()
arr1 = sorted(arr1)
print time.time() - t1

# print arr
print
t1 = time.time()
merge_sort(arr)
print time.time() - t1
