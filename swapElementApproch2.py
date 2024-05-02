def swapList(newList):
    newList[0],newList[-1]=newList[-1],newList[0]
    return newList
userList=input("Enter the list number")
newList=userList.split(',')
print(swapList(newList))