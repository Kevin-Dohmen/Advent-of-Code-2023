calibrationValues = []
calibrationSum = 0

nums = [*"0123456789"]
numsSpelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def getInput():
    f = open("input.txt", 'r')
    input = f.read().splitlines()
    f.close()
    return input
 
def main():
    print
    input = getInput()
    
    print("Input: (scrabled data)")
    print(input)
    
    for line in input:
        print(line)
        vals = []
        chars = [*line]
        
        # get first
        firstDone = False
        shrtline = ""
        for i in range(0, len(chars)):
            shrtline = shrtline + chars[i]
            for number in numsSpelled:
                if number in shrtline and not firstDone:
                    vals.append(numsSpelled.index(number) + 1)
                    print(f"num {number} in {shrtline}  {str(numsSpelled.index(number) + 1)}")
                    firstDone = True
                if str(numsSpelled.index(number) + 1) in shrtline and not firstDone:
                    vals.append(numsSpelled.index(number) + 1)
                    print(f"num {str(numsSpelled.index(number) + 1)} in {shrtline}   {str(numsSpelled.index(number) + 1)}")
                    firstDone = True
        
        # get last
        lastDone = False
        shrtline = ""
        for i in range(len(chars) - 1, 0 - 1, -1):
            shrtline = chars[i] + shrtline
            for number in numsSpelled:
                if number in shrtline and not lastDone:
                    vals.append(numsSpelled.index(number) + 1)
                    print(f"num {number} in {shrtline}  {str(numsSpelled.index(number) + 1)}")
                    lastDone = True
                if str(numsSpelled.index(number) + 1) in shrtline and not lastDone:
                    vals.append(numsSpelled.index(number) + 1)
                    # print("num " + str(numsSpelled.index(number) + 1) + " in " + shrtline + "   " + str(numsSpelled.index(number) + 1))
                    print(f"num {str(numsSpelled.index(number) + 1)} in {shrtline}   {str(numsSpelled.index(number) + 1)}")
                    lastDone = True
        
        print(int(str(vals[0]) + str(vals[1])))
        print("\n\n")
        
        calibrationValues.append(int(str(vals[0]) + str(vals[1])))
        


    print(f"\n\nValues stripped from scrabled data:\n{calibrationValues}")
    
    calibrationSum = sum(calibrationValues)

    print(f"\n\nCalibrationValue: {calibrationSum}")

main()
