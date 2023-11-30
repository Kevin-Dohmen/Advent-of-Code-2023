import os

# define root dorectory
wd = os.getcwd()

for i in range (1, 26):
    # generate folder name
    folderName = 'lvl_'
    if i < 10:
        folderName += '0'
    folderName += str(i)

    # make directory and cd into it
    os.mkdir(folderName)
    os.chdir(folderName)

    # make file
    f = open('score.txt', 'w')
    f.close()

    # return to root directory
    os.chdir(wd)
