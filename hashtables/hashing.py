

def insert_with_double_hashing(arr, h_1, h_2):
	for i in range(len(arr)):
		index = (h_1 + i * h_2) % len(arr)
		if arr[index] is None:
			return index

def insert_with_linear_hashing(arr, h):
	for i in range(len(arr)):
		index = (h + i) % len(arr)
		if arr[index] is None:
			return index

# h_1 = 2
# for h_2 in range(1, 7):
#     location = insert_with_double_hashing([33, None, 27, 32, 55, None, 47], h_1, h_2)
#     print(f'{h_1 = }, {h_2 = }, {location = }')


for h in range(0, 7):
    location = insert_with_linear_hashing([33, None, 27, 32, 55, None, 47], h)
    print(f'{h = }, {location = }')

