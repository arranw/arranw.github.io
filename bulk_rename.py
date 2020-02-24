import os
import datetime

date = datetime.datetime

i = 1

files = os.listdir("c:/pictures")

for file in files:
    fileType = file[-4:]
    fileDate = date.strptime(file[:-4], '%Y%m%d_%H%M%S')
    formattedDate = date.strftime(fileDate, "%d_%b_%Y_%H%M").upper()
    newFileName = "Aus_{}_{}{}"
    fileNo = str(i).zfill(4)
    formattedFilename = newFileName.format(fileNo, formattedDate, fileType)

    i = i + 1

    original = 'c:/pictures/' + file
    new = 'c:/pictures/' + formattedFilename

    os.rename(original, new)
