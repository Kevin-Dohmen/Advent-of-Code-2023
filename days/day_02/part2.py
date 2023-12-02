
red = 12
green = 13
blue = 14

def getInput():
    f = open("input.txt", 'r')
    input = f.read().splitlines()
    f.close()
    return input

def formatGames(input):
    games = []
    for item in input:
        games.append(item.split("; "))

    formattedGames = []
    for i in range (len(games)):
        formattedGames.append([])
        sets = games[i]
        for set in sets:
            formattedSet = []
            if "Game" not in set:
                for block in set.split(", "):
                    formattedSet.append(block)
            else:
                setWithoutGameNum = set.split(": ")[1]
                for block in setWithoutGameNum.split(", "):
                    formattedSet.append(block)
            formattedGames[i].append(formattedSet)

    return formattedGames

def main():
    input = formatGames(getInput())
    gamesData = []
    for i in range(len(input)):
        game = input[i]
        possibleSets = []
        gameMax = [0, 0, 0]
        print(str(game))
        for set in game:
            redAmnt, greenAmnt, blueAmnt = 0, 0, 0
            # print(set)
            for block in set:
                if "red" in block:
                    redAmnt += int(block.split()[0])
                elif "green" in block:
                    greenAmnt += int(block.split()[0])
                elif "blue" in block:
                    blueAmnt += int(block.split()[0])
            if redAmnt >= gameMax[0]:
                gameMax[0] = redAmnt
            if greenAmnt >= gameMax[1]:
                gameMax[1] = greenAmnt
            if blueAmnt >= gameMax[2]:
                gameMax[2] = blueAmnt
        print(gameMax)
        val = 1
        for item in gameMax:
            val = val * item
        gamesData.append(val)
    
    print(sum(gamesData))
    


main()
