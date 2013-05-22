##VIPER 4.0
##
##CREATED BY SIDDHARTH KANNAN
##
##WRITTEN ON PYTHON 2.7 AND TKINTER 8.5
##
##OS:LINUX MINT 14 NADIA


##     This program is free software. It comes without any warranty, to
##     the extent permitted by applicable law. You can redistribute it
##     and/or modify it under the terms of the Do What The Fuck You Want
##     To Public License, Version 2, as published by Sam Hocevar. See
##     http://www.wtfpl.net/ for more details.


##Main File
##
##Main file for VIPER 4 GUI using Tkinter 8.5 and Written in Python 2.7
##
##Revision history for this file is as so:
##
##created 8th April, 2013
##
##    changes:
##
##        created the VIPER class and defined some functions in it.
##
##        created the display function that displayed all the records stored inside the console
##        and not inside the window as i want it to be. schedule is to change it the next time
##        you log in.
##
##Modified 9th April, 2013
##
##    changes:
##
##        changed the function that displays all the records inside the window and
##        made 2 new functions that initiated the frame readied to be packed or to be gridded
##
##        created the isolating,opy file and modified the function here to make sure that
##        now: one line in the data consists of one complete record.
##
##        also integrated the two files isolating.py and the file newRec.py more
##        deeply into the main run of the program.
##
##        added a button inside the function that displays all the records without their
##        passwords that will take the user back to the main menu.
##
##        added one more button that will delete all the records by deleteing the file
##        and also added the associated functions for the same
##        and the confirmation will be taken from the user using the built in
##        message box library
##
##Modified 10th April, 2013
##
##    changes:
##        found a bug in the isolating.py file that had to be changed.
##        the object that we were accepting: we were not making sure that
##        it was a string before aplying the string command and the library
##        functions defined under the string library.
##
##        added one more button that will show a table and then in that table
##        buttons so that the user can see all the details of any one particular account
##        by pressing the button that is there in front of that account
##
##
##        added specifications to all the functions so that they can be easily accessed
##        and their function understood at a later stage
##
##Modified 11th April, 2013
##
##    changes:
##
##        added one more button that would allow the user to modify an account
##
##        created the modifying.py file that consists the function for the modifying part of
##        the program
##
##        the file was completed successfully
##
##        but the intergration into the main file not complete as on 15:30 on 11th April, 2013
##
##Modified 12th April, 2013
##
##    changes:
##
##        major errors found in both the modules modifying and newrec
##        these errors call for a major overhaul in the whole algorithm that
##        was designed for modifying a record
##        and major error found in mainFile: which implies that whenever any'Modify This'
##        button is pressed always the last record is selected for modifcation.
##
##        this needs to be changed.
##
##Modified 14th April, 2013
##
##    changes:
##
##        class name of getInput has been appropriately changed to record()
##        and necessart changes made in all the related files.
##
##        major changes in the implementation of the modifying algorithm.
##        the previous algorithm was most probably wrong. and thus has been
##        changed to a new algorithm. the class modifyRec has been defined inside
##        the file modifying.py and the function of this class has been
##        wrapped up in a function modRec which will take either the record()
##        instance as a parameter or the string equivalent of a record instance.
##
##        changes were made in the newRec.py file also in which the class
##        method stringToObject has been changed so as to include the case in which
##        the parameter passed to the function is a record object and not a string.
##
##        changes are yet to be made in the mainFIle to accomodate all the new modiying
##        algorithms and a method needs to be deviced so that the user can select the
##        record that he wants to change rather than the last record each time
##        as was happenning in the previous algorithm.
##
##Modified 15th April, 2013
##
##    changes:
##        major mistakes found in all the three functions in which the records
##        are shown. have to make major changes to the algorithms as in this case
##        whatever button be pressed we will always be working with the last record.
##
##        possibly use a list of checkbuttons and then check which of the heck buttons
##        have been set to on and then display only these records
##
##Modified 16th April, 2013
##
##    changes:
##        decided that check buttons can't be used and only way out is to ask the
##        user to for the number of the record whose details he wants to see,
##        just like in VIPER 3.0.
##        will continue to work on a GUI solution for this.
##
##        question on stack overflow gives an elegant solution. create a seprate
##        function for each record. will use this in all three operations
##        1. see
##        2. modify
##        3. delete one specific account.
##
##Modified 17th April, 2013
##
##    changes:
##
##        all major mistakes were rectified and after thourough testing decided on
##        14:58 that there are no more bugs in either the modify function. all
##        the testing code was removed from this file. minor changes were made
##        in the seeAllRecordsWithoutPasswords function as it was found that
##        the variable 'thisrecord' was not taking the last character in remarks
##        due to an unknown reason while it showed the whole record to the user.
##        the changed have now rectified this and it is working now.
##
##        changes were made to the modifying module so that if the user enters
##        a PERIOD '.' then the value of the field will be retained as earilier.
##
##        as of 15:25 on 17th April, 2013 all the functions have been tested and
##        found to work correctly.
##
##Modified 20th April, 2013
##
##    changes:
##
##        added the button that will allow the user to delete any one account.
##
##        also added the two functions that are required for it.
##
##        changed the source code so as to segment things and get to things
##        more easily.
##
##        only the masterkey prompt at required places now remains.'
##
##Modified 21st April, 2013
##
##    changes:
##
##        all the master key integration that had to be done was completed. The
##        default masterkey was set to 'abcd'. A new button to change the
##        master key has been added to the main menu.
##
##Modified 22nd April, 2013
##
##    changes:
##
##        the masterkey integration has been checked.
##
##        the exit screen orientation and presentation is remaining.
##
##        the program will now have a SHA1 encryption on the master key as entered
##        by the user. I am looking for a way to encrypt the user information too.
##
##        the exiting window has been configured and when the escape key is pressed
##        then the program will end and it will show a credits screen. this screen
##        will end after 8 seconds.
##
##Modified 23rd April, 2013
##
##    changes:
##
##        added a salt to the master key before storing into the file. this
##        ensures that the data will remain safe.
##
##        Major bug spotted in the self.checkpoint function. The problem is that
##        once the execution of self.checkpoint is done then the control gets shifted back
##        and this means that even unauthorised users can make changes to the file
##        and the program will not be able to stop this. posted a stack overflow question
##        to this effect. awaiting an answer: 1532 hrs.
##
##Modified 24th April, 2013
##
##    changes:
##
##        changes were made to the checkpoint function. decision made that the
##        changes are as so:
##
##            1. on unauthorised access. A dialog will be given to user and
##              the application will quit.
##
##            2. salt was added as mentioned earlier. and appropriate changes were
##              made in the change master key function too.
##
##        the software is now ready for release. encryption on data will be
##        done in the next release and not in this one. this release will be with
##        linux and windows executables.
##
##Modified 26th April, 2013
##
##    changes:
##
##        more changes were made to this file just before release. I added a dialog
##        after a new record is stored and also when the master key file is not
##        available in the memory.
##
##Modified 27th April, 2013
##
##    changes:
##
##        more changes so as to make the application full screen with the topbar.
##        changes made in new record and modifying modules regarding this.


        
from Tkinter import *

