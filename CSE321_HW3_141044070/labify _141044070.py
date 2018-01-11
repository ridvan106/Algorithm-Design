"""
Rıdvan Demirci 141044070

"""
# -*- coding: utf-8 -*-
#graphların baslangıc notlarını return eder connected degil ise connected ise  1 return eder baslangıc nodu
def checkConnected(mapOfGTUs):
    neigbourd = []
    visited=[]
    notConnectedVertex=[]

    while(len(visited) != len(mapOfGTUs)):
        for j in range(len(mapOfGTUs)):
            j = j+1
            if(not(j in visited)):
                neigbourd.append(j)
                notConnectedVertex.append(j)
                break
        while(len(neigbourd)>0):
           vertex = neigbourd.pop(0)
           #print("vertex:",vertex)
           komsular = set(mapOfGTUs.get(vertex))

           size = len(komsular)
           for i in range(size):
               t = komsular.pop()
               if(not(t in visited) and not(t in neigbourd)):
                 neigbourd.append(t)

          # print(neigbourd)
           visited.append(vertex)
           #print(visited)
    return notConnectedVertex


def findMinimumCostToLabifyGTU(x,y,mapOfGTU):
    if (x < y):
        cost = len(mapOfGTU) * x
        return cost
    startsVertex = checkConnected(mapOfGTU) #graph connected degil ise start noktalari return edilir
   # print(startsVertex)
    #print(mapOfGTU)

    vertexSize = 0
    nodeSize = len(startsVertex)*x
    #print(nodeSize)
    while(len(startsVertex)>0):
        vertexTable=[]
        tempVertex=[]
        val =startsVertex.pop()
        vertexTable.append(val)
        tempVertex.append(val)
        #print(vertexTable)
        while(len(vertexTable)>0):
            t = vertexTable.pop(0)
           # print(t)
            neighbord = mapOfGTU.get(t)
            size = len(neighbord)
            for i in range(size):
                #print(neighbord)
                var = neighbord.pop()
                if(not(var in tempVertex)):
                    tempVertex.append(var)
                    vertexTable.append(var)

        vertexSize = vertexSize+len(tempVertex)-1


    return ((vertexSize*y)+nodeSize)


#test durumları
"""mapOfGTU = {     1 : set([2,3]),
                 2 : set([1,3,4]),
                 3 : set([1,2,4]),
                 4 : set([3,2]),
                 5 : set([6]),
                 6 : set([5]) }"""
"""mapOfGTU ={
            1:set([2,3]),
            2:set([1,3]),
            3:set([1,2]),
            4:set([5,6]),
            5:set([4,6]),
            6:set([4,5]),
            7:set([8]),
            8:set([7])}"""
"""mapOfGTU = {
    1 : set([2,3]),
    2 : set([1,3]),
    3 : set([1,2]) } # graph is initialized as dictionary"""
"""mapOfGTU = {
    1 : set([5]),
    2 : set([5]),
    3 : set([5]),
    4 : set([5]),
    5 : set([1,2,3,4])}"""
"""mapOfGTU ={
            1:set([3]),
            2:set([4]),
            3:set([1,5,7,8]),
            4:set([2,9]),
            5:set([3]),
            6:set([9]),
            7:set([3]),
            8:set([3]),
            9:set([6]),
            }"""
"""mapOfGTU = {
    1 : set([2]),
    2 : set([1]) }"""
"""mapOfGTU ={
            1:set([2]),
            2:set([1,3,5]),
            3:set([2,4]),
            4:set([3,5,7]),
            5:set([2,4,6]),
            6:set([5]),
            7:set([4,8]),
            8:set([7,9]),
            9:set([8]),
            }"""
"""mapOfGTU = {
    1 : set([2,4]),
    2 : set([1,3,4]),
    3 : set([2,4]),
    4 : set([1,2,3]),
    5 : set([])}    """    
"""mapOfGTU ={
            1:set([2]),
            2:set([1,3]),
            3:set([2,4]),
            4:set([3,5]),
            5:set([4,6]),
            6:set([5,7]),
            7:set([6,8]),
            8:set([7,9]),
            9:set([8]),
            }"""

mapOfGTU = {
    1 : set([]),
    2 : set([]),
    3 : set([]),
    4 : set([]),
    5 : set([])}


print(findMinimumCostToLabifyGTU(2,1,mapOfGTU))