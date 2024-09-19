'''
Consider the following code:
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
What will be the value of newlist?'''
fruits = ['apple', 'banana', 'cherry']
newlist = [x for x in fruits if x == 'banana']
#['banana']

'''Fill in the missing parts to complete the list comprehension:'''
fruits = ["apple", "banana", "cherry"]
newlist = [x for x in fruits]

'''Consider the following code:
fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
What will be the value of newlist?'''
fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
#['apple','apple','apple']