import os

# define root dorectory
wd = os.getcwd()

folderAmnt = 25 # amount of folders to make (only supports below 100 for now)
folderStartWith = 'day_' # will add number after

filesToAdd = ['notes.txt', 'input.txt'] # files to add to each folder

for i in range (1, folderAmnt - 1):
    # generate folder name
    folderName = folderStartWith
    if i < 10:
        folderName += '0'
    folderName += str(i)

    # make directory and cd into it
    os.mkdir(folderName)
    os.chdir(folderName)

    # make file
    for item in filesToAdd:
        f = open(item, 'w')
        f.close()

    # return to root directory
    os.chdir(wd)
