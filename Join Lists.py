'''What is a correct syntax for joining list1 and list2 into list3?'''

#list3 = list1 + list2

'''What is a correct syntax for adding elements from list2 into list1?'''
#list1.extend(list2)

'''Consider the following code:
list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
What will be the value of list1?'''
list1 = ['a', 'b' , 'c']
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
#['a', 'b', 'c', 1, 2, 3]