# This is a sample Python script.
import math
import re
from sys import argv

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#getting i/o locations
train = argv[1]
test = argv[2]
model = argv[3]
answers = argv[4]

#my features for line
features = "call","device","machine","sales","launch","distance","unit","production","sale"
#So first I am trying to make sense based on features
#So the sense would be phone, and feature would be line


#line by line
Sense = []
key = ""

f =  open(train, "r")
with open(train) as file:
    for line in file:
        #storing what the correct sense is
        if("senseid" in line):
            if("phone" in line):
                key = "phone"
            if("product" in line):
                key = "product"
            #going to use the senseid as the key in the dic
        if("<s>" in line):
            aFeatures = [0,0,0,0,0,0,0,0,0, key]
            for i in range(len(features)-1):
                #splitting the sentence, to get the count of features
                if(features[i] in line):
                    #NOTE: I used the word with no bounds as my regex,
                    #My reasoning was that prevented me from having to make special cases
                    #for words like call to also get calls
                    aFeatures[i] = len(re.findall(features[i],line))
                    continue

            aFeaturesTuple = tuple(aFeatures)
            Sense.append(aFeatures)

#These are my tests. The end of the vector list is what contains the rule guess
for vector in Sense:
    if(vector[0] > 0):
        #Now the last index of Sense will have the sense determined by my test
        vector.append("phone")
    else:
        if (vector[1] > 0):
            # return
            vector.append("product")
        else:
            if (vector[2] > 0):
                # return
                vector.append("product")
            else:
                if (vector[3] > 0):
                    # return
                    vector.append("product")
                else:
                    if (vector[4] > 0):
                        # return
                        vector.append("product")
                    else:
                        if (vector[5] > 0):
                            # return
                            vector.append("phone")
                        else:
                            if (vector[6] > 0):
                                # return
                                vector.append("product")
                            else:
                                if (vector[7] > 0):
                                    # return
                                    vector.append("product")
                                else:
                                    if (vector[8] > 0):
                                        # return
                                        vector.append("product")
                                    else:
                                        vector.append("product")

countSense = {}


#going in and counting all of the features
for i in range(len(features)):
    featCount = 0
    for vector in Sense:
        if vector[i] > 0:
            featCount += vector[i]

    featAndCountTuple = (features[i], featCount)
    #getting the count of features
    countSense[features[i]] = featCount

testRankings = {}
for i in range(len(features)):
    totalFeatures = countSense[features[i]]
    totalProdGivenFeature = 0
    totalPhoneGivenFeature = 0
    for vector in Sense:
        if vector [i] > 0 and vector[len(vector)-2] == 'product':
            totalProdGivenFeature += vector[i]
        else:
            if vector [i] > 0 and vector[len(vector)-2] == 'phone':
                totalPhoneGivenFeature += vector[i]

    if totalFeatures == 0:
        totalFeatures = 1
    ProdGivenFeature = totalProdGivenFeature / totalFeatures
    PhoneGivenFeature = totalPhoneGivenFeature / totalFeatures
    if PhoneGivenFeature == 0:
        PhoneGivenFeature = 1
    if ProdGivenFeature == 0:
        ProdGivenFeature = 1
    testRank = abs(math.log(ProdGivenFeature/PhoneGivenFeature))
    testRankings[features[i]] = testRank



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
