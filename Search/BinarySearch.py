def binarySearch(array, target):
    # Write your code here.
	low = 0
	high = len(array)-1
	while low <= high:
		mid = (low+high)//2
		if target == array[mid]:
			return mid
		elif target < array[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return -1
    pass

