#!/usr/bin/python3

### SIMPLE FUNCTION ###

def my_function():
  print("Hello World")

my_function()

### FUNCTION WITH AN ARGUMENT ###
def name_function(name):
    print("My name is " +name)

name_function("John Iacovacci")


### RETURN VALUE FROM FUNCTION ###
def my_function(x,y):
  return  x * y

print(my_function(3,5))

### FUNCTION WITH X ARGS ###
def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Jonathan","Michael")

### FUNCTION WITH KEY WORD ARGUMENTS ###

def my_function(child2, child1):
  print("The youngest child is " + child2)

my_function(child1 = "Jonathan", child2 = "Michael")

### ARBITARY KEY WORD ARGUMENTS ###

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Jonathan", lname = "Iacovacci")


