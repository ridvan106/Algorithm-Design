"""
    Rıdvan Demirci
        141044070
    problem en kısa yol problemine benziyor ama tam tersi
    öncelikle arraylerin ilk columb ları herzaman sabit diğerleri için ise
    enson daki arraye ya öncesi yada bir üst ve öncesinden gelen deger olabilir.
    ilk baş taki array için ise yad gene kendinden önce yada önce ve altından gelen olabilir

    diğer tüm arrayler için 3 ihtimal vardır,ya kendinden önce ,kendinden önce üst veya
    kendinden önce ve alttan geline bilir bunların maximumu return edilir

    analaiz olarak da dynamic programing de zaten analizler table size ile dogru orantılıdır
    burada da table size gelen arraydeki row ve columb la alakalı oldugu için
    O(n*m) 'dir

"""

def arrange(myList):
    temp = list(myList)
    i  =1
    while(i<len(temp)):
        temp[i] = temp[i]+temp[i-1]
        i+=1
    return temp

def theft(amountOfMoneyInLand):
    row = len(amountOfMoneyInLand)
    col = len(amountOfMoneyInLand[0])
    maximum = 0
    dinamikArray =[]
    temp =[]
    for i in range(row):
        for j in range(col):
            if(j == 0):
                temp.append(amountOfMoneyInLand[i][j])
            else:
                temp.append(0)
        dinamikArray.append(list(temp))
        if (maximum < dinamikArray[i][j]):
            maximum = dinamikArray[i][j]
        temp.clear()

    #print(dinamikArray)
    #print(col)
    i = 1
    while(i< col):
        j = row-1
        while(j>=0):
            if(j == 0):
                if(row == 1):
                    dinamikArray[j][i] = dinamikArray[j][i - 1] + amountOfMoneyInLand[j][i]
                else:
                    dinamikArray[j][i]= max(dinamikArray[j][i-1],dinamikArray[j+1][i-1])+amountOfMoneyInLand[j][i]
            elif(j == (row -1)):
                dinamikArray[j][i] = max(dinamikArray[j][i - 1], dinamikArray[j - 1][i - 1]) + amountOfMoneyInLand[j][i]

            else:
                dinamikArray[j][i] = max(dinamikArray[j][i - 1], dinamikArray[j + 1][i - 1], dinamikArray[j - 1][i - 1]) + amountOfMoneyInLand[j][i]
            if(maximum < dinamikArray[j][i]):
                maximum = dinamikArray[j][i]
            j -=1
        i +=1
    #print(dinamikArray)
    return  maximum


#amountOfMoneyInLand = [[1,2],[3,4],[5,6],[10,1],[3,5]]
#amountOfMoneyInLand = [[1,2]]
#amountOfMoneyInLand = [[100,20,30],[40,80,10],[4,8,7]]
#amountOfMoneyInLand = [[100,20,30],[40,90,10],[4,8,7]]
#amountOfMoneyInLand = [[1]]
#amountOfMoneyInLand = [[10],[20],[30]]
#amountOfMoneyInLand = [[1,2,3,4,5,6],[4,8,0,1,2,10]]
#amountOfMoneyInLand = [[1],[0],[2],[3],[40],[8]]
#amountOfMoneyInLand = [[100,5,4,2],[3,500,40,50],[10,20,200,1]]
#amountOfMoneyInLand = [[4,8,7,3],[10,5,2,8],[4,40,2,100],[7,16,20,30]]

#amountOfMoneyInLand= [[1,3,1,5], [2,2,4,1], [5,0,2,3], [0,6,1,2]]
amountOfMoneyInLand= [[10,33,13,15], [22,21,4,1], [5,0,2,3], [0,6,14,2]]
res = theft(amountOfMoneyInLand)
print("sonuc",res)
