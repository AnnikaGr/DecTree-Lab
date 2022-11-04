import dtree
import monkdata as m


# Assignment 3
for set in m.trainingsets:
    for attribute in m.attributes:
        print("Result:\n Set: "+ str(set)+ "\n Attribute: "+ str(attribute)+ "\n AverageGain: " + str(dtree.averageGain(set,attribute)))


for set in m.testingsets:
    for attribute in m.attributes:
        print("Result:\n Set: "+ str(set)+ "\n Attribute: "+ str(attribute)+ "\n AverageGain: " + str(dtree.averageGain(set,attribute)))



# Assignment 4 validation

# entropies of subsets
counter=1
for dataset in m.trainingsets:
    print ("Set: "+ str(counter))
    counter=+1
    for attr in m.attributes:
        for attrVal in attr.values:
             subset = dtree.select(dataset,attr,attrVal)
             print("Attribute: "+ str(attr) + " AttrVal: "+ str(attrVal)+ " Entropy: " + str(dtree.entropy(subset)))

# weighted sum of entropy of subsets

print("\n---------------- Weighted Sum of Entropy of Subsets -----------------")
counter=1
for dataset in m.trainingsets:
    print ("Set: "+ str(counter))
    counter+=1
    for attr in m.attributes:
        weightedSum=0
        for attrVal in attr.values:
            subset = dtree.select(dataset,attr,attrVal)
            weightedSum+= dtree.entropy(subset) * len(subset)
        print("Attribute: "+ str(attr) + " Weighted Sum: " + str(weightedSum))
