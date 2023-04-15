#This would be run python3 scorer.py ans.txt line-key.txt
#most likely baseline 0.57142857142
#Result was .66 acc vs vs most likely (product) .57
#I manually calculated most likely
#accuracy was improved by .09


import math
import re
from sys import argv

ans = argv[1]
key = argv[2]

fAns = open(ans, "r")
fKey = open(key, "r")

#Getting our test output and key into lines to compare
faLines = fAns.readlines()
fkLines = fKey.readlines()

confusionMatrix = {}
correctTag = 0
totalTag = 0

for i in range(len(fkLines)):

    #getting only the context for each instance
    key = fkLines[i].partition("senseid=\"")[2]
    key = key.partition("\"/>")[0]
    ans = faLines[i].partition("> ")[2]
    ans = ans.partition("\n")[0]

    if(ans==key):
        correctTag = correctTag+1
        totalTag = totalTag +1
    else:
        totalTag = totalTag +1

    if ans in confusionMatrix:
        if key in confusionMatrix[ans]:
            confusionMatrix[ans][key] += 1
        else:
            confusionMatrix[ans][key] = 1
    else:
        confusionMatrix[ans] = {key: 1}

#getting accuracy (correct/total)
acc = correctTag/totalTag

print("test: key: count \n")
for testTag in confusionMatrix:
    row = []
    for keyTag in confusionMatrix[testTag]:
        #printing the confusion matrix (but not in matrix form)
        print(testTag + ":" + keyTag + " " + str(confusionMatrix[testTag][keyTag]))
print("Accuracy " + str(acc))

#Most likely from training =