def sortedSquaredArray(array):
    # Write your code here.
	squaredArray = []
	for i in range(len(array)):
		squaredArray.append(array[i]*array[i])
	squaredArray.sort()	
    return squaredArray
