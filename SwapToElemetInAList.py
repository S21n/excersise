def SwapPosition(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list

#Driver function
list=[23,65,19,90]
pos1,pos2=1,3
print(SwapPosition(list,pos1-1,pos2-1))
