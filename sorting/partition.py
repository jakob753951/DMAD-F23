def partition(arr: list, start_index: int, end_index: int) -> list:
	arr = arr.copy()
	pivot = arr[start_index]
	less_than_pivot = []
	greater_than_pivot = []
	for i in range(start_index + 1, end_index + 1):
		if arr[i] <= pivot:
			less_than_pivot.append(arr[i])
		else:
			greater_than_pivot.append(arr[i])

	arr[start_index:end_index + 1] = less_than_pivot + [pivot] + greater_than_pivot
	return arr


l = [21, 17, 28, 14, 9, 18, 6, 1, 26, 15, 30, 7, 13, 19, 2]
new_l = partition(l, start_index=3, end_index=12)

print(l)
print(new_l)