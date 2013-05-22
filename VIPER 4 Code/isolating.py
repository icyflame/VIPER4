##File number 2
##
##This file has the function that can take a line from the file which is
##passed to it as parameter and return the four fields that are there in it
##as separate variables.
##
##This is a part of the program in Python Tkinter
##
##created on 9th April, 2013


from newRec import *

import string

def isolate(i):

    i = str(i)

    i = i.strip('\n')

    this = 'username:'
    other = 'account:'

    ##username

    un = i[string.find(i,this) + len(this):string.find(i,other)]
    this = other
    other = 'password:'

    ##account
    ac = i[string.find(i,this) + len(this):string.find(i,other)]
    this = other
    other = 'remarks:'

    ##password
    pas = i[string.find(i,this) + len(this):string.find(i,other)]
    this = other
    other = '\n'

    ##remarks

    rem = i[string.find(i,this) + len(this):string.find(i,'\n')]
    rem = rem.strip('\n')
    #rem = i[string.find(i,this) + len(this):string.find(i,other)]

    return (un,ac,pas,rem)

##app = record()
##
##app.getFromUser()
##
##un,ac,pas,rem = isolate(str(app))
##
##print un
##print ac
##print pas
##print rem
