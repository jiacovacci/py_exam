#!/usr/bin/python3

### CONTROL FLOW ###

### if test ###

a = 3
b = 5
print('if a = 3 and x = 5')
if b > a:
  print("b is greater than a")

### if elif test ###

a = 6
b = 5
print('elsif a = 6 and x = 5')
if b > a:
   print("b is greater than a")
elif a > b:
    print("a is greater than b")

### if elif else test ###

a = 5
b = 5
print('else a = 5 and x = 5')
if b > a:
   print("b is greater than a")
elif a > b:
   print("a is greater than b")
else:
       print("a is equal to b")


### FOR NEXT ###

print('for next loop')
my_list = ['a','b','c','d','e']
for it_name in my_list:
    print (it_name)

### looping thru a string ###
print('looping thru string')

for x in "orange":
  print(x)

print('fomatting loop thru string')

index_count = 0
for letter in 'orange':
  print('At index {} the letter is {}'.format(index_count,letter))
  index_count += 1

### while loops ###
print('while loop')

i = 1
while i < 5:
  print(i)
  i += 1


### while loop break ###
print('while loop break')

i = 1
while i < 5:
  print(i)
  if i == 3:
    break
  i += 1

