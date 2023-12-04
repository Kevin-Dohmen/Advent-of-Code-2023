
nums = [*"0123456789"]

def getInput():
    f = open("input.txt", 'r')
    input = f.read().splitlines()
    f.close()
    return input


def formatInput(input):
    tmplist = []
    for item in input:
        tmplist.append([*item])
    return tmplist


def main():
    input = formatInput(getInput())
    
    validValues = []
    
    for y in range(len(input)):
        stringTrue = False
        cString = ""
        for x in range(len(input[y])):
            cCharacter = input[y][x]
            if cCharacter in nums:
                print(f"character {cCharacter} at {x+1}:{y+1} is a valid character")
                cString += cCharacter
                for yOffset in range(-1, 2):
                    yC = y + yOffset
                    for xOffset in range(-1, 2):
                        xC = x + xOffset
                        if (0 <= xC < len(input[y])) and 0 <= yC < len(input):
                            checkChar = input[yC][xC]
                            if checkChar not in nums and checkChar != '.':
                                print(f"character {cCharacter} at {x+1}:{y+1} is adjacent to {checkChar} at {xC+1}:{yC+1}")
                                stringTrue = True
            else:
                if stringTrue == True:
                    print(f"cString = {cString}")
                    validValues.append(int(cString))
                stringTrue = False
                cString = ""
                        
    print(sum(validValues))


main()
