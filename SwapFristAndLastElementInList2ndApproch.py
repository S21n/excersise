def swapPosition(list,pos1,pos2):
    #poping both of the element from the list
    temp1 = list.pop(pos1)
    temp2 = list.pop(pos2-1)
    #inserting the element at the position of the other element 
    list.insert(pos1,temp2)
    list.insert(pos2,temp1)
    return list
#Driver code
list = [1,2,3,4,5,6,7,8,9,10]
print(swapPosition(list,1,3))
