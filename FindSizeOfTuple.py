import sys
#sample tuple
tuple1=(1,2,3,4,5,6,7,8,9,0)
tuple2=(0,9,8,7,6,5,4,3,2,1)
tuple3=(1,3,5,7,9)
Tuple4 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek", "Deepanshu")

#printing the size of tuple using getsizeof() function
print("the size of tuple1 :",sys.getsizeof(tuple1))
print("the size of tuple2 :",sys.getsizeof(tuple2))
print("the size of tuple3 :",sys.getsizeof(tuple3))
print("the size of tuple4 :" + str(sys.getsizeof(Tuple4))+ "bytes")
 