#David Ferrufino
#CMSC 416
#Assignment 04
#03/26/2023
#Project will take in a sentence, and it contains a word
#Project will use rules to determine context of word
#In this case either Product Line or Phone Line (sense)

#When the test was run, my resulting log values for each tests discriminatoryness was
#"call: 1.4","device: 0.0","machine:1.95","sales:2.66","launch:1.95","distance:0.0","unit 1.02","production 0.0","sale 0.0"

#Then I remade the order of the tests to be from greatest to least math log value (for max acc)
#Order is sales (product), machine (product), launch (product), call (phone), unit (product),

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

#my features
features = "sales","sale","launch","call","short","unit","long","production"
#So first I am trying to make sense based on features
#So the sense would be phone, and feature would be line


#asld;kfj;sklafkasl;ds;flkeyboardworks
Sense = []
key = ""

#reading the training data and making a vector for each feature count
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
            aFeatures = [0,0,0,0,0,0,0,0, key]
            for i in range(len(features)):
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
        vector.append("product")
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
                    vector.append("phone")
                else:
                    if (vector[4] > 0):
                        # return
                        vector.append("phone")
                    else:
                        if (vector[5] > 0):
                            # return
                            vector.append("product")
                        else:
                            if (vector[6] > 0):
                                # return
                                vector.append("phone")
                            else:
                                if (vector[7] > 0):
                                    # return
                                    vector.append("product")
                                else:
                                    if (vector[7] > 0):
                                        # return
                                        vector.append("product")
                                    else:
                                        vector.append("phone")

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
#in this section I determine the ranking of the features and tests
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

    #If total Features == 0, prevents it from dividing by 0 error
    if totalFeatures == 0:
        totalFeatures = 1
    #Finding each sense given each test
    ProdGivenFeature = totalProdGivenFeature / totalFeatures
    PhoneGivenFeature = totalPhoneGivenFeature / totalFeatures

    #Preventing division by zero
    if PhoneGivenFeature == 0:
        PhoneGivenFeature = 1
    if ProdGivenFeature == 0:
        ProdGivenFeature = 1
    #Getting the abs and log of the feature for each sense (shows how discriminatory it is)
    testRank = abs(math.log(ProdGivenFeature/PhoneGivenFeature))
    testRankings[features[i]] = testRank



#Tagging the test-set and outputting
f =  open(test, "r")
with open(test) as file:
    for line in file:
        key = ""
        if("instance id=" in line): #Getting the instance id on test
            key = line[14:-1]
            print(key, end = " ")
        if("<s>" in line):  #getting the entire line
            if("sales" in line):
                print("product" )
            else:
                if ("sale" in line):
                    print("product")
                else:
                    if ("launch" in line):
                        print("product")
                    else:
                        if ("call" in line):
                            print("phone")
                        else:
                            if ("short" in line):
                                print("phone")
                            else:
                                if ("unit" in line):
                                    print("product")
                                else:
                                    if ("long" in line):
                                        print("phone")
                                    else:
                                        if ("production" in line):
                                            print("product")
                                        else:
                                            print("phone")
