def isPalindrome(string):
    # Write your code here.
    mirrorStr = ""
    for i in reversed(range(len(string))):
        mirrorStr = mirrorStr + string[i]
        return mirrorStr == string
 

