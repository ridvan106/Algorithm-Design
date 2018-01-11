"""
Rıdvan Demirci
    141044070
    
    dived and conquere ile array en alt duzeye kadar ayrılır
    daha sonra karsilastirma oncekiler ile karsilastirilarak geri gelir

- worst case için sitringlerin tamamı aynı olması string boyutu m olursa
worstcase:O(mlogn) olur



"""

def common_postfix(inpA,inpB):#posfix karsilastirilmasi yapilir,constant diye dusunulur
    size1 = len(inpA)-1
    size2 = len(inpB)-1
    tempWord = ""
    flag = True
    while(size1 >=0 and size2 >=0 and flag):
        if(inpA[size1] == inpB[size2]):
            tempWord = inpA[size1]+tempWord
            size1 -= 1
            size2 -= 1
        else:
            flag = False

    return tempWord
def helper(inpStrings):#arrayi dived eden bolum
    if (len(inpStrings) <= 1):
        return inpStrings[0]
    else:
        mid = int(len(inpStrings) / 2)  # tam orta degeri

        leftSide = longest_common_postfix(inpStrings[0:mid])
        rightSide = longest_common_postfix(inpStrings[mid:])
        print(leftSide,rightSide)
        res = common_postfix(leftSide,rightSide)
       # print("res",res)
        if(res == ""):
            return ""
        return res
def longest_common_postfix(inpStrings):
    val = helper(inpStrings)
    if(val == ""):
        return "no match postfix word"
    return val


"""inpStrings = ["bash", "trash", "backslash","flash"]"""
inpStrings = ["absorptivity", "circularity", "electricity", " importunity", "humanity"]
"""inpStrings = ["gürcistan","bulgaristan","ermenistan","macaristan","endoneztan"]"""
lcp = longest_common_postfix(inpStrings)
print("result",lcp)
