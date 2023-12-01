import os

# define root dorectory
wd = os.getcwd()

folderAmnt = 25 # amount of folders to make (only supports below 100 for now)
folderStartWith = 'day_' # will add number after

filesToAdd = ['notes.txt', 'input.txt', "part1.py", "part2.py"] # files to add to each folder

for i in range (1, folderAmnt + 1):
    # generate folder name
    folderName = folderStartWith
    if i < 10:
        folderName += '0'
    folderName += str(i)

    # make directory and cd into it
    if folderName not in os.listdir():
        print(f"folder {folderName} does not exist: creating folder {folderName}")
        os.mkdir(folderName)
    else:
        print(f"folder {folderName} already exists")
    os.chdir(folderName)

    # make file
    for item in filesToAdd:
        if item not in os.listdir():
            print(f"file {item} not in {folderName}")
            f = open(item, 'w')
            f.close()
        else:
            print(f"file {item} already exists in {folderName}")

    # return to root directory
    os.chdir(wd)
