'''What is a correct syntax for joining tuple1 and tuple2 into tuple3?'''
#tuple3 = tuple1 + tuple2

'''What is a legal way to turn this tuple: (1,2,3) into this tuple:(1,2,3,1,2,3)?'''
tuple1 = (1,2,3)
tuple1 = tuple1 * 2

'''Consider the following code:
tuple1 = ('a', 'b' , 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple2 + tuple1
What will be the value of tuple3?'''

tuple1 = ('a', 'b' , 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple2 + tuple1
#(1, 2, 3, 'a', 'b', 'c')
