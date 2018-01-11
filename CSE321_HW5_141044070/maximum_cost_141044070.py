"""
    Rıdvan Demirci 141044070

once problemin basinda 2 tane array olusturdum ilk arrayin ilk indisi
y nin ilk indisi ikinci arrayin ilk indisi ise 1 dir
sonra kendinden sonrakini duruma gore karsilastirdim
ve butuk olmasi icin 1 mi veya arrayin kendi indisi mi
diye yerlestirdim onlari da bir arrayde tuttum


"""

def find_maximum_cost(Y):
   cost1=[]
   cost2=[]
   for x in Y:
       cost1.append(0)
       cost2.append(0)

   cost1[0] = Y[0]
   cost2[0] = 1
  #s print(cost1,"\n",cost2)

   i=1
   while(i<len(Y)):
       if(cost1[i-1] != 1):
           cost1[i] = 1
       else:
           if(i == len(Y)-1):
               if(cost1[i-1] == 1):
                   cost1[i]=Y[i]
               else:
                   cost1[i] = 1
           elif((Y[i+1]-1)>(2*(Y[i]-1))):
               cost1[i] = 1
           else:
               cost1[i] = Y[i]

       if (cost2[i - 1] != 1):
           cost2[i] = 1
       else:
           if (i == len(Y) - 1):
               if (cost2[i - 1] == 1):
                   cost2[i] = Y[i]
               else:
                   cost2[i] = 1
           elif ((Y[i + 1] - 1) > (2 * (Y[i] - 1))):
               cost2[i] = 1
           else:
               cost2[i] = Y[i]


       i +=1
  # print("cost1",cost1,sumOf(cost1))
  # print("cost2",cost2,sumOf(cost2))
   return max(sumOf(cost1),sumOf(cost2))
def sumOf(X):

    S = 0
    if(len(X) == 1):
        return X[0]
    for i in range(len(X)-1):
        S += abs(X[i+1] -X[i])

    return S





"""Y = [2,3,6,7,9]"""
"""Y = [14,1,14,1,14]"""

Y = [50,28,1,1,13,7]
"""Y = [5]"""
"""Y = [80,6,45,2,31,50]"""
"""Y =[100,200,400]"""
"Y = [2,8,9,12,55,46,3,1,5]"""
"""Y = [1,9,11,7,3]"""
"""Y = [50,28,1,1,13,7]"""
"""Y =[79 ,6 ,40, 68, 68 ,16 ,40 ,63 ,93 ,49 ,91]"""
"""Y = [80, 22 ,45 ,11 ,67 ,67 ,74 ,91 ,4 ,35 ,34 ,65 ,80 ,21 ,95 ,1 ,52 ,25 ,31 ,2 ,53]"""
cost = find_maximum_cost(Y)
print("result",cost)