from newRec import *

from isolating import *

from modifying import *

from hashlib import *

import tkMessageBox

import tkSimpleDialog

import tkFont

import string

fileName = 'viper'

salt = 'developedbysiddharthkannan'

SHOW_TOPBAR = True  ##varibale will control whether the top bar with the three close, minimise, restore buttons
                    ##will be shown or not.

CHANGE_SIZE = True

def setDefault():

    '''sets the default masterkey to \'abcd\''''

    m = 'abcd'

    m = m + salt

    m = sha1(m)
    m = m.hexdigest()

    filin = open('mast','w')

    filin.write(m)

    filin.close()

#setDefault()

class VIPER(object):
    def __init__(self):

        '''class function that will initialise an object'''

        self.window = Tk()

        self.window.title('Visual Interface for Password Entry and Retreival')

        self.big = tkFont.Font(family='Helvetica',size=20)

        root = self.window

        # make it cover the entire screen
        w, h = root.winfo_screenwidth(), root.winfo_screenheight()
        root.overrideredirect(not SHOW_TOPBAR)
        root.geometry("%dx%d+0+0" % (w, h))


        self.w = w
        self.h = h

        self.listofcbs = []
        self.initBindings()

        self.initFiles()

        self.initFrameAndButtons()


    ################################

##      FUNCTIONS FOR INITIALISING

    ################################

    def initFiles(self):

        try:
            a = open(fileName,'r')

        except IOError:

            a = open(fileName,'w')


        a.close()

        try:
            a = open('mast','r')

        except IOError:

            setDefault()
            

    def initBindings(self):

        self.window.bind('<Escape>',self.quitwin)

    def initFrame(self):

        '''initialises the frame using the pack method

           ideal for all kinds of activities with buttons or labels'''

        try:
            self.frame.destroy()

        except:
            pass

        self.frame = Frame(self.window,width=600,height=500)
        self.frame.pack()
        self.frame.pack_propagate(not CHANGE_SIZE)

    def initFrameAndButtons(self):

        '''this function will initialise the frame and also the buttons
            that are a part of VIPER's main menu'''

        self.initFrame()

        self.initButtons()

    def initFrameForTableDisplay(self):


        '''initialises the frame using the grid method.
            this is ideal to create things like tables and other
            ways that may be used to present tabular data to the user'''

        try:
            self.frame.destroy()

        except:
            pass

        self.frame = Frame(self.window,width=500,height=500)
        self.frame.grid()

        if self.getnumrec() > 10:
            self.frame.grid_propagate(1)

        else:
            self.frame.grid_propagate(0)

    def initButtons(self):

        '''function that will initialise all the buttons into the main frame.
            must be called only after any one of the frame initialising
            functions are called'''

        ##Button for new record

        listOfButtons = []

        listOfButtons.append(Button(self.frame,text='Enter a new record',command=self.getNewRec))
        listOfButtons.append(Button(self.frame,text='See all the stored records',command=self.seeAllRecordsWithoutPassword))
        listOfButtons.append(Button(self.frame,text='See the password of an account',command=self.showTableForSeeing))
        listOfButtons.append(Button(self.frame,text='Modify an account',command=self.modify))
        listOfButtons.append(Button(self.frame,text='Delete an account',command=self.delAcc))
        listOfButtons.append(Button(self.frame,text='See the number of records stored in file',command=self.showNumRec))
        listOfButtons.append(Button(self.frame,text='Change the master key',command=self.changeMastKey))
        listOfButtons.append(Button(self.frame,text='Delete all records',fg='white',bg='red',command=self.confirmDelete))
        listOfButtons.append(Button(self.frame,text='QUIT',fg='red',bg='black',command=self.quitwin))


        for i in range(len(listOfButtons)):

            listOfButtons[i].config(font=self.big)

            listOfButtons[i].pack(side='top')


    ###################################

