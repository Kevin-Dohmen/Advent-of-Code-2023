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
        
    # do the thing
    

main()