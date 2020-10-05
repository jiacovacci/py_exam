#!/usr/bin/python3

### List Example ###
print('loop thru list')
my_list = ['d','e','f','a','b']
for it_name in my_list:
    print (it_name)

### RANGE ###
print('range starting at position 2 upto but not including position 4')
print(my_list[2:4])

#Remember that the first item is position 0,
#and note that the item in position 4 is NOT included

### REPLACE ITEM ###

print('replace position 1 with z')

my_list[1] = 'z'
print(my_list)

### LENGTH ###

print('length of list')

print(len(my_list))

### SORT METHOD ###

print('sort the list')
my_list.sort()

print(my_list)

### TUPLE ###

print('loop thru tuple')
my_list = ('d','e','f','a','b')
for it_name in my_list:
    print (it_name)

########## DICTIONARY #################

print('dictionary example')

x = {"name" : "John", "email" : "john.iacovacci1@gmail.com"}
print (x['name'])
print(type(x))
