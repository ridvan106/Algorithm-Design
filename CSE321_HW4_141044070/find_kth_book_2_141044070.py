"""
    Rıdvan Demirci
        141044070
 -önce gelen 2 listenin boş olup olmama durumlarına bakıp o duruma
 göre dive yaparak zaten logk da bulur
 -diger durumda ise gelen listelerin ortanca elemanlarına bakar
 indis toplamları 1 den küçük ise her ikisininde ortadan sonraki listenin
 devamı gönderilir tekrar
 -eger kucuk ise ortadan sol degerler gonderilir 1 e esitse return degeri en kucuk olan
 olur




"""




def find_kth_book_2(m, n, k):
    if(not n):
        if (k == 1):
            return m[0]
        mid = int(len(m)/2)
        if((k-mid) == 1):
            return m[mid]
        elif(k -mid > 1):
            return find_kth_book_2(m[mid:], n, k - mid)
        return find_kth_book_2(m[1:], n, k - 1)
    elif(not m):
        if (k == 1):
            return n[0]
        mid = int(len(n) / 2)
        if ((k - mid) == 1):
            return n[mid]

        elif (k - mid > 1):
            return find_kth_book_2(m, n[mid:], k - mid)
        return find_kth_book_2(m, n[1:], k - 1)

    else:
        if(k == 1):
            if(m[0]<n[0]):
                return m[0]
            return n[0]
        mid1 = int(len(m) / 2)
        mid2 = int(len(n) / 2)
        cond = k -(mid1+mid2)
        if(cond > 1):
            return find_kth_book_2(m[mid1:],n[mid2:],cond)
        elif(cond ==1):
            if (m[mid1] < n[mid2]):
                return m[mid1]
            return n[mid2]
        elif(cond <1):
            if(m[mid1]<n[mid2]):
                return find_kth_book_2(m, n[:mid2], k)
            return find_kth_book_2(m, n[:mid1], k)




m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop","oor","oos"]
book = find_kth_book_2(m,n,5)
print(book)