calibrationValues = []
calibrationSum = 0

nums = [*"0123456789"]

def getInput():
    f = open("input.txt", 'r')
    input = f.read().splitlines()
    f.close()
    return input
 
def main():
    print
    input = getInput()
    
    print(f"Input: (scrabled data)\n{input}")
    for line in input:
        vals = []
        chars = [*line]
        for item in chars:
            if item in nums:
                vals.append(item)
        
        calibrationValues.append(int(vals[0] + vals[len(vals) - 1]))

    print(f"\n\nValues stripped from scrabled data:\n{calibrationValues}")
    
    calibrationSum = sum(calibrationValues)
    print(f"\n\nCalibrationValue: {calibrationSum}")

main()