##      GENERAL FUNCTIONS

    ###################################


    def reinitialise(self):

        '''this will delete the existing frame and initialise a new frame
            along with all the buttons as they were on the main menu'''

        self.frame.destroy()

        self.initFrameAndButtons()


    def show(self,record='',ev=None):

        '''this will show the user the details of the account that he has decided
            to view'''
        
        tkMessageBox.showinfo('Details of selected account',record)
                    

    def rearrangeFiles(self):

        '''will remove the basic file and rename the file temp as viper'''

        import os

        os.remove(fileName)

        os.rename('temp',fileName)

    def checkpoint(self):

##        tkMessageBox.showinfo('Checkpoint','Checkpoint encountered')
##        return

        ##first take the masterKey from the file

        try:

            inFile = open('mast','r')

        except IOError:

            self.quitwin()

            tkMessageBox.showinfo('sorry','The master key file is not available.\
We are unable to proceed. Go to siddharthkannan.webs.com and download the default\
 master key file. Goodbye')

            import sys
            sys.exit()

        M = inFile.read()

        inFile.close()

        temp = tkSimpleDialog.askstring('master key','Enter your master key:',show='*')

        temp = temp + salt

        temp = sha1(temp)

        temp = temp.hexdigest()

        if not temp == M:

            self.unauthorised()

            tkMessageBox.showinfo('access denied','Unauthorised access has been \
detected. Sorry. We can\'t allow you to continue. Goodbye.')

            self.window.destroy()

            import sys
            sys.exit()

        else:

            return

    #############################

##          NEW RECORD

    #############################    


    def getNewRec(self):

        '''this function will take a new record from the user and check if
            all the fields are empty. if this is the case then the new record will
            not be written to the file and the user will be given a message
            reflecting this'''


        self.checkpoint()

        app = record()

        self.win = self.window

        self.win.withdraw()

        app.getFromUser()

        a = isolate(app)

        isEmpty = True

        for i in a:
            if i != '':
                isEmpty = False

        if isEmpty:
            tkMessageBox.showinfo('Warning','The record you entered has all \
fields empty. We will not write it to the file')

            self.win.update()
            self.win.deiconify()

            return

        out = open(fileName,'a')

        out.write(str(app))

        out.close()

        tkMessageBox.showinfo('Success','The operation was successful. The new record\
 was written to file')
        
        self.win.deiconify()


    ###########################################

