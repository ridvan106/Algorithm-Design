"""
Rıdvan Demirci
    14144070
- iki implementasyonu karsilastirdigimizda
    Hoare partision daha verimli gözüküyo çünku lomuto
    partitiona göre swap sayısı daha azdır



"""

#derste hocanın yazdıgı pseudo kode implementationı x
def lomutoPartition(arr,first,last):
    p=arr[first]
    s = first
    i = first+1
    while(i<=last):
        if(arr[i] < p):
            s +=1
            arr[s],arr[i] = arr[i],arr[s]
        i +=1
    arr[first],arr[s] = arr[s],arr[first]
    return s

#derste hocanın yazdıgı pseudo kode implementationı x
def hoarePartition(arr,first,last):
    p = arr[first] #pivot
    i = first
    j = last
    while(j> i):
        while(arr[i]<p):
            i += 1

        while(arr[j]>p):
            j =j-1
        if(i<=j):
            arr[i], arr[j] = arr[j], arr[i]
    return  j
#lomuto cagirir
def quickSortLomuto(arr):
    if (not arr or len(arr) == 1):
        return arr
    return helperSort2(arr, 0, len(arr) - 1)

#hoare cagirir
def quickSortHoare(arr) :

    if(not arr or len(arr) == 1):
        return arr
    return helperSort(arr,0,len(arr)-1)

#hoare icin helper
def helperSort(arr,first,last):
     if(last > first):
        indis = hoarePartition(arr,first,last)
        #print(arr)
        helperSort(arr,first,indis)
        helperSort(arr,indis+1,last)
        return arr

#lomuto icin helper
def helperSort2(arr, first, last):
    if (last > first):
        indis = lomutoPartition(arr, first, last)
       # print(arr)
        helperSort2(arr, first, indis)
        helperSort2(arr, indis + 1, last)
        return arr




arr = [15,4,68,24,75,16,42]
qsh = quickSortHoare(arr)
print(qsh,"\nass")
arr = [15,4,68,24,75,16,42]
qsh = quickSortLomuto(arr)
print(qsh)
