#inistilize tuple
test_tuple =(1,3,5,6,7,9,2)
#printing original tuple
print("the original tuple : ",str(test_tuple))
#inisilizing k 
k=1
# maximum and minimum element in the tuple
#using shorted() +loop

res=[]
test_tuple=list(sorted(test_tuple))
for idx, val in enumerate(test_tuple):
    if idx < k or idx >= len(test_tuple) - k:
        res.append(val)
res = tuple(res)

print("The extracted values : " + str(res)) 

