import random
import monkdata as m
import dtree
import drawtree_qt5
from matplotlib import pyplot as plt
import statistics

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]

# monk1 - prune tree
monk1train, monk1val = partition(m.monk1, 0.6) # size of training is 60 percent

newBestTree = dtree.buildTree(monk1train, m.attributes)
newValAcc = dtree.check(newBestTree, monk1val)
oldValAcc= 0.0

#TODO kleiner gleich
while oldValAcc < newValAcc:
    bestTree=newBestTree
    oldValAcc= dtree.check(bestTree, monk1val)
    prunedTrees= dtree.allPruned(bestTree)
    for newTree in prunedTrees:
        if(dtree.check(newTree, monk1val) > oldValAcc):
         newBestTree = newTree
    newValAcc= dtree.check(newBestTree, monk1val)

# drawtree_qt5.drawTree(bestTree)

# monk2 set for all fractions

fractionList =[]
fraction= 0.3
testAccuracyList=[]
valAccuracyList=[]
trainAccuracyList=[]


while fraction <= 0.8:
    fractionList.append(fraction)

    for i in range(100):
        monk1train, monk1val = partition(m.monk1, fraction) # size of training is 60 percent

        newBestTree = dtree.buildTree(monk1train, m.attributes)
        bestTree=newBestTree
        newValAcc = dtree.check(newBestTree, monk1val)
        oldValAcc= 0.0

        while oldValAcc < newValAcc:
            bestTree = newBestTree
            oldValAcc = dtree.check(bestTree, monk1val)
            prunedTrees = dtree.allPruned(bestTree)
            for newTree in prunedTrees:
                if(dtree.check(newTree, monk1val) > oldValAcc):
                    newBestTree = newTree
            newValAcc= dtree.check(newBestTree, monk1val)

        valAccuracyList.append(dtree.check(bestTree, monk1val))
        testAcc= dtree.check(bestTree, m.monk2test)
        testAccuracyList.append(testAcc)
        trainAccuracyList.append(dtree.check(bestTree,monk1train))

    fraction+=0.1

    #drawtree_qt5.drawTree(bestTree)

n=100
testAccuracyListAvg = [statistics.mean(testAccuracyList[i:i+n])for i in range(0,len(testAccuracyList),n)]
valAccuracyListAvg = [statistics.mean(valAccuracyList[i:i+n]) for i in range(0,len(valAccuracyList),n)]
# trainAccuracyListAvg = [statistics.mean(trainAccuracyList[i:i+n]) for i in range(0,len(trainAccuracyList),n)]

testAccuracyListVar = [statistics.variance(testAccuracyList[i:i+n]) for i in range(0,len(testAccuracyList),n)]
valAccuracyListVar = [statistics.variance(valAccuracyList[i:i+n]) for i in range(0,len(valAccuracyList),n)]
# trainAccuracyListVar = [statistics.variance(trainAccuracyList[i:i+n]) for i in range(0,len(trainAccuracyList),n)]


#TODO add data points

plt.errorbar(fractionList, testAccuracyListAvg, testAccuracyListVar, label='Averaged Test Accuracy')
plt.errorbar(fractionList, valAccuracyListAvg, valAccuracyListVar, label='Averaged Validation Accuracy')
# plt.plot(fractionList, trainAccuracyListAvg, label='Averaged Training Accuracy')

plt.xlabel("Fraction of Training Data")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

