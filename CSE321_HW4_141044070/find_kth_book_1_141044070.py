"""
    Rıdvan Demirci
        141044070
kodun basinda listelerden herhangi biri bos gelme ihtimaline karsi
gelen m ve n listelerinin bos olup olmama durumları kontrol edilip
gonderilir...
daha sonra listenin baş kısımları karşılaştırılır küçük olan kısımdan
k==1 ise cevap kucuk olandır eger k==1 degil ise
kucuk olan arrayin orta tarafı tekrar gonderilir.... boyle her iterationda
2 arrayden birinin yarısı gittiği için O(logn + logm)'olur






"""

def find_kth_book_1(m,n,k):
    if(not n):
        if (k == 1):
            return m[0]
        mid = int(len(m)/2)
        if((k-mid) == 1):
            return m[mid]
        elif(k -mid > 1):
            return find_kth_book_1(m[mid:], n, k - mid)
        return find_kth_book_1(m[1:], n, k - 1)
    elif(not m):
        if (k == 1):
            return n[0]
        mid = int(len(n) / 2)
        if ((k - mid) == 1):
            return n[mid]

        elif (k - mid > 1):
            return find_kth_book_1(m, n[mid:], k - mid)
        return find_kth_book_1(m, n[1:], k - 1)
#--------------------------------------------------------------------
    else:
        if(m[0] < n[0]):
            if(k == 1):
                return m[0]
            mid = int(len(m) / 2)
            if(m[mid]<n[0] and not(mid==0) and (k-mid >=1)):
                return find_kth_book_1(m[mid:], n, k - mid)
            return find_kth_book_1(m[1:],n,k-1)
        else:
            if(k == 1):
                return n[0]
            mid = int(len(n) / 2)
            if (n[mid] < m[0] and not(mid==0) and (k-mid >=1)):
                return find_kth_book_1(m, n[mid:], k - mid)
            return find_kth_book_1(m, n[1:], k-1)


m = ["algotihm", "programminglanguages", "systemsprogramming"]
n = ["computergraphics", "cprogramming","oop","oor","oos"]
book = find_kth_book_1(m,n,7)
print(book)