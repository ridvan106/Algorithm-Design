# -*- coding: utf-8 -*-
#	python 3.6 ile derlenirse daha iyi olur
#       Rıdvan Demirci
#               141044070
#
#
#
def compareScales (leftScaleList, rightScaleList):
	print (leftScaleList ,"-" , rightScaleList)
	result = sum(leftScaleList) - sum(rightScaleList)
	if result < 0:
		return 1
	elif result > 0:
		return -1
	else:
		return 0
def findRotten(listOfwalnut,size):	#logaritmik time da olması icin array size da girilmeli
	
	if(size == 1):
		return 0
	if(size % 2 == 0):		# cift ise direk yarirsi ile islemler yapar
		temp = compareScales(listOfwalnut[0:int(size/2)],listOfwalnut[int(size/2):]) # sol ve sag tarafın farkı alınır
		#print temp
		if(temp == 1):
			return findRotten(listOfwalnut[0:int(size/2)],int(size/2)) # sag taraf buyuk ise rotten sol taraftadir
		elif(temp == -1):
			return int(size/2) + findRotten(listOfwalnut[int(size/2):],int(size/2))
		else:
			return -1;
	else:
		temp = size/2
		tempSum = compareScales(listOfwalnut[0:int(temp)],listOfwalnut[int(temp+1):])
		if(tempSum == 0):			#sag ve sol esit ise ortadaki eleman en kucuktur
			if(listOfwalnut[int(temp)]==listOfwalnut[int(temp)-1]):
				return -1
			return int(temp)
		elif(tempSum == -1):
			return int(temp) + 1 + findRotten(listOfwalnut[int(temp+1):],int(temp))	#yaridan sonra
		else:
			return findRotten(listOfwalnut[0:int(temp)],int(temp))	#yaridan once
				
				
	

sample = [1,1,1,1,1,0.5,1,1,1]	#ornek
print (len(sample))
print ("index: ",findRotten(sample,len(sample)))	#drive kısmı
