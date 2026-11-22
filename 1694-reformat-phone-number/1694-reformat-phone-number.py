class Solution:
    def reformatNumber(self, number):
        number = number.replace(" ", "").replace("-", "")
        
        result = []
        i = 0
        
        while len(number) - i > 4:
            result.append(number[i:i+3])
            i += 3
        
        remaining = len(number) - i
        
        if remaining == 4:
            result.append(number[i:i+2])
            result.append(number[i+2:i+4])
        else:
            result.append(number[i:])
        
        return "-".join(result)