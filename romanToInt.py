class Solution(object):
    def romanToInt(self, s):
        result = 0
        values = []
        count = 0
        #convert the input string to numbers in an array
        for x in s:
            if x == 'I':
                values.append(1)               
            elif x == 'V':
                values.append(5)
            elif x == 'X':
                values.append(10)
            elif x == 'L':
                values.append(50)
            elif x == 'C':
                values.append(100)
            elif x == 'D':
                values.append(500)
            elif x == 'M':
                values.append(1000)
        #convert number array to integer
        max = len(values)
        while (count < max):
            if((count != (max - 1)) and (values[count] >= values[(count + 1)])):
                result = result + values[count]
                count = count + 1
            elif((count != (max - 1)) and (values[count] < values[(count + 1)])):
                result = result + ((values[count + 1]) - values[count])
                count = count + 2
            else:
                result = result + values[count]
                count = count + 1
        return result
