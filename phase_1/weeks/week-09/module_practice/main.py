# Goal: greet a user
# Input: user name
# Output: greeting and farewell
# Steps: create functions that can be called 
# Python concepts: function, import
import greetings

def acknowledge(name):  
    print(greetings.greet(name))
    print(greetings.farewell(name))

acknowledge("Fawo")