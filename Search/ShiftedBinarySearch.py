def shiftedBinarySearch(array, target):
    # Write your code here.
	return shiftedBinarySearchHelper(array, target, 0, len(array)-1)

def shiftedBinarySearchHelper(array, target, lower, upper):
	while lower <= upper:
		mid = (lower+upper)//2
		lowerbound = array[lower]
		upperbound = array[upper]
		if target == array[mid]:
			return mid
		elif lowerbound <= array[mid]:
			if target < array[mid] and target >= lowerbound:
				upper = mid - 1
			else:
				lower = mid + 1
		else:
			if target > array[mid] and target <= upperbound:
				lower = mid + 1
			else:
				upper = mid -1
	return -1
	
