def SwapPoosition(list,pos1,pos2):
    get=list[pos1],list[pos2]
    list[pos2],list[pos1]=get
    return list

#driver code
list=[1,2,3,4,5,6,7,8,9,10]
pos1=5
pos2=4
print(SwapPoosition(list,pos1-1,pos2-1))