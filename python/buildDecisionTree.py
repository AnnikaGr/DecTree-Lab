import idlelib.calltip_w

import dtree
import monkdata as m
import drawtree_qt5


# compute information gains on level 2

newNodes= {}
for attrVal in m.attributes[4].values:
    newNodes[attrVal] = dtree.select(m.monk1,m.attributes[4],attrVal)
    # newNodes.append(dtree.select(m.monk1,m.attributes[4],attrVal))

newAttributes = []
for attr in m.attributes:
    if(attr != m.attributes[4]):
        newAttributes.append(attr)

print("\n ----------------- Average Gains for future decisions after choosing A5  -----------------")
for prevDecision, subset in newNodes.items():
    print("PrevDecision: "+ str(prevDecision))
    for attr in newAttributes:
        print("Attribute: " + str(attr) + ", AvgGain: " + str(dtree.averageGain(subset, attr)))

print("\n ----------------- Entropies at subsets after choosing A5 -----------------")

for prevDecision, subset in newNodes.items():
    print("PrevDecision: "+ str(prevDecision))
    print("Attribute: " + str(attr) + ", Entropy: " + str(dtree.entropy(subset)))


# Next choices
for prevDecision, subset in newNodes.items():
    print("PrevDecision: "+ str(prevDecision))
    bestAttr = dtree.bestAttribute(subset, newAttributes)
    for bestAttrVal in bestAttr.values:
        print("BestAttribute: " + str(bestAttr.name) + ", BestAttrVal: " + str(bestAttrVal) + " MostCommons: "+ str(dtree.mostCommon(dtree.select(subset,bestAttr,bestAttrVal))))

# Compared to predefined routine

drawtree_qt5.drawTree(dtree.buildTree(m.data_test, m.attributes_test, 2))

# Assignment 5
print ("----- Assignment 5 Train and Test sets ----------")

# print ("\nMonk1")
# t= dtree.buildTree(m.monk1, m.attributes)
# print (dtree.check(t, m.monk1))
# print (dtree.check(t, m.monk1test))
#
# print ("\nMonk2")
# t= dtree.buildTree(m.monk2, m.attributes)
# print (dtree.check(t, m.monk2))
# print (dtree.check(t, m.monk2test))
#
# print ("\nMonk3")
# t= dtree.buildTree(m.monk3, m.attributes)
# print (dtree.check(t, m.monk3))
# print (dtree.check(t, m.monk3test))