""""
Rıdvan Demirci
    141044070

- verilen array ilk önce dived and conquer de olan dive kısmı
için en küçük parçalara ayrılır ancak ilk önce arrayin ilk kısmında
sag ve sol kısımların hesaplanması için farklı flagler ile gonderilir...
bunun için hesaplama ayırt etmek içinde yine aynı fonksyon kullanılır
sadece 1 tane degerde enkucuk sub arrat olabilir bu durum için ise status
table kulanılır

- worstcase durumu ise arrayin tamamının minimum sub array içine dahil olma
durumudur.
budurumda listeyi tamamı için conquere yapıcak ve sonuna kadar parçalıyacağı için
worstcase:O(nlogn) olur



"""
import sys

def arrange(sol,sag,flag,statusTable):
    leftSum = sum(sol)
    rightSum = sum(sag)
    if(leftSum <sum(statusTable)):  #kucuk olan kısımlar status table atılır
        statusTable.clear()
        for i in sol:
            statusTable.append(i)

    if(rightSum<sum(statusTable)):  #eger sag kısım en kucuk ise o atilir
        statusTable.clear()
        for i in sag:
            statusTable.append(i)
    temp=[]
    if(flag == 0):  #arrayin sol kismi gelmis ise
        if(rightSum<0 and leftSum<0):   #iki tarafda sifirdan kucuk ise listenin tamami doner
            temp = sol
            for i in range(len(sag)):
                temp.append(sag[i])
        elif (rightSum < leftSum):  #eger sataraf kucuk ise sag taraf return eder
            temp = sag
        elif(leftSum < rightSum):   #sol taraf kucuk ise her iki taraf return eder
            temp = sol
            for i in range(len(sag)):
                temp.append(sag[i])

    elif(flag == 1):    #arrayin sag tarafi gelmis ise
        if((leftSum>0 and rightSum>0) or (leftSum<0 and rightSum<0) ):#her iki taraf pozitif veya negatif ise direk tamami
            temp = sol
            for i in range(len(sag)):
                temp.append(sag[i])
        elif (leftSum < rightSum):
            temp = sol
            for i in range(len(sag)):
                temp.append(sag[i])
        elif (rightSum <= leftSum):
            temp = sol
            for i in range(len(sag)):
                temp.append(sag[i])

    summ = 0
    indis = -1
    if(flag == 0):  #eger soltaraf status table dan kucuk ise status yerine alınır
        for i in range(len(temp)):
            summ = summ +temp[i]
            if(summ < sum(statusTable)):
                indis =i
        if(not(indis ==-1)):
            statusTable.clear()
            for i in range(indis+1):
                statusTable.append(temp[i])
    else:   #sag taraf kucuk ise ayni sekilde status table yerini alir
        i = len(temp)-1
        while(i>=0):
            summ = summ + temp[i]
            if (summ < sum(statusTable)):
                indis = i
            i -=1
        if (not (indis == -1)):
            statusTable.clear()
            for i in range(indis + 1):
                statusTable.append(temp[i+indis])

    return  temp

def min_subarray_finder(inpArr):
    if(len(inpArr) <= 1):
        return inpArr
    else:
        mid = int(len(inpArr) / 2) # tam orta degeri
        statusTable = [99999]   #maximum boyle dusunulkur

        leftSide= inpArr[0:mid]
        rightSide=inpArr[mid:]
        leftSide = leftarrange(leftSide,statusTable)    #sol kisim gonderilir
        rightSide = rightArrange(rightSide, statusTable)    #sag kisim gonderilir
        arrange(leftSide,rightSide,0,statusTable)   #arrange edilir
        return statusTable  #status table return edilir en kucuk deger orda var


def leftarrange(inpA,statusTable):  #sol kisim duzeltmek icin
    if (len(inpA) <= 1):
        return inpA
    mid = int(len(inpA) / 2)  # tam orta degeri
    if(len(inpA)%2 == 0 ):  #cift ise dirrek gonderilirs
        leftSide = leftarrange(inpA[0:mid],statusTable)
        rightSide = leftarrange(inpA[mid:],statusTable)
        return arrange(leftSide, rightSide,0,statusTable)


    else:   #tek ise orta deger tutulur duruma gore merge edilir
        leftSide = leftarrange(inpA[0:mid], statusTable)
        rightSide = leftarrange(inpA[mid+1:], statusTable)
        temp = arrange(leftSide, rightSide, 0, statusTable)

        if(len(inpA) - len(temp) == 1):
            temp.insert(mid,inpA[mid])

        return temp

def rightArrange(inpA,statusTable):
    if (len(inpA) <= 1):
        return inpA
    mid = int(len(inpA) / 2)  # tam orta degeri
    leftSide = rightArrange(inpA[0:mid],statusTable)
    rightSide = rightArrange(inpA[mid:],statusTable)
    return arrange(leftSide, rightSide,1,statusTable)

"""inpArr = [1, 2,4,-1,-2,1]"""
"""inpArr = [1,2,3,-5,1,-2,3,7]"""
"""inpArr = [1,-2,-6,5,-8,-8,9,6]"""
"""inpArr = [15,-6,-9,8]"""
inpArr = [1, -4, -7, 5, -13, 9, 23,-1]
"""inpArr = [-4, 5, -13]"""
"""inpArr = [1,2,3,-4,0,-9]"""
"""inpArr =[5,6,-90,1,2,3,4,7,-16]"""
"""inpArr = [-10,1,2,3,4,-21]"""
"""inpArr =[1,2,-9,-5,10,-11,6,-8,1,2,3,-7]"""
print(min_subarray_finder(inpArr))
