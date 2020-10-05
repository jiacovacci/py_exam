#!/usr/bin/python3

### LOCAL STRING  ###

name = "Jonathan"

def hello():
    #LOCAL
    name = 'I AM LOCAL'
    print('Hello '+name)

hello()

### GLOBAL STRING ###

name = 'THIS IS A GLOBAL STRING'

def greet():
    
    name = "Sammy"
    def hello():
        print('Hello '+name)

    hello()

greet()