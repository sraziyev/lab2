'''Consider this syntax:
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
what will be a correct syntax for printing the name 'May'?'''
#print(customers['c2']['name']

'''Insert the missing part to loop through the keys and values of all nested dictionaries:'''
a = {'name' : 'John', 'age' : '20'}
b = {'name' : 'May', 'age' : '23'}
customers = {'c1' : a, 'c2' : b}
for x, obj in customers.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])

'''True or False. A dictionary can only have one level of nested dictionaries.'''
#False