##     SEE RECORDS WITHOUT PASSWORD(TABLE)

    ###########################################

    def seeAllRecordsWithoutPassword(self):

        '''this will initialise a table that will show all the accounts
            with only the usernames and the accounts'''

        inFile = open(fileName,'r')

        #self.checkpoint()

        startRow = 0
        serialColumn = 1
        unColumn = 2
        acColumn = 3

        self.frame.destroy()

        self.initFrameForTableDisplay()    

        counter = startRow + 1

        #print self.w, self.h

        
        Label(self.frame,text='SERIAL').grid(row=startRow,column=serialColumn)
        Label(self.frame,text='USERNAME').grid(row=startRow,column=unColumn)
        Label(self.frame,text='ACCOUNT').grid(row=startRow,column=acColumn)
        


        for i in inFile:  ##i contains one full record with all the parameters in a record

            un,ac,pas,rem = isolate(i)

            a = isolate(i)

            Label(self.frame,text=str(counter-startRow),width=5).grid(row=counter,column=serialColumn)

            j = un
            Label(self.frame,text=j).grid(row=counter,column=unColumn)


            j = ac
            Label(self.frame,text=j).grid(row=counter,column=acColumn)

            counter += 1

        inFile.close()

        counter += 2

        Button(self.frame,text='Back To Main Menu',command=self.reinitialise).grid(row=counter,column=2)

    #########################################

##      SEEING THE DETAILS OF ANY ACCOUNT

    ##########################################


    def showTableForSeeing(self):

        '''this function will give the user the option to see the complete
            details of any one of the records using a series of buttons'''


        self.seeAllRecordsWithoutPassword()

        buttons = []

        inFile = open(fileName,'r')

        for i in inFile:

            un,ac,pas,rem = isolate(i)

            a = isolate(i)

            thisrecord = 'Username:' + un + '\nAccount:' + ac + '\nPassword:'\
                         + pas + '\nRemarks:' + rem
            
            buttons.append(Button(self.frame,text='See details',\
                                   command=self.callbackForShow(thisrecord)))

        counter = 0

        for i in buttons:            

            i.grid(row=counter + 1,column=4)
            counter += 1


    def callbackForShow(self,thisrecord):
        
        """ returns a callback for self.show """
        def callback():                 # make a new function
            self.checkpoint()       # check if the user is authorised
            self.show(thisrecord)    # that shows the given record
        return callback                 # return this function


    #######################################

##      MODIFY AN ACCOUNT

    #######################################

    def modify(self):
        '''allows to modify any one field'''

        self.seeAllRecordsWithoutPassword()

        buttons = []

        inFile = open(fileName,'r')

        for i in inFile:

            old = record()

            old.stringToObject(i)

            un = old.un
            ac = old.acc
            pas = old.pas
            rem = old.remarks

            thisrecord = str(old)
            
            buttons.append(Button(self.frame,text='Modify Record',\
                                   command=self.callbackForModify(thisrecord)))

        counter = 0

        inFile.close()

        for i in buttons:            

            i.grid(row=counter + 1,column=4)
            counter += 1

    def callbackForModify(self,thisrecord):

        '''returns functions that can be used to modify a record'''

        def callback():

            self.checkpoint()

            self.window.withdraw()           

            newrec = modRec(thisrecord)

            if newrec.isEmpty():
                tkMessageBox.showinfo('warning','all fields of new record are \
empty. we will not make any changes to the file')

                self.window.deiconify()
                return

            if str(newrec) == thisrecord:
                tkMessageBox.showinfo('no changes made','no changes were made \
to the original record. no changed will be made in the file too.')

                self.window.deiconify()
                return

            filin = open(fileName,'r')            

            filout = open('temp','w')

            for i in filin:

                if i == thisrecord:

                    filout.write(str(newrec))
                    continue

                filout.write(i)

            filin.close()

            filout.close()

            self.rearrangeFiles()

            tkMessageBox.showinfo('message','the record was modified')

            self.window.deiconify()

            self.modify()    

        return callback

    #######################################

##      DELETE ANY ONE ACCOUNT

    #######################################

    def delAcc(self):
        '''will give the user a method to delete any one account
            from a list of accounts'''

        self.seeAllRecordsWithoutPassword()

        buttons = []

        inFile = open(fileName,'r')

        for i in inFile:

            old = record()

            old.stringToObject(i)

            un = old.un
            ac = old.acc
            pas = old.pas
            rem = old.remarks

            thisrecord = str(old)
            
            buttons.append(Button(self.frame,text='Delete this Record',\
                                   command=self.callbackForDelete(thisrecord)))

        counter = 0

        inFile.close()

        for i in buttons:            

            i.grid(row=counter + 1,column=4)
            counter += 1

    def callbackForDelete(self,thisrecord):

        '''returns functions that can be used to delete a record'''

        def callback():

            self.checkpoint()

            inFile = open(fileName,'r')

            out = open('temp','w')

            flag = False  ##flag will be set to true if the user has deleted an account

            for i in inFile:

                if i == thisrecord:

                    un,ac,pas,rem = isolate(i)

                    message = 'Username:' + un + '\nAccount:' + ac + '\nPassw\
ord:'\
                                 + pas + '\nRemarks:' + rem + '\n\n' + \
