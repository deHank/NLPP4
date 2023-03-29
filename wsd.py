# This is a sample Python script.
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
                if(features[i] in line):
                    aFeatures[i] = aFeatures[i]+1
                    continue

            aFeaturesTuple = tuple(aFeatures)
            Sense.append(aFeatures)

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




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
