
class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []

        currentString = ""
        currentNum = 0

        for char in s:
            if char.isdigit():
                currentNum = currentNum * 10 + int(char)

            elif char == '[':
                countStack.append(currentNum)
                stringStack.append(currentString)

                currentNum = 0
                currentString = ""

            elif char == ']':
                k = countStack.pop()
                previousString = stringStack.pop()

                currentString = previousString + currentString * k

            else:
                currentString += char

        return currentString
