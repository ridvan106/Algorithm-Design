"""
----Rıdvan Demirci 141044070----


öncelikle greedy algoritması gereği en uygun seçenek olan
digit kadar( N ) listeye 5 sayısını atar ve check() fonktionuna gönderir
eğer uyugunsa listeyi string yapıp return eder,
eğer uygun değil ise yine greedy algoritmasına göre son basamaktan
başlayıp her basamağa 3 koyup tekrar check()  fonksyonuna gönderir


"""

#fonsyon decent olup olmamasını kontrıl eder
def check(get_list):
    tree = 0
    five = 0
    for i in get_list:
        if(i == 3):
            tree += 1
        else:
            five += 1

    if(tree%5 == 0 and five%3 == 0):
        return True
    return False

#gelen listeyi stringe cevirir
def convertDigit(getList):
    tempString = ""
    for i in getList:
        tempString +=str(i)
    return tempString


def decentNumber(Num):
    tempList = []
    for i in range(Num):
        tempList.append(5)

    if (check(tempList)):
        return convertDigit(tempList)
    else:
        indis = Num -1
        for i in range(Num):
            tempList[indis] = 3
            if (check(tempList)):
                return convertDigit(tempList)
            indis -=1
    return -1


print(decentNumber(1))
print(decentNumber(3))
print(decentNumber(4))
print(decentNumber(5))
print(decentNumber(6))
print(decentNumber(11))
