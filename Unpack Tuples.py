'''Consider the following code:
fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)
What will be the value of y?'''
fruits = ('apple', 'banana', 'cherry')
(x, y, z) = fruits
print(y)
#banana

'''Consider the following code:
fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)
What will be the value of y?'''
fruits = ('apple', 'banana', 'cherry')
(x, *y) = fruits
print(y)
#['banana', 'cherry']

'''Consider the following code:
fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)
What will be the value of y?'''
fruits = ('apple', 'banana', 'cherry', 'mango')
(x, *y, z) = fruits
print(y)
#['banana', 'cherry']