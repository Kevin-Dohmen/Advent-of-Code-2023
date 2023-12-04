
def getInput():
    f = open("input.txt", 'r')
    input = f.read().splitlines()
    f.close()
    return input

def formatInput(input):
    tmplist = []
    for item in input:
        tmp = item.split(':')
        tmp2 = tmp[1].split('|')
        tmplist.append([tmp[0], tmp2[0].split(), tmp2[1].split()])
        
    return tmplist


def main():
    input = formatInput(getInput())
    
    vals = []
    
    for card in input:
        x = 0
        for number in card[1]:
            if number in card[2]:
                x += 1
        if x >= 1:
            print(f"x:{x} \tpow(2, x)/2: {pow(2, x)/2}")
            vals.append(pow(2, x)/2)
    
    for val in vals:
        print(val)
    
    print(sum(vals))

main()
