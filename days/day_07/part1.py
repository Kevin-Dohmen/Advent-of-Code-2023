cardStrength = [*"23456789TJQKA"]


def getInput():
    f = open("input.txt", 'r')
    input = f.read().splitlines()
    f.close()
    return input


def formatInput(input):
    tmplst = []
    for item in input:
        tmp1 = item.split()
        tmplst.append([[*tmp1[0]], int(tmp1[1])])
    return tmplst


def main():
    input = formatInput(getInput())
    gameData = []
    matchAmnt = []
    
    for game in input:
        print(game)
        hand = game[0]
        handCharCount = []
        ijDone = []
        
        for i in range(len(hand)):
            ichar = hand[i]
            charCount = 0
            
            for j in range(len(hand)):
                if i != j and i not in ijDone and j not in ijDone:
                    jchar = hand[j]
                    
                    if ichar == jchar:
                        print(f"match {ichar} {jchar}")
                        
                        charCount += 2
                        ijDone.append(i)
                        ijDone.append(j)
            handCharCount.append(charCount)
        print(handCharCount)
        matchAmnt.append(handCharCount)
    
    #for item in matchAmnt:
    #    print(item)
        
                        


main()
