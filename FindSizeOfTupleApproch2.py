#sample tuple
tuple1=(1,2,3,4,5,6,7,8,9,0)
tuple2=(0,9,8,7,6,5,4,3,2,1)
tuple3=(1,3,5,7,9)
Tuple4 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek", "Deepanshu")

#printing the size of tuple 1.Using inbuilt __sizeof__() method:
print("the size of tuple1 :"+str(tuple1.__sizeof__())+"bytes")
print("the size of tuple2 :"+str(tuple2.__sizeof__())+"bytes")
print("the size of tuple3 :"+str(tuple3.__sizeof__())+"bytes")
print("the size of tuple4 :"+str(Tuple4.__sizeof__())+ "bytes")