calibrationValues = []
calibrationSum = 0

nums = [*"0123456789"]
numsSpelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getInput():
    f = open("input.txt", 'r')
    input = f.read().splitlines()
    f.close()
    return input

def wordtonum(input):
    output = []
    for item in input:
        tmpvar = item
        for num in numsSpelled:
            if num in item:
                item = item.replace(num, str(numsSpelled.index(num) + 1))
                print("replaced something " + item + " " + num + " " + str(numsSpelled.index(num) + 1))
        output.append(item)
    return output
 
def main():
    print
    input = getInput()
    
    input = wordtonum(input)
    
    print("Input: (scrabled data)")
    print(input)
    for line in input:
        firstDone = False
        vals = []
        chars = [*line]
        for item in chars:
            if item in nums:
                vals.append(item)
        
        calibrationValues.append(int(vals[0] + vals[len(vals) - 1]))

    print("\n\nValues stripped from scrabled data:")
    print(calibrationValues)
    
    calibrationSum = sum(calibrationValues)

    print("\n\nCalibrationValue:")
    print(calibrationSum)

main()
