'''What is a correct syntax for looping through the items of a tuple?'''
for x in ('apple', 'banana', 'cherry'):
    print(x)

'''Insert the missing part of the while loop below to loop through the items of a tuple.'''
mytuple = ('apple', 'banana', 'cherry')
i = 0
while i < len(mytuple):
    print(mytuple[i])
    i = i + 1

'''Insert the missing part of the for loop below to loop through the items of a tuple by using the range function to loop through the tuple's index numbers.'''
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])