class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        number1 = 0
        number2 = 0
        length1 = len(num1)
        length2 = len(num2)
        stringToDigit = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9}
        digitToString = {0 : "0", 1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}

        for i in range(len(num1)):
            number1 += (10 ** (length1 - 1)) * stringToDigit[num1[i]]
            length1 -= 1 
        for i in range(len(num2)):
            number2 += (10 ** (length2 - 1)) * stringToDigit[num2[i]]
            length2 -= 1
        
        finalNumber = number1 * number2
        finalString = ""
        while finalNumber >= 0:
            digit = finalNumber % 10
            finalString += digitToString[digit]
            finalNumber = finalNumber // 10
            if finalNumber == 0:
                break
        return finalString[::-1]
                 