#!/usr/bin/python3

### GLOBAL STRING ###

name = 'THIS IS A GLOBAL STRING'

def greet():
    
    name = "Sammy"
    def hello():
        print('Hello '+name)

    hello()


greet()