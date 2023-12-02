
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
            if redAmnt <= red and greenAmnt <= green and blueAmnt <= blue:
                possibleSets.append(True)

            else :
                possibleSets.append(False)
        gamesData.append([i+1, game, possibleSets])
            

        #print(f"Red:{redAmnt} Green:{greenAmnt} Blue:{blueAmnt}")
        # if redAmnt <= red and greenAmnt <= green and blueAmnt <= blue:
           # print("Correct")
            # gamesData.append([i+1, game, [redAmnt, greenAmnt, blueAmnt]])
        #print("\n")

    possibleGames = []
    for game in gamesData:
        print(f"Game {game[0]}: {game[1]}: {game[2]}")
        gameIsPossible = True
        for set in game[2]:
            if set == False:
                print("False")
                gameIsPossible = False
                break
        if gameIsPossible:
            print("True")
            possibleGames.append(game)
        print("\n")


    
    gamesDataum = 0
    for item in possibleGames:
        # print(f"Game {item[0]}: {item[1]}: {item[2]}")
        gamesDataum += item[0]
    
    print(f"Possible Game Sum: {gamesDataum}")
    


main()
