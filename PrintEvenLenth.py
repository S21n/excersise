def Evenlen(string):
    #split the string
    string=string.split(' ')
    #loop through the string
    for i in string:
        #check if the length of the string is even
        if len(i)%2==0:
            print(i)

#driver code
string=input("enter string")
#function call
Evenlen(string)