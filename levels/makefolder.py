import os

wd = os.getcwd()

for i in range (1, 26):
    folderName = 'lvl_' + str(i)
    os.mkdir(folderName)
    os.chdir(folderName)
    f = open('score.txt', 'w')
    f.close()
    os.chdir(wd)
