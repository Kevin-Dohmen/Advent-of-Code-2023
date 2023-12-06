def getInput():
    f = open("input.txt", 'r')
    input = f.read().splitlines()
    f.close()
    return input


def formatInput(input):
    tmplst = []
    for item in input:
        tmp1 = item.split(':')
        tmplst.append([tmp1[0], tmp1[1].split()])
    tmplst2 = []
    for i in range(4):
        tmplst2.append(["race "+str(i), [tmplst[0][1][i], tmplst[1][1][i]]])
    return tmplst2

def main():
    input = formatInput(getInput())
    ways_to_win = []

    for race in input:
        time = int(race[1][0])
        record_distance = int(race[1][1])
        ways = 0

        for button_hold_time in range(time):
            speed = button_hold_time
            remaining_time = time - button_hold_time
            total_distance = speed * remaining_time

            if total_distance > record_distance:
                ways += 1

        ways_to_win.append(ways)

    result = 1
    for ways in ways_to_win:
        result *= ways

    print(result)

main()
