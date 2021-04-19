def isValidSubsequence(array, sequence):
    # Write your code here.
	i, j = 0, 0
    while i < len(array) and j < len(sequence):
		if array[i] == sequence[j]:
			j = j+1
		i = i + 1
	return j == len(sequence)
	
