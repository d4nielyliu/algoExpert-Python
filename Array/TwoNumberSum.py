
def twoNumberSum(array, targetSum):
    # Write your code here.
    for i in range(len(array)-1):
        firstNum = array[i]
        for j in range(i+1, len(array)):
            secondNum =  array[j]
            twoNumSum = firstNum + array[j]
            if twoNumSum == targetSum:
               print([array[i], array[j]])
    print([])

def main():
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(twoNumberSum(array, targetSum))
    
    
main()
