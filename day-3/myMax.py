def getmax(list1):
    max=-1
    if len(list1)==0:
        return max
    else:
        for i in range(len(list1)):
            if list1[i]>max:
                max=list1[i]
        return max 

