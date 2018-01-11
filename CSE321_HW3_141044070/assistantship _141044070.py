import math #infinity sayisini kullanmak icin import edildi
def findOptimalAssistantship(inputList):
    sizeofAsistant = len(inputList)
    sizeOfcourse = len(inputList[0])
    if(sizeofAsistant < sizeOfcourse):
        return -1
    else:
        listem =[]
        returnedList=[]
        for i in range(sizeofAsistant):
            listem.append(i)
        heapPermutation(listem,sizeofAsistant,returnedList)
        temp = math.inf
        templist=[]
        for i in returnedList:
            Stemp = 0

            for j in range(sizeofAsistant):
                if(j < sizeOfcourse):
                    Stemp =inputTable[i[j]][j]+Stemp
                else:
                    Stemp = Stemp + 6

            if(Stemp < temp):
                temp = Stemp
                templist = list(i)
        TTlist = []
        for i in range(sizeofAsistant):
            TTlist.append(0)
        for i in range(sizeofAsistant):
            if(i < sizeOfcourse ):
                TTlist[templist[i]] = i
            else:
                TTlist[templist[i]] = -1
    return (TTlist,temp)

#heaps permutation algoritmasının pesudure uygulaması vikipedia da sudo kodu mevcut
#https://www.wikizero.com/en/Heap's_algorithm
def heapPermutation(inputList,start,myliste):
    if(start == 1):
        myliste.append(list(inputList))
    else:
        for i in range(start):
            heapPermutation(inputList, start-1,myliste)
            if (start % 2 == 0):
                temp = inputList[i]
                inputList[i] = inputList[start - 1]
                inputList[start - 1] = temp
            else:
                temp = inputList[0]
                inputList[0] = inputList[start - 1]
                inputList[start - 1] = temp
        heapPermutation(inputList, start - 1, myliste)


# Courses  0  1   2     n * r n: course, r :asistan r >= n
"""inputTable = [[5, 8,  7],  # R.A. 0
             [8, 12, 7],  # R.A. 1
             [4, 8,  50],
              [1,20,40],
              [4,5,6],
              [9,40,10],
              [3, 4, 5],
              [1, 1, 1]]  # R.A. 2"""

"""inputTable = [[5, 8,  7],  # R.A. 0
             [8, 12, 7],  # R.A. 1
             [4, 8,  50],
              [1,20,40],
              [4,5,6],
              [9,40,10]]  # R.A. 2"""

inputTable = [[5, 8,  7],  # R.A. 0
             [8, 12, 7],  # R.A. 1
             [4, 8,  5]]

asist ,time =findOptimalAssistantship(inputTable)
print("assistant:",asist,"\ntime: ",time)

