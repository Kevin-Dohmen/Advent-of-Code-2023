def getInput():
    f = open("input.txt", 'r')
    input = f.read().splitlines()
    f.close()
    return input


def formatInput(input):
    tmplst = []
    sequence = [*input[0].strip()]  # Remove leading and trailing whitespace
    
    for i in range(len(input)):
        item = input[i]
        if i >= 2:
            tmp = item.split('=')
            tmp2 = tmp[1].split(',')
            tmplst.append([tmp[0].strip(), [x.strip().strip('()') for x in tmp2]])  # Remove leading and trailing parentheses for each item in tmp2
        
    return sequence, tmplst


def main():
    sequence, input = formatInput(getInput())
    
    print(sequence)
    
    for item in input:
        print(item)
    
    lenSeq = len(sequence)
    
    i = 0

    srcItem = "AAA"
    
    lastItem = "ZZZ"
    
    working = True
    while working:
        lr = sequence[i % lenSeq]

        for j in range(len(input)):
            item = input[j]
            if item[0] == srcItem and item[1][0] != lastItem:
                fndItem = item
                if lr == 'L':
                    srcItem = fndItem[1][0]
                else:
                    srcItem = fndItem[1][1]
                break
        if fndItem[0] == lastItem:
            print(f"FOUND IT! {i}")
            working = False
        
        
        print(f"{i}\tSearch item: {srcItem} \t|Left/Right item: {lr} \t|Found item: {fndItem} \t|FoundIndex: {j}")
        i += 1


main()