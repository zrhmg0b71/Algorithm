A = list()
sum = 0

for i in range(5):
    A.append(int(input()))
    sum += A[i]

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged_arr = []

    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
    merged_arr += left[l:]
    merged_arr += right[r:]
    return merged_arr

print(sum // 5)
sorted_arr = merge_sort(A)
print(sorted_arr[2])