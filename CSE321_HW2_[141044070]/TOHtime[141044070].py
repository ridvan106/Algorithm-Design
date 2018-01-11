# -*- coding: utf-8 -*-
#	python 3.6 ile derlenirse daha iyi olur
#       Rıdvan Demirci
#       141044070


import sys
def timeCalculate(a,b,n,time):
	sizeHonoi = 3
	count = 1
	list =["SRC","AUX","DST"]	#sabit pegler
	for inlist in range(sizeHonoi):
		#print(inlist)
		if list[inlist] == a:	#hangi diske tasinacaksa o fark hesaplanır
			temp1 = count
		if list[inlist]  == b:
			temp2 = count
		count = (count +1)
		
	temp1 = abs(temp1 - temp2)	
	time[n-1] = temp1*n + time[n-1];	#ve ilgii indis ile toplanir
def towers(n):
	time =[]
	for i in range(n):		#her pegs icin liste ye 0 eklenir
		time.append(0);
		
	
	towershelper("SRC","AUX","DST",n,time);		#pegs isimleri sabit olmali
	for i in range(n):	
		print ("Elapsed time for disk" ,i+1,  ":", time[i])
def towershelper(a,b,c, n,time):
	if n == 1:
		print ("disk ",n ," :move from", a , "to", c)
		timeCalculate(a,c,n,time);
		 	
	else:
		towershelper(a,c,b,n-1,time)
		print ("disk ",n ," :move from", a , "to", c)
		timeCalculate(a,c,n,time);
		towershelper(b,a,c,n-1,time);
n = input("Enter the input size:")


towers(int(n));
	