'you have chosen to delete this account. are you sure?'



                    
                    if not tkMessageBox.askyesno('confirmation',message):

                        ##user chose not to delete the record                      

                        tkMessageBox.showinfo('confirmed','the record was not deleted')                        

                        break

                    else:

                        flag = True

                        ##user chose to delete the record

                        message = 'Username:' + un + '\nAccount:' + ac + '\nPassw\
ord:'\
                                 + pas + '\nRemarks:' + rem + '\n\n' + \
'This record has now been deleted.'

                        tkMessageBox.showinfo('deleted',message)

                        continue


                out.write(i)

                

            out.close()

            inFile.close()

            if flag:
                self.rearrangeFiles()

            else:

                import os
                os.remove('temp')

            
            self.delAcc()                

        return callback


    #####################################

##      NUMBER OF RECORDS STORED

    #####################################

    def showNumRec(self):

        tkMessageBox.showinfo('Number of records','The total number of records \
are: %s' % str(self.getnumrec()))

    def getnumrec(self):

        '''returns the number of records stored in the file'''

        inFile = open(fileName,'r')

        x = 0

        for i in inFile:
            x+=1

        return x

    ##########################

##      CHANGE MASTER KEY

    ##########################

    def changeMastKey(self):

        self.checkpoint()

        attempt1 = tkSimpleDialog.askstring('new master key','Enter the new master key:',show='*')

        if len(attempt1) < 4:
            tkMessageBox.showinfo('failure','minimum length of master key is 4 charachters')
            self.initFrameAndButtons()
            return

        attempt2 = tkSimpleDialog.askstring('confirm new master key','Re-enter the new master key:',show='*')

        if not attempt1 == attempt2:

            tkMessageBox.showinfo('Failure','The two master keys you entered are not the same. \
\nThe master key was not changed. \nTry again.')

            self.initFrameAndButtons()
            return False

        inFile = open('mast','w')

        attempt1 = attempt1 + salt

        att = sha1(attempt1)
        att = att.hexdigest()

        inFile.write(att)

        inFile.close()

##        print 'new:',att

        self.initFrameAndButtons() 
        


    ########################################

##      DELETE ALL ACCOUNTS

    #####################################

    def confirmDelete(self):

        '''function that will confirm the delete all records option from the user'''

        self.checkpoint()

        self.frame.destroy()

        self.initFrame()

        if tkMessageBox.askyesno('Confirmation','Are you sure you want to delete all the records?'):
            self.resetAll()

        else:
            self.initFrameAndButtons()

    def resetAll(self):


        '''deletes all the records stored till now, must not be called directly
            must be called only through the confirmDelete function that will
            give the user a choice to delete all the records'''

        inFile = open(fileName,'w')

        inFile.close()

        tkMessageBox.showinfo('confirmation','All the records have been deleted')

        self.initFrameAndButtons()


    ##############################

##      EXITING THE APPLICATION

    ##############################

    def unauthorised(self,ev=None):

        '''will be called if the user enters the wrong master password'''

        self.frame.destroy()

        self.initFrameForTableDisplay()

        self.frame.grid_propagate(1)

        self.big  = tkFont.Font(family='helvetica',size=24)

        r = self.frame

        c = 0
        
        Label(r,text='Unauthorised access detected. Goodbye',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Created by Siddharth Kannan',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Written on Python 2.7 and Tkinter 8.5',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='OS: LINUX MINT 14 NADIA',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='This software is licensed under the WTFPL license.',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='See the copying file for more details.',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Application will quit in 8 seconds.',font=self.big).grid(row=c,column=0)
        c+=1        

    def quitwin(self,event=None):

        '''function that will destroy the present window and then create a new
            window that will give the credits'''

##        self.window.destroy()

        self.frame.destroy()

        self.initFrameForTableDisplay()

        #self.frame.config(width=500,height=500)

        self.frame.grid_propagate(1)

        self.big  = tkFont.Font(family='helvetica',size=24)

        r = self.frame

        c = 0

        Label(r,text='Created by Siddharth Kannan',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Written on Python 2.7 and Tkinter 8.5',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='OS: LINUX MINT 14 NADIA',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='This software is licensed under the WTFPL license.',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='See the copying file for more details.',font=self.big).grid(row=c,column=0)
        c+=1
        Label(r,text='Application will quit in 8 seconds.',font=self.big).grid(row=c,column=0)
        c+=1   

        self.window.after(8000,self.window.destroy)


app = VIPER()

mainloop()
