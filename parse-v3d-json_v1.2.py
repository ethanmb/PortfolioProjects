#
#Ethan Mackenzie Brown
#June 2 2022
#
#updated to fix issue where certain measurements had no data for some trials
#

import json
import csv


from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file


prevFile = ""
currentTrial = {}
trialNumbers = []
master = []
headerHolder = []
trialInt = 0

#opens csv to write to


jsonToRead = filename
csvToWrite = filename.replace(".json", ".csv")

with open (csvToWrite, "w") as x:
    thewriter = csv.writer(x)

    #opens json to read from
    with open (jsonToRead, "r") as f:
        exportedFile = json.load(f)
        exportedFile = exportedFile["Visual3D"]

        #iterates through every piece of data exported
        for trials in exportedFile:
            trialName = trials["filename"]
            measurementType = trials["name"]
            signal = trials["signal"]
            #looks to see if we're still on same trial, as each piece of data is exported seperately, so you have multiple for the same trial
            if (prevFile != trialName):
                master.append({"trialName":trialName.replace(".c3d", "")})
                trialNameReal = trialName.replace(".c3d", "")
            trialInt = int(trialNameReal[len(trialNameReal) - 2:]) -1

            #iterate through signals
            for data in signal:
                component = data["component"]
                output = data["data"]
                master[trialInt][measurementType+component] = output
                headerHolder.append(measurementType+component)
                headerHolder = list(dict.fromkeys(headerHolder))
            prevFile = trialName


    headerHolder.sort()
    headerHolder.insert(0, "trialName")
    thewriter.writerow(headerHolder)

    #anything with no data will now be 0
    for x in master:
        for key in headerHolder:
            if key not in x:
                x[key] = 0

    #iterates through master list and writes to csv
    for x in master:
        #fixes trial name
        trialName = x["trialName"]
        trialNameReal = trialName.replace(".c3d", "")

        holder = []

        #removes brackets and '' from data
        for key in headerHolder:
            z = str(x[key])
            z = z.replace("[", "")
            z = z.replace("]", "")
            z = z.replace("'", "")
            holder.append(z)

        thewriter.writerow(holder)
