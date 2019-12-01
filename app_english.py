from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import time
from tkinter import ttk
from random import *
import smtplib
import pickle
import os
from tkinter import filedialog as fd
import datetime
from datetime import timedelta
from statistics import mean
import pyttsx3
from pyttsx.engine import Engine
import speech_recognition as sr
import base64
import pyaudio
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from googletrans import Translator


#!/usr/bin/env python
# -*- coding: utf-8 -*-


USERDANE = {"admin":["admin" , "admin"]}
USERWARD = {"admin":["ENGLISH WARD" , "POLISH WARD" , 0,0]}
fname = "USERDANE.py"

key_file ='key.key'

if os.path.isfile(key_file):
    print("Key does exist at this time")
else:
        key = Fernet.generate_key()
        file = open('key.key', 'wb')
        file.write(key)
        file.close()

if os.path.isfile(fname):
    print("file does exist at this time")
else:
    pickle.dump( USERDANE, open( "USERDANE.py", "wb" ))
    pickle.dump( USERWARD, open( "USERWARD.py", "wb" ))
    USERDANE = pickle.load(open("USERDANE.py" , "rb"))
    with open("USERWARD.py", 'rb') as f1:
        data1 = f1.read()
    user =list(USERDANE)
    password_provided = user[0]
    password = password_provided.encode() 
    salt = b'\xc4:\xe3\xa9\x14x` ?\xee\xa7\xa7\xd3 >h' 
    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                        backend=default_backend()
                        )
    key = base64.urlsafe_b64encode(kdf.derive(password))  
    val_ferenet = Fernet(key)
    encrypted = val_ferenet.encrypt(data1)
    with open("USERWARD.py", 'wb') as f1:
        f1.write(encrypted)
    pickle.dump( USERDANE, open( "USERDANE.py", "wb" ))
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    with open('USERDANE.py', 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open('USERDANE.py', 'wb') as f:
        f.write(encrypted)

try:
      
        USERDANE = pickle.load(open("USERDANE.py" , "rb"))
        pickle.dump( USERDANE, open( "USERDANE.py", "wb" ))
        file = open('key.key', 'rb')
        key = file.read()
        file.close()
        with open('USERDANE.py', 'rb') as f:
                data = f.read()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        with open('USERDANE.py', 'wb') as f:
                f.write(encrypted)
except:
        print("działa")

           

class Users:

    def __init__(self ):
        self.win =Tk()
        self.win.withdraw()    
        self.Master = Toplevel()
        self.Master.title ('ENgliSh WORD')
        self.Master.resizable( width = False , height= False)
        self.Master.configure(bg='white')
        self.Master.geometry ('650x500+0+0')
        self.frame1 = Frame (self.Master , bg='white')
        self.frame1.place( relwidth = 1 , relheight = 1 )
        self.Log = ""
        self.pasw = []

        DateofOrder = StringVar()
        DateofOrder.set(str(time.strftime("     %d/%m/%Y")))
        file = open('key.key', 'rb')
        key = file.read()
        
        
        with open('USERDANE.py', 'rb') as f:
                data = f.read()
        fernet = Fernet(key)
        dencrypted = fernet.decrypt(data)
        with open('USERDANE.py', 'wb') as f:
                f.write(dencrypted)
 

        def Login():
            
            USERDANE = pickle.load(open("USERDANE.py" , "rb"))
            self.Log = "{}".format(self.txtUser.get())
            self.pasw = self.txtPassword.get() 
            password_provided = self.txtUser.get()
            password = password_provided.encode() 
            salt = b'\xc4:\xe3\xa9\x14x` ?\xee\xa7\xa7\xd3 >h' 
            kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                        backend=default_backend()
                        )
            key = base64.urlsafe_b64encode(kdf.derive(password)) 
            f = Fernet(key)
            try:
                decrypted = f.decrypt(USERDANE[self.Log] [3])
            except KeyError:
                    tkinter.messagebox.showinfo("FAILD" , "incorrect password or login")
            password = decrypted.decode()                     
            
            if self.Log in list(USERDANE) and password == self.pasw :               
                self.Master.destroy()
                self.app1 =WindowFILE(self.Log)
            else:
                tkinter.messagebox.showinfo("FAILD" , "incorrect password or login")
                self.txtPassword.delete(0, 'end')
                self.txtPassword.focus()
            
        def LoginEnter(event):
            USERDANE = pickle.load(open("USERDANE.py" , "rb"))
            self.Log = "{}".format(self.txtUser.get())
            self.pasw = self.txtPassword.get()
            password_provided = self.txtUser.get()
            password = password_provided.encode() 
            salt = b'\xc4:\xe3\xa9\x14x` ?\xee\xa7\xa7\xd3 >h' 
            kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                        backend=default_backend()
                        )
            key = base64.urlsafe_b64encode(kdf.derive(password))  

            f = Fernet(key)
            try:
                decrypted = f.decrypt(USERDANE[self.Log] [3])
            except KeyError:
                    tkinter.messagebox.showinfo("FAILD" , "incorrect password or login")
            password = decrypted.decode()           
            
            if self.Log in list(USERDANE) and password == self.pasw : 
                self.Master.destroy()            
                self.app1 =WindowFILE(self.Log)
            else:
                
                tkinter.messagebox.showinfo("FAILD" , "incorrect password or login")
                self.txtPassword.delete(0, 'end')
                self.txtPassword.focus()

        #======================================================================================================================
        self.frame3 = Frame (self.Master , bg='white' ,width =220 , height = 100)
        self.frame3.place( x=430 , y=0 )     

        self.background_image = PhotoImage(file = 'images.png')
        self.flagalabel = Label(self.frame1 , image = self.background_image  )
        self.flagalabel.place(anchor ='nw')
        
        self.flagalabel2 =Label(self.Master , image = self.background_image   )
        self.flagalabel2.place(x=650 ,y =500 ,  anchor ='se' )

        self.wersja = Label(self.frame3 , text ='version:', bg='white' , bd=1 , relief='ridge')
        self.wersja.grid(row=0 ,column =0  , ipadx= 30)

        self.aktu = Label(self.frame3 , text ='update date:', bg='white' , bd=1 , relief='ridge')
        self.aktu.grid(row=1 ,column =0 ,ipadx= 18)

        self.txtwersja = Label(self.frame3  , bd=1 , bg='white' , text='        1.0.0'  ,relief='ridge' , justify='left', anchor='w'  )
        self.txtwersja.grid(row=0 ,column =2 ,ipadx= 89) 

        self.txtaktu = Label(self.frame3  , bd=1 , bg='white' ,textvariable = DateofOrder  ,relief='ridge'  , anchor='w' )
        self.txtaktu.grid(row=1 ,column =2 ,ipadx= 77 , sticky = 'w') 

        def click( event):
            self.Master.destroy()
            self.app = WindowRecower()
             
        self.ForgPASS = Text(self.frame1 , font = ('arial' , 15 , 'bold' ), bd=0,cursor = "arrow")
        self.ForgPASS.insert('end' , 'recover password ')
        self.ForgPASS.place(x=100 , y=390)
        self.ForgPASS.tag_add("tag", "1.0", "1.16")
        self.ForgPASS.tag_config("tag" , foreground="blue")
        self.ForgPASS.tag_bind("tag" ,"<Button-1>",click)


        def regist( event):
            self.Master.destroy()
            self.app = WindowREGISTER()
              
        self.ForgPASS = Text(self.frame1 , font = ('arial' , 15 , 'bold' ), bd=0 ,cursor = "arrow"  )
        self.ForgPASS.insert('end' , 'registration')
        self.ForgPASS.place(x=100 , y=430)
        self.ForgPASS.tag_add("tag", "1.0", "1.16")
        self.ForgPASS.tag_config("tag" , foreground="blue")
        self.ForgPASS.tag_bind("tag" ,"<Button-1>",regist)

        
        #==============================================================================================================================
              
        
        self.frame2 = Frame(self. Master  ,bg = 'white', bd=2, relief='ridge')
        self.frame2.place(relx=0.5 , rely = 0.5 , relwidth = 0.75 , relheight = 0.5 , anchor ='center')


        self.frame5 = Frame(self.frame2,bg = 'white')
        self.frame5.place(relx=0.15 , rely = 0.3 , relwidth = 0.7 , relheight = 0.4)

        #==========================================================================================================================

        self.lblUser = Label(self.frame5 , text ='LOGIN:', bg='white'  , font = ('arial' , 18 , 'bold') , bd=2 , relief='ridge')
        
        self.lblUser.grid(row=0 ,column =0 ,pady = 5, padx = 1 , sticky='w',ipadx=1, ipady=2)

        self.lblPassword = Label(self.frame5 , text ='PASSWORD:'  , bg='white' , bd=2 , relief='ridge',)
        
        self.lblPassword.grid(row=1 ,column =0 ,pady = 5, padx = 1 , sticky='w',ipadx=9, ipady=9 )

        self.txtUser = Entry(self.frame5  , bd=2 , bg='white' , font = ('arial' , 18 , 'bold')  ,relief='ridge'  )
        self.txtUser.grid(row=0 ,column =1 ,columnspan=2,pady = 5, padx = 2 , sticky='e',ipadx=1, ipady=2  ) 
        self.txtUser.focus()

        self.txtPassword = Entry(self.frame5  , bd=2 , bg='white' , font = ('arial' , 18 , 'bold'), show ='*'    ,relief='ridge'  )
        self.txtPassword.grid(row=1 ,column =1 ,columnspan=2,pady = 5, padx = 2 , sticky='e',ipadx=1, ipady=2 ) 

        self.lblPanel = Label(self.frame2 , text='Login panel' , bg='white' , font = ('arial' , 18 , 'bold'))
        self.lblPanel.grid(row=1 ,column =1 ,columnspan=2,pady = 15, padx = 50 , sticky='e')

        self.btnLogin =Button(self.frame2 , text='Login ' ,width=13, bg='grey' , font = ('arial' , 15 , 'bold'), bd=2 , command = Login )
        
        self.btnLogin.place(x=440 ,y =230 ,  anchor ='se')
        self.txtPassword.bind('<Return>', LoginEnter)

        def _destroy():
                if tkinter.messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
                        file = open('key.key', 'rb')
                        key = file.read()
                        with open('USERDANE.py', 'rb') as f:
                                data = f.read()
                        fernet = Fernet(key)
                        encrypted = fernet.encrypt(data)
                        with open('USERDANE.py', 'wb') as f:
                                f.write(encrypted)
                        self.Master.destroy()

        self.Master.protocol('WM_DELETE_WINDOW', _destroy)
        self.Master.mainloop()

class WindowREGISTER:
    def __init__(self ):
        self.Master = Toplevel()
        self.Master.title("REGISTRATION")
        self.Master.resizable( width = False , height= False)
        self.Master.geometry('700x700+0+0')
        self.Master.config(bg = 'white')
        self.frame1 = Frame(self.Master , bg ='white')
        self.frame1.place( relwidth = 1 , relheight = 1 )
        self.ROndomNUMBER = []
        self.User1 = []
        self.passw1 = []
        self.email = []
        self.passw2 = []
        Marks = ["!" , "@" , "#" , "$" , "%" , "&" , "&" , "*" ]
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

        


        #============================================dodać użytkownika=======================================================================
        def add_USER():
                   
            x=randint(10000 , 60000)
            randomRef = str(x)
            
            self.User1 = self.txtLOGIN.get()
            self.passw1 = self.txtPassward .get()
            self.passw2 = self.txtrPassward.get()
            self.email = self.txtE_MAIL.get()
            self.Firstname = self.txtFirstName.get()
            self.surname = self.txtSurName.get()
            self.scieint = self.cboStatus.get () 

            USERDANE = pickle.load(open("USERDANE.py" , "rb"))
            for users in list(USERDANE):
                    try:
                        with open("USERWARD.py", 'rb') as f:
                                data = f.read()

                        password_provided = "{}".format(users)
                        password = password_provided.encode() 
                        salt = b'\xc4:\xe3\xa9\x14x` ?\xee\xa7\xa7\xd3 >h' 
                        kdf = PBKDF2HMAC(
                                algorithm=hashes.SHA256(),
                                length=32,
                                salt=salt,
                                iterations=100000,
                                backend=default_backend()
                                )
                        key = base64.urlsafe_b64encode(kdf.derive(password))
                        val_ferenet = Fernet(key)
                        dencrypted = val_ferenet.decrypt(data)
                        with open('USERWARD.py', 'wb') as f1:
                                f1.write(dencrypted)

                        USERWARD = pickle.load(open("USERWARD.py" , "rb"))

                    except:
                            continue

            LETER = 0

            for leter in self.passw1:
                if leter in letters:
                    LETER += 1
            MARKS = 0
            for leter1 in self.passw1:
                if leter1 in Marks:
                    MARKS += 1
            EMAILCOUNT = 0
            for val in list(USERDANE.values()):
                
                if self.email in val:

                    EMAILCOUNT +=1

            if self.User1  not in list(USERDANE) and MARKS >=1 and  LETER >= 1 and self.passw1 == self.passw2 and EMAILCOUNT ==0:
                self.ROndomNUMBER.clear()
                self.ROndomNUMBER.append(randomRef)

                try:
                    server = smtplib.SMTP('imap.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login('english.ward.app@gmail.com' , 'abimfelojzucxpgt')
                    message = 'EMAIL CODE NUMBER  {} '.format(randomRef)
                    server.sendmail('english.ward.app@gmail.com' , self.email, message)
                    server.quit()
                    self.WrongTable.insert(END, "działa")
                    self.apps = self.open_window()
           
                except:                  
                    tkinter.messagebox.showinfo("EMAIL" , "Wrong adress email")
            elif self.passw1 != self.passw2:
                tkinter.messagebox.showinfo("REPEAT" , "reapet Password")
            elif EMAILCOUNT >=1:
                tkinter.messagebox.showinfo("EMAIL" , "the email exists")
                
            elif MARKS == 0 :
                tkinter.messagebox.showinfo("PASSWORD" , "the password must contain letters (!@#$%^&*)")

            elif LETER ==0 :
                tkinter.messagebox.showinfo("PASSWORD" , "the password must contain a capital letter")
            elif len(self.User1) == 0:
                tkinter.messagebox.showinfo("LOGIN" , "enter login")
        #=================================================================================================================================           
   
        self.background_image = PhotoImage(file = 'images.png')
        self.flagalabel = Label(self.frame1 , image = self.background_image  )
        self.flagalabel.place(anchor ='nw')
        
        self.flagalabel2 =Label(self.Master , image = self.background_image   )
        self.flagalabel2.place(x=700 ,y =700 ,  anchor ='se' )

        self.frame2 = Frame(self. Master  ,bg = 'white', bd=2, relief='ridge')
        self.frame2.place(relx=0.5 , rely = 0.5 , relwidth = 0.75 , relheight = 0.75 , anchor ='center')

        self.frame3 = Frame(self.frame2,bg = 'white')
        self.frame3.place( relwidth = 0.3 , relheight = 0.9 , rely = 0.05)

        self.frame4 = Frame(self.frame2,bg = 'white')
        self.frame4.place(relx=0.3 ,  relwidth = 0.6, relheight = 0.9 , rely = 0.05)

        self.lblLOGIN =Label(self.frame3, font = ('arial', 14 , 'bold') ,text = 'LOGIN' , bd = 7 , bg='white')
        self.lblLOGIN.grid (row = 1 , column = 0 , sticky ='e' ,padx=30, pady=5)

        self.txtLOGIN = Entry(self.frame4, font = ('arial', 14 , 'bold')  , bd = 2  )
        self.txtLOGIN.grid (row = 1 , column = 1, ipadx=35,padx=5, pady=5,ipady=5)

        self.lblFirstName =Label(self.frame3, font = ('arial', 14 , 'bold') ,text = 'Firstname' , bd = 7 , bg='white')
        self.lblFirstName.grid (row = 2 , column = 0 , sticky ='e' ,padx=30, pady=5)

        self.txtFirstName = Entry(self.frame4, font = ('arial', 14 , 'bold')  , bd = 2  )
        self.txtFirstName.grid (row = 2 , column = 1, ipadx=35,padx=5, pady=5,ipady=5)

        self.lblSurName =Label(self.frame3, font = ('arial', 14 , 'bold') ,text = 'Surname' , bd = 7 , bg='white')
        self.lblSurName.grid (row = 3 , column = 0 , sticky ='e' ,padx=30, pady=5)

        self.txtSurName =Entry(self.frame4, font = ('arial', 14 , 'bold')  , bd = 2  )
        self.txtSurName.grid (row = 3 , column = 1, ipadx=35,ipady=5 ,padx=5, pady=5)

        self.lblE_MAIL =Label(self.frame3, font = ('arial', 14 , 'bold') ,text = 'E_MAIL' , bd = 7 , bg='white')
        self.lblE_MAIL.grid (row = 4 , column = 0 , sticky ='e' ,padx=30, pady=5)

        self.txtE_MAIL =Entry(self.frame4, font = ('arial', 14 , 'bold')  , bd = 2  ,
                                    textvariable = "" )
        self.txtE_MAIL.grid (row = 4 , column = 1, ipadx=35,padx=5, pady=5,ipady=5)

        self.lblPassward =Label(self.frame3, font = ('arial', 14 , 'bold') ,text = 'Passward' , bd = 7 , bg='white')
        self.lblPassward.grid (row = 5 , column = 0 , sticky ='e' ,padx=30, pady=6)

        self.txtPassward =Entry(self.frame4, font = ('arial', 14 , 'bold')  , bd = 2  , show = '*'  )
        self.txtPassward.grid (row = 5 , column = 1, ipadx=35,padx=5, pady=5,ipady=5)

        self.lblrPassward =Label(self.frame3, font = ('arial', 10 , 'bold') ,text = 'Repeat password' , bd = 7 , bg='white')
        self.lblrPassward.grid (row = 6 , column = 0 , sticky ='e' ,padx=30, pady=6)

        self.txtrPassward =Entry(self.frame4, font = ('arial', 14 , 'bold')  , bd = 2  , show = '*' ,
                                    textvariable = "" )
        self.txtrPassward.grid (row = 6 , column = 1, ipadx=35,padx=5, pady=5,ipady=5)

        self.lblrStatus =Label(self.frame3, font = ('arial', 10 , 'bold') ,text = 'scientific status' , bd = 7 , bg='white')
        self.lblrStatus.grid (row = 7 , column = 0 , sticky ='e' ,padx=30, pady=6)

        self.cboStatus = ttk.Combobox(self.frame4 , textvariable = "" , state = 'readonly' , 
                                    font = ('arial', 14 , 'bold') , width=19 )

        self.cboStatus['value'] = ['', 'STUDENT' , 'WORKER' , 'OFFICE WORKER' , 'PENSIONER']
        self.cboStatus.current(0)
        self.cboStatus.grid (row = 7 , column = 1, ipadx=33,padx=5, pady=5,ipady=5)

        self.btnREGISTRATION =Button(self.frame4 , text='registration ' , width=13, bg='grey' , font = ('arial' , 15 , 'bold'), bd=2 , 
         command=add_USER)
        self.btnREGISTRATION.grid (row = 8, column = 1 , pady=90  , sticky ='e')

        self.frame5 = Frame(self.frame2 , bg = 'white')
        self.frame5.place(relx=0.05 ,  relwidth = 0.4, relheight = 0.20 , rely = 0.73)

        self.WrongTable = Text(self.frame5 ,font = ('arial' , 10 , 'bold') , fg='red', bd=0)
        self.WrongTable.place(relwidth = 1, relheight = 1) 

        def _destroy():
                if tkinter.messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
                        file = open('key.key', 'rb')
                        key = file.read()
                        USERDANE = pickle.load(open("USERDANE.py" , "rb"))
                        pickle.dump( USERDANE, open( "USERDANE.py", "wb" ))
                        with open('USERDANE.py', 'rb') as f:
                                data = f.read()

                        fernet = Fernet(key)
                        encrypted = fernet.encrypt(data)
                        with open('USERDANE.py', 'wb') as f:
                                f.write(encrypted)

                        self.Master.destroy()
                        mainWindow = Users()

        self.Master.protocol('WM_DELETE_WINDOW', _destroy)
        self.Master.mainloop()

    def open_window (self):

        self.Master1 = Toplevel()
        self.Master1.title("CODE MAIL")
        self.Master1.resizable( width = False , height= False)
        self.Master1.geometry('650x500+0+0')
        self.Master1.config(bg='white')
        self.frame1 = Frame (self.Master1 , bg='white')
        self.frame1.place( relwidth = 1 , relheight = 1 )

        def chuckNUMBER ():
            
            USERDANE = pickle.load(open("USERDANE.py" , "rb"))
            USERWARD = pickle.load(open("USERWARD.py" , "rb"))

            date = datetime.date.today()
            self.User1 = self.txtLOGIN.get()
            
            
            for numb in self.ROndomNUMBER:

                if numb == self.txtCODEMAIL.get():

                    password_provided = self.User1 
                    password = password_provided.encode() 
                    salt = b'\xc4:\xe3\xa9\x14x` ?\xee\xa7\xa7\xd3 >h' 
                    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                        backend=default_backend()
                        )
                    key = base64.urlsafe_b64encode(kdf.derive(password)) 
                    f = Fernet(key)
                    passw = self.passw1.encode()
                    encrypted = f.encrypt(passw)

                    USERDANE[self.User1] =  [self.Firstname , self.surname , self.email , encrypted , self.scieint , 0 ,date ,0]
                    USERWARD[self.User1] = []

                    pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                    pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                    with open("USERWARD.py", 'rb') as f:
                        data = f.read()
                    user =list(USERDANE)
                    password_provided = user[0]
                    password = password_provided.encode() 
                    salt = b'\xc4:\xe3\xa9\x14x` ?\xee\xa7\xa7\xd3 >h' 
                    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                        backend=default_backend()
                        )
                    key = base64.urlsafe_b64encode(kdf.derive(password)) 
                    val_ferenet = Fernet(key)
                    encrypted = val_ferenet.encrypt(data)
                    with open("USERWARD.py", 'wb') as f1:
                        f1.write(encrypted)

                    file = open('key.key', 'rb')
                    key = file.read()
    
                    with open('USERDANE.py', 'rb') as f:
                                data = f.read()

                    fernet = Fernet(key)
                    encrypted = fernet.encrypt(data)
                    with open('USERDANE.py', 'wb') as f:
                                f.write(encrypted)
                    tkinter.messagebox.showinfo("Registration" , "Registration is correct")
                    self.Master1.destroy()
                    self.Master.destroy()
                    mainWindow = Users()

                    

        self.background_image = PhotoImage(file = 'images.png')
        self.flagalabel = Label(self.frame1 , image = self.background_image  )
        self.flagalabel.place(anchor ='nw')
        
        self.flagalabel2 =Label(self.Master1 , image = self.background_image   )
        self.flagalabel2.place(x=650 ,y =500 ,  anchor ='se' )

        self.frame2 = Frame(self. Master1  ,bg = 'white', bd=2, relief='ridge')
        self.frame2.place(relx=0.5 , rely = 0.5 , relwidth = 0.75 , relheight = 0.5 , anchor ='center')

        self.frame3 = Frame(self.frame2   ,bg = 'white')
        self.frame3.place(relx=0.1 , rely = 0.15 , relwidth = 0.8 , relheight = 0.7 )

        self.lblCODEMAIL = Label(self.frame3 , text = 'CODE EMAIL' , font = ('arial', 15 , 'bold') , bg = 'white')
        self.lblCODEMAIL.pack( side = 'top')

        self.txtCODEMAIL =Entry(self.frame3, font = ('arial', 16 , 'bold')  , bd = 2   , width = 24, textvariable = "" )
        self.txtCODEMAIL.place( x=50,  y =50 )

        self.btnREGIMail =Button(self.frame3 , text='registration ' , width=13, bg='grey' , font = ('arial' , 15 , 'bold'), bd=2,
        command =chuckNUMBER )
        self.btnREGIMail.pack (side = 'bottom')

        self.Master1.mainloop()

class WindowRecower:
    def __init__(self):
        self.Master = Toplevel()
        self.Master.title("Admin View")
        self.Master.resizable( width = False , height= False)
        self.Master.geometry('650x500+0+0')
        self.Master.config(bg='white')
        self.frame1 = Frame (self.Master , bg='#E0EEEE')
        self.frame1.place( relwidth = 1 , relheight = 1 )
        var1 = StringVar()

        def _destroy():
                if tkinter.messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
                        file = open('key.key', 'rb')
                        key = file.read()
                        USERDANE = pickle.load(open("USERDANE.py" , "rb"))
                        pickle.dump( USERDANE, open( "USERDANE.py", "wb" ))
                        with open('USERDANE.py', 'rb') as f:
                                data = f.read()

                        fernet = Fernet(key)
                        encrypted = fernet.encrypt(data)
                        with open('USERDANE.py', 'wb') as f:
                                f.write(encrypted)

                        self.Master.destroy()
                        mainWindow = Users()

        self.Master.protocol('WM_DELETE_WINDOW', _destroy)
        

        def chuck(event):
                User = self.txt_login.get()
                email = self.txt_email.get()
                USERDANE = pickle.load(open("USERDANE.py" , "rb"))
                userval = USERDANE[User]
                if User in list(USERDANE):

                        if email == userval[2]:

                                password_provided = User
                                password = password_provided.encode() 
                                salt = b'\xc4:\xe3\xa9\x14x` ?\xee\xa7\xa7\xd3 >h' 
                                kdf = PBKDF2HMAC(
                                                algorithm=hashes.SHA256(),
                                                length=32,
                                                salt=salt,
                                                iterations=100000,
                                                backend=default_backend()
                                                )
                                key = base64.urlsafe_b64encode(kdf.derive(password)) 
                                
                                f = Fernet(key)
                                decrypted = f.decrypt(userval[3])
                                password = decrypted.decode()
                                try:
                                        server = smtplib.SMTP('imap.gmail.com:587')
                                        server.ehlo()
                                        server.starttls()
                                        server.login('english.ward.app@gmail.com' , 'abimfelojzucxpgt')
                                        message = 'Your Password is  {} '.format(password)
                                        server.sendmail('english.ward.app@gmail.com' , email, message)
                                        server.quit()

                                except:                
                                        tkinter.messagebox.showinfo("EMAIL" , "Wrong adress email")

                                var1.set ('Your Password is  {} '.format(password))


                
        self.lbl_login = Label(self.frame1, font = ('arial', 16 , 'bold')    , width = 24, text="LOGIN", bg='#E0EEEE')
        self.lbl_login.place(relx=0.1 , rely = 0.15 , relwidth = 0.8 , relheight = 0.1 )
        self.txt_login = Entry(self.frame1 , font = ('arial', 16 , 'bold')  , bd = 2  )
        self.txt_login.place(relx=0.1 , rely = 0.25 , relwidth = 0.8 , relheight = 0.1 )
        self.lbl_email = Label(self.frame1, font = ('arial', 16 , 'bold')     , width = 24, text="EMAIL", bg='#E0EEEE')
        self.lbl_email.place(relx=0.1 , rely = 0.35 , relwidth = 0.8 , relheight = 0.1 )
        self.txt_email = Entry(self.frame1 , font = ('arial', 16 , 'bold')  , bd = 2  )
        self.txt_email.place(relx=0.1 , rely = 0.45 , relwidth = 0.8 , relheight = 0.1 )
        self.txt_email.bind('<Return>' , chuck)
        
        self.lbl_password = Label(self.frame1, font = ('arial', 16 , 'bold')  , bd = 2   , width = 24, textvariable = var1 , bg='#E0EEEE')
        self.lbl_password.place(relx=0.1 , rely = 0.6 , relwidth = 0.8 , relheight = 0.1 )
        self.Master.mainloop()

class WindowFILE:
    
    def __init__(self , USER):
        self.Master = Toplevel()
        self.Master.title("ENGLISH WARD")
        self.Master.minsize("1800", "1000")

        self.Master.config(bg='white')
        self.frame1 = Frame (self.Master , bg='#E0EEEE')
        self.frame1.place( relwidth = 1 , relheight = 1 )
        self.User = USER
        with open("USERWARD.py", 'rb') as f2:
                data21 = f2.read()

        USERDANE = pickle.load(open("USERDANE.py" , "rb"))

        for users in list(USERDANE):    
                try:
                        
                        password_provided = "{}".format(users)
                        password = password_provided.encode() 
                        salt = b'\xc4:\xe3\xa9\x14x` ?\xee\xa7\xa7\xd3 >h' 
                        kdf = PBKDF2HMAC(
                                algorithm=hashes.SHA256(),
                                length=32,
                                salt=salt,
                                iterations=100000,
                                backend=default_backend()
                                )
                        key = base64.urlsafe_b64encode(kdf.derive(password))
                        val_ferenet = Fernet(key)
                        dencrypted = val_ferenet.decrypt(data21)
                        
                        with open('USERWARD.py', 'wb') as f21:
                                f21.write(dencrypted)
                        USERWARD = pickle.load(open("USERWARD.py" , "rb"))
                        
                        break
                
                except :
                        print("błąd")

        self.numer = 0
        self.numerP = 0
        self.today = datetime.date.today()
        self.d = datetime.date.today() + timedelta(days=1)
        self.d1 = datetime.date.today() + timedelta(days=2)
        self.d2 = datetime.date.today() + timedelta(days=3)
        self.d3 = datetime.date.today() + timedelta(days=5)
        self.find_liczbe = 0
        self.liczba_wys = 0
        self.reserv_count =0
        
        
                            
        def _destroy():
                if tkinter.messagebox.askokcancel('Quit', 'Are you sure you want to exit?'):
                        file = open('key.key', 'rb')
                        key = file.read()
                        USERDANE = pickle.load(open("USERDANE.py" , "rb"))
                        pickle.dump( USERDANE, open( "USERDANE.py", "wb" ))
                        with open('USERDANE.py', 'rb') as f:
                                data = f.read()

                        fernet = Fernet(key)
                        encrypted = fernet.encrypt(data)
                        with open('USERDANE.py', 'wb') as f:
                                f.write(encrypted)

                        
                        USERWARD = pickle.load(open("USERWARD.py" , "rb"))

                        pickle.dump( USERWARD, open( "USERWARD.py", "wb" ))
                        with open("USERWARD.py", 'rb') as f1:
                                data1 = f1.read()

                        password_provided = self.User
                        password = password_provided.encode() 
                        salt = b'\xc4:\xe3\xa9\x14x` ?\xee\xa7\xa7\xd3 >h' 
                        kdf = PBKDF2HMAC(
                                algorithm=hashes.SHA256(),
                                length=32,
                                salt=salt,
                                iterations=100000,
                                backend=default_backend()
                                )
                        key = base64.urlsafe_b64encode(kdf.derive(password)) 
                        val_ferenet = Fernet(key)
                        encrypted = val_ferenet.encrypt(data1)
                        with open("USERWARD.py", 'wb') as f:
                                f.write(encrypted)
                        self.Master.destroy()

        self.Master.protocol('WM_DELETE_WINDOW', _destroy)

        USERDANE1 = pickle.load(open("USERDANE.py" , "rb"))
        userDane1 = USERDANE1[self.User]

        if userDane1[6] != self.today:    
            userDane1[6]=self.today
            userDane1[7]=0
            pickle.dump(USERDANE1 , open("USERDANE.py" , "wb"))

        #====================================================================================================================================
        def dodaj_slowka ():
            self.frame4 = Frame(self.frame1 , bg = 'white')
            
            self.frame4.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
            self.slowka_angielskie = Label(self.frame4 , text = 'Słówko Angielskie' , font = ('arial', 20 , 'bold') , bg = 'white')
            self.slowka_angielskie.place(   relx = 0.15 , rely = 0.15)
            self.txtslowka_angielskie = Entry(self.frame4 ,font = ('arial', 19 , 'bold')  , bd = 2  ,  bg = 'white', relief='ridge' ,)
            self.txtslowka_angielskie.place(relwidth = 0.7 , relheight = 0.08 ,  relx = 0.15 , rely = 0.22)
            self.slowka_polskie = Label(self.frame4 , text = 'Słówko Polskie' , font = ('arial', 20 , 'bold') , bg = 'white')
            self.slowka_polskie.place(   relx = 0.15 , rely = 0.4)
            self.txtslowka_polskie = Entry(self.frame4 ,font = ('arial', 19 , 'bold')  , bd = 2  ,  bg = 'white', relief='ridge' , )
            self.txtslowka_polskie.place(relwidth = 0.7 , relheight = 0.08 ,  relx = 0.15 , rely = 0.48)
            
            def addword ():
                USERWARD = pickle.load(open("USERWARD.py" , "rb"))
                englishward = self.txtslowka_angielskie.get()
                englishword_strip =[]
                
                for word in englishward.split(','):
                    englishword_strip.append(word.strip())
                polishward = self.txtslowka_polskie.get()
                polishward_strip=[]
                for word1 in polishward.split(','):
                    polishward_strip.append(word1.strip())

                uservalue = USERWARD[self.User]
                date = datetime.date.today()
                
                if list(uservalue).count(englishward) >= 1:
                    tkinter.messagebox.showinfo("Word" , "The word exists ")

                else:
                    uservalue.append([englishword_strip, polishward_strip , [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [ date, date, date, date, date, date, date, date]])
                    USERWARD[self.User] = uservalue

                    pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                    englishward = self.txtslowka_angielskie.delete(0, 'end')
                    polishward = self.txtslowka_polskie.delete(0, 'end')
                    self.calkowita_liczba_slow.config(text = "liczba słów :{}".format(len(uservalue)) )

            self.addslowko = Button(self.frame4 , text = "Dodaj Słówko" , width=12 , bg='#458B74' , font = ('arial' , 20 , 'bold'), bd=3,
            command =addword , justify = 'center')
            self.addslowko.bind('<Return>' , addword)
            self.addslowko.place (relx = 0.65 , rely = 0.7)
#=======================================POWTÓRKI===================================================================================
        self.frame2 = Frame (self.frame1 , bg = '#E0EEEE')
        self.frame2.place(relwidth = 0.28 , relheight = 1 , relx =0 , rely = 0)
        def powtorki():
            USERWARD = pickle.load(open("USERWARD.py" , "rb"))
            USERDANE = pickle.load(open("USERDANE.py" , "rb"))
            uservalue = USERWARD[self.User]
            userDane = USERDANE[self.User]
            
            def eng_word():
                shuffle(uservalue)

                def newapp(event):
                        frame21.destroy()
                        app= eng_word()
                def newapp1():
                        frame21.destroy()
                        app= eng_word()
                def try_lerned(ward,i):
                        value = ward
                        i=i
                        word2= ','.join(uservalue[i][1])
                        valu =','.join(ward)

                        if value == uservalue[i][1]:
                                
                                userDane[5] += 10
                                userDane[7] += 10
                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )


                                for x in range(3,8):
                                        label1.place(relwidth = 0.05 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                        label1.update()
                                        time.sleep(0.1)
                                        if x >=7:
                                                label1.place_forget()
                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))

                                app= eng_word()
                        else:
                                uservalue[i][2][0] +=1
                                uservalue[i][3][0] = 0
                                uservalue[i][4][0] = self.d

                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                
                                for b in range(0 , len(btn)) :

                                                if btn[b]["text"] == word2:

                                                        btn[b].place_info()

                                                        btn[b].configure(background='green')
                                                        btn[b]["command"] = newapp1
                                                        frame21.bind('<Return>' ,newapp )
                                                        
                                                        
                                                else :
                                                        btn[b].configure(bg='white')
                                        
                                                if btn[b]["text"] == valu:

                                                        btn[b].place_info()

                                                        btn[b].configure(background='red')

                def add_value (ward,i):
                        value = ward
                        i=i
                        word2= ','.join(uservalue[i][1])
                        valu =','.join(ward)

                        if value == uservalue[i][1] and  uservalue[i][3][0] <= 5:
                                
                                uservalue[i][4][0] = self.d
                                uservalue[i][3][0] +=1
                                uservalue[i][2][0] +=1
                                userDane[5] += 1
                                userDane[7] += 1
                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )


                                for x in range(3,8):
                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                        label1.update()
                                        time.sleep(0.1)
                                        if x >=7:
                                                label1.place_forget()
                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                app= eng_word()
                        elif value == uservalue[i][1] and  7 >=uservalue[i][3][0] > 5:
                                uservalue[i][4][0] = self.d1
                                uservalue[i][3][0] +=1
                                uservalue[i][2][0] +=1
                                userDane[5] += 1
                                userDane[7] += 1
                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                for x in range(3,8):
                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                        label1.update()
                                        time.sleep(0.1)
                                        if x >=7:
                                                label1.place_forget()
                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                app= eng_word()
                        elif value == uservalue[i][1] and  9 >uservalue[i][3][0] > 7:
                                uservalue[i][4][0] = self.d2
                                uservalue[i][3][0] += 1
                                uservalue[i][2][0] += 1
                                userDane[5] += 2
                                userDane[7] += 2
                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                label1= Label(frame21 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                for x in range(3,8):
                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                        label1.update()
                                        time.sleep(0.1)
                                        if x >=7:
                                                label1.place_forget()
                                
                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                app= eng_word()
                        elif value == uservalue[i][1] and  uservalue[i][3][0] == 9:
                                uservalue[i][4][0] = "NAUCZONE"
                                uservalue[i][3][0] += 1
                                uservalue[i][2][0] +=1
                                userDane[5] += 10
                                userDane[7] += 10
                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                for x in range(3,8):
                                        label1.place(relwidth = 0.05 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                        label1.update()
                                        time.sleep(0.1)
                                        if x >=7:
                                                label1.place_forget()
                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                app= eng_word()
                        else :
                                uservalue[i][2][0] +=1
                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                
                                for b in range(0 , len(btn)) :

                                                if btn[b]["text"] == word2:

                                                        btn[b].place_info()

                                                        btn[b].configure(background='green')
                                                        btn[b]["command"] = newapp1
                                                        frame21.bind('<Return>' ,newapp )
                                                        
                                                        
                                                else :
                                                        btn[b].configure(bg='white')
                                        
                                                if btn[b]["text"] == valu:

                                                        btn[b].place_info()

                                                        btn[b].configure(background='red')


                licz_data = 0
                rand=randint(0,10)
                randomR = int(rand)
                if randomR != 0 :
                        for i in range(len(uservalue)):
                                date=(uservalue[i][4][0])

                                try:           
                                        if date <= self.today:
                                                licz_data +=1
                                                word1= ','.join(uservalue[i][0])
                                                word2= ','.join(uservalue[i][1])
                                                
                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)

                                                lbl_English = Label(frame21 , font = ('arial' , 18 , 'bold') , bd=2 , bg ='#458B74', relief='ridge' , text = word1 )
                                                lbl_English.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.05)
                                                eng_sample = [ "dobrze" , "jeden" , "cześć" , "dwa"]

                                                btn = []
                                                if len(uservalue) <5:
                                                
                                                        for g in range(0,4):
                                                                
                                                                btn.append(Button(frame21 ,font = ('arial' , 18 , 'bold') , bd=2 ,bg='white', relief='ridge' , text = eng_sample[g]))
                                                                btn[g].place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20+(g*0.1))
                                                                btn[g]["command"] = lambda x = eng_sample[g] : add_value(x,i) 
                                                                btn[g].configure(bg ='white')
                                                                
                                                        y=randint(0,3)
                                                        randomRef = int(y)

                                                        btn[randomRef]["text"] = word2
                                                        btn[randomRef]["command"] = lambda x = uservalue[i][1] : add_value(x,i) 

                                                        break
                                                else:
                                                        count =sample(range(0, len(uservalue)) , 4)

                                                        for l in range(0 ,len(count)):

                                                                if i  == count[l]:
                                                                        for m in range(0, len(uservalue)):
                                                                                if m  not in count and m != i :

                                                                                        count[l] = m
                                                                                        break
                                                                else :
                                                                        print("is ok")

                                                for a in range(0,4):

                                                        word3= ','.join(uservalue[count[a]][1])
                                                        
                                                        
                                                        btn.append(Button(frame21 ,font = ('arial' , 18 , 'bold') , bd=2 ,bg='white', relief='ridge' , text = word3))
                                                        btn[a].place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20+(a*0.1))
                                                        btn[a]["command"] = lambda x = uservalue[count[a]][1] : add_value(x,i) 
                                                        btn[a].configure(bg ='white')
                                                        
                                                y=randint(0,3)
                                                randomRef = int(y)

                                                btn[randomRef]["text"] = word2
                                                btn[randomRef]["command"] = lambda x = uservalue[i][1] : add_value(x,i) 

                                                break

                                except TypeError: 
                                        
                                        continue   

                else:
                        for i in range(len(uservalue)):
                                date=(uservalue[i][4][0])
                                try:  

                                        if date == "NAUCZONE":
                                                licz_data +=1
                                                
                                                word1= ','.join(uservalue[i][0])
                                                word2= ','.join(uservalue[i][1])
                                                
                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)

                                                lbl_English = Label(frame21 , font = ('arial' , 18 , 'bold') , bd=2 , bg ='#458B74', relief='ridge' , text = word1 )
                                                lbl_English.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.05)
                                                eng_sample = [ "dobrze" , "jeden" , "cześć" , "dwa"]

                                                btn = []
                                                if len(uservalue) <5:
                                                
                                                        for g in range(0,4):
                                                                
                                                                btn.append(Button(frame21 ,font = ('arial' , 18 , 'bold') , bd=2 ,bg='white', relief='ridge' , text = eng_sample[g]))
                                                                btn[g].place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20+(g*0.1))
                                                                btn[g]["command"] = lambda x = eng_sample[g] : try_lerned(x,i) 
                                                                btn[g].configure(bg ='white')
                                                                
                                                        y=randint(0,3)
                                                        randomRef = int(y)

                                                        btn[randomRef]["text"] = word2
                                                        btn[randomRef]["command"] = lambda x = uservalue[i][1] : try_lerned(x,i) 

                                                        break
                                                else:
                                                        count =sample(range(0, len(uservalue)) , 4)

                                                        for l in range(0 ,len(count)):

                                                                if i  == count[l]:
                                                                        for m in range(0, len(uservalue)):
                                                                                if m  not in count and m != i :

                                                                                        count[l] = m
                                                                                        break

                                                for a in range(0,4):

                                                        word3= ','.join(uservalue[count[a]][1])
                                                        
                                                        
                                                        btn.append(Button(frame21 ,font = ('arial' , 18 , 'bold') , bd=2 ,bg='white', relief='ridge' , text = word3))
                                                        btn[a].place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20+(a*0.1))
                                                        btn[a]["command"] = lambda x = uservalue[count[a]][1] : try_lerned(x,i) 
                                                        btn[a].configure(bg ='white')
                                                        
                                                y=randint(0,3)
                                                randomRef = int(y)

                                                btn[randomRef]["text"] = word2
                                                btn[randomRef]["command"] = lambda x = uservalue[i][1] : try_lerned(x,i) 

                                                break

                                except TypeError: 
                                        
                                        continue   

                if licz_data <= 0 :
                        app1 = powtorki()



            count_english = 0
            for i in range(len(uservalue)):
                date=(uservalue[i][4][0])
                try:
                        if date <= self.today:
                                count_english +=1
                        
                except TypeError:
                        
                        continue

            frame20 = Frame(self.frame1 , bg = "#CCCC99")
            frame20.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
            english= Button(frame20 ,font = ('arial', 14 , 'bold')  , bd = 2   , justify = 'left' , bg='#458B74',
             text= "Ćwiczenie 1  - Wybierz Polskie znaczenie{:>65} Słówek".format(count_english) ,command = eng_word)
            if count_english >=1 :
                english.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.05)

            def pol_word():
                shuffle(uservalue)

                def newapp(event):
                    frame21.destroy()
                    app= pol_word()
                def newapp1():
                    frame21.destroy()
                    app= pol_word()

                def try_lerned(ward,i):
                        value = ward
                        i=i
                        word2= ','.join(uservalue[i][0])
                        valu =','.join(ward)

                        if value == uservalue[i][0]:
                                
                                userDane[5] += 10
                                userDane[7] += 10
                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )


                                for x in range(3,8):
                                        label1.place(relwidth = 0.05 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                        label1.update()
                                        time.sleep(0.1)
                                        if x >=7:
                                                label1.place_forget()
                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))

                                app= pol_word()
                        else:
                                uservalue[i][2][0] +=1
                                uservalue[i][3][0] = 0
                                uservalue[i][4][0] = self.d

                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                
                                for b in range(0 , len(btn)) :

                                                if btn[b]["text"] == word2:

                                                        btn[b].place_info()

                                                        btn[b].configure(background='green')
                                                        btn[b]["command"] = newapp1
                                                        frame21.bind('<Return>' ,newapp )
                                                        
                                                        
                                                else :
                                                        btn[b].configure(bg='white')
                                        
                                                if btn[b]["text"] == valu:

                                                        btn[b].place_info()

                                                        btn[b].configure(background='red')

                def add_value (ward , i):
                        i=i
                        value = ward
                        word2= ','.join(uservalue[i][0])
                        valu =','.join(ward)

                        if value == uservalue[i][0] and  uservalue[i][3][1] <= 5:
                                uservalue[i][4][1] = self.d
                                uservalue[i][3][1] +=1
                                uservalue[i][2][1] +=1
                                userDane[5] += 1
                                userDane[7] += 1
                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )
    
    
                                for x in range(3,8):
                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                        label1.update()
                                        time.sleep(0.1)
                                        if x >=7:
                                                label1.place_forget()
                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                app= pol_word()
                        elif value == uservalue[i][0] and  7 >=uservalue[i][3][1] > 5:
                                uservalue[i][4][1] = self.d1
                                uservalue[i][3][1] +=1
                                uservalue[i][2][1] +=1
                                userDane[5] += 1
                                userDane[7] += 1
                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )
    
    
                                for x in range(3,8):
                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                        label1.update()
                                        time.sleep(0.1)
                                        if x >=7:
                                                label1.place_forget()
                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                app= pol_word()
                        elif value == uservalue[i][0] and  9 >uservalue[i][3][1] > 7:
                                uservalue[i][4][1] = self.d2
                                uservalue[i][3][1] += 1
                                uservalue[i][2][1] += 1
                                userDane[5] += 2
                                userDane[7] += 2
                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                label1= Label(frame21 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )
    
    
                                for x in range(3,8):
                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                        label1.update()
                                        time.sleep(0.1)
                                        if x >=7:
                                                label1.place_forget()
                                
                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                app= pol_word()
                        elif value == uservalue[i][0] and  uservalue[i][3][1] == 9:
                                uservalue[i][4][1] = "NAUCZONE"
                                uservalue[i][3][1] += 1
                                uservalue[i][2][1] +=1
                                userDane[5] += 10
                                userDane[7] += 10
                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )
    
    
                                for x in range(3,8):
                                        label1.place(relwidth = 0.05 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                        label1.update()
                                        time.sleep(0.1)
                                        if x >=7:
                                                label1.place_forget()
                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                app= pol_word()
                        else :
                                uservalue[i][2][1] +=1
                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                for b in range(0 , len(btn)) :

                                                if btn[b]["text"] == word2:

                                                        btn[b].place_info()

                                                        btn[b].configure(background='green')
                                                        btn[b]["command"] = newapp1
                                                        frame21.bind('<Return>' ,newapp )
   
                                                else :

                                                        btn[b].configure(bg='white')
                                        
                                                if btn[b]["text"] == valu:

                                                        btn[b].place_info()  
                                                        btn[b].configure(background='red')



                licz_data = 0
                rand=randint(0,10)
                randomR = int(rand)
                if randomR != 0 :
                        for i in range(len(uservalue)):
                                date=(uservalue[i][4][1])
                                
                                try:    
                                        if date <= self.today:
                                                licz_data +=1
                                                word1= ','.join(uservalue[i][1])
                                                word2= ','.join(uservalue[i][0])
                                                
                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                                
                                                
                                                lbl_English = Label(frame21 , font = ('arial' , 18 , 'bold') , bd=2 ,bg='#458B74', relief='ridge' , text = word1 )
                                                lbl_English.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.05)
                                                
                                                eng_sample = [ "good ", "one" , "hi" , "two"]
                                                btn = []
                                                if len(uservalue) < 5:
                                                
                                                        for g in range(0,4):
                                                                
                                                                btn.append(Button(frame21 ,font = ('arial' , 18 , 'bold') , bd=2 ,bg='white', relief='ridge' , text = eng_sample[g]))
                                                                btn[g].place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20+(g*0.1))
                                                                btn[g]["command"] = lambda x = eng_sample[g] : add_value(x,i) 
                                                                btn[g].configure(bg ='white')
                                                                
                                                        y=randint(0,3)
                                                        randomRef = int(y)

                                                        btn[randomRef]["text"] = word2
                                                        btn[randomRef]["command"] = lambda x = uservalue[i][0] : add_value(x,i) 

                                                        break
                                                else:
                                                        count =sample(range(0, len(uservalue)) , 4)

                                                        for l in range(0 ,len(count)):

                                                                if i  == count[l]:

                                                                        for m in range(0, len(uservalue)):
                                                                                if m  not in count and m != i :

                                                                                        count[l] = m

                                                                                        break
                                                                else :
                                                                        print("is ok")

                                                for g in range(0,4):
                                                        
                                                        word3= ','.join(uservalue[count[g]][0])
                                                        
                                                        
                                                        btn.append(Button(frame21 ,font = ('arial' , 18 , 'bold') , bd=2 ,bg='white', relief='ridge' , text = word3))
                                                        btn[g].place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20+(g*0.1))
                                                        btn[g]["command"] = lambda x = uservalue[count[g]][0] : add_value(x,i) 
                                                        btn[g].configure(bg ='white')
                                                        
                                                y=randint(0,3)
                                                randomRef = int(y)

                                                for word3 in uservalue[i][0]:
                                                        btn[randomRef]["text"] = word2
                                                        btn[randomRef]["command"] = lambda x = uservalue[i][0] : add_value(x,i) 

                                                break
                                
                                except TypeError:

                                                continue
                else:
                        for i in range(len(uservalue)):
                                date=(uservalue[i][4][1])
                                
                                try:    
                                        if date <= "NAUCZONE":
                                                licz_data +=1
                                                word1= ','.join(uservalue[i][1])
                                                word2= ','.join(uservalue[i][0])
                                                
                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                                
                                                
                                                lbl_English = Label(frame21 , font = ('arial' , 18 , 'bold') , bd=2 ,bg='#458B74', relief='ridge' , text = word1 )
                                                lbl_English.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.05)
                                                
                                                eng_sample = [ "good ", "one" , "hi" , "two"]
                                                btn = []
                                                if len(uservalue) < 5:
                                                
                                                        for g in range(0,4):
                                                                
                                                                btn.append(Button(frame21 ,font = ('arial' , 18 , 'bold') , bd=2 ,bg='white', relief='ridge' , text = eng_sample[g]))
                                                                btn[g].place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20+(g*0.1))
                                                                btn[g]["command"] = lambda x = eng_sample[g] : try_lerned(x,i) 
                                                                btn[g].configure(bg ='white')
                                                                
                                                        y=randint(0,3)
                                                        randomRef = int(y)

                                                        btn[randomRef]["text"] = word2
                                                        btn[randomRef]["command"] = lambda x = uservalue[i][0] : try_lerned(x,i) 

                                                        break
                                                else:
                                                        count =sample(range(0, len(uservalue)) , 4)

                                                        for l in range(0 ,len(count)):

                                                                if i  == count[l]:

                                                                        for m in range(0, len(uservalue)):
                                                                                if m  not in count and m != i :

                                                                                        count[l] = m

                                                                                        break
                                                                else :
                                                                        print("is ok")

                                                for g in range(0,4):
                                                        
                                                        word3= ','.join(uservalue[count[g]][0])
                                                        
                                                        
                                                        btn.append(Button(frame21 ,font = ('arial' , 18 , 'bold') , bd=2 ,bg='white', relief='ridge' , text = word3))
                                                        btn[g].place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20+(g*0.1))
                                                        btn[g]["command"] = lambda x = uservalue[count[g]][0] : try_lerned(x,i) 
                                                        btn[g].configure(bg ='white')
                                                        
                                                y=randint(0,3)
                                                randomRef = int(y)

                                                for word3 in uservalue[i][0]:
                                                        btn[randomRef]["text"] = word2
                                                        btn[randomRef]["command"] = lambda x = uservalue[i][0] : try_lerned(x,i) 

                                                break
                                
                                except TypeError:

                                                continue

                if licz_data <= 0 :
                        app3 = powtorki()
                       
            count_polish = 0

            for i in range(len(uservalue)):
                date=(uservalue[i][4][1])
                try:
                        if date <= self.today:
                                count_polish +=1
                        
                except TypeError:
                       
                        continue
            Polish= Button(frame20 ,font = ('arial', 14 , 'bold')  , bd = 2   , justify = 'left', bg='#458B74' ,
             text= "Ćwiczenie 2  - Wybierz Angielskie znaczenie{:>65} Słówek".format(count_polish) , command = pol_word )
            if count_polish >=1 :
                Polish.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.16)

            def W_ENG_WORD():
                shuffle(uservalue)
                licz_data =0
                def next_word():
                        frame21.destroy()
                        app= W_ENG_WORD()
                
                def Chuck_word(event):
                        polword = Ent_Pol.get()
                        cor_Word = uservalue[i][0]

                        Ent_Pol.destroy()
                        correct_text = Text(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,pady = 20 )
                        if len(cor_Word)>=2:
                                polword_split = []
                                
                                count_word=0
                                lengh_word =0
                                for word1 in polword.split(','):
                                        polword_split.append(word1.strip())
                                for ind , word in enumerate(polword_split):
                                        correct_word = 0

                                        for word3 in cor_Word:
                                                
                                        
                                                if word.lower() == word3.lower():
                                                        
                                                        correct_word+=1
                                                        count_word+=1

                                        if correct_word >0:
                                                
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                        
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"right") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3
                                
                                                correct_text.tag_config("{}".format(word+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"right0"), background="white", foreground="black" , justify = 'center')
                                                
                                        else:
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"wrong") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3

                                                                                                                        
                                                correct_text.tag_config("{}".format(word+"wrong"), background="white", foreground="red" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"wrong"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"wrong0"), background="white", foreground="red" , justify = 'center')
                                                
                                correct_text.config(state = "disabled")
                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                name = ','.join(cor_Word)
                                        
                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)    

                                if len(cor_Word)>count_word >0:

                                                uservalue[i][4][2] = self.d
                                                
                                                uservalue[i][2][2] +=1
                                                userDane[5] += 1*correct_word
                                                userDane[7] += 1*correct_word
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*correct_word),   font = ('arial' , 20 , 'bold') , bd = 4 )


                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                        
                                elif len(cor_Word)<=count_word :
                                                
                                                if   uservalue[i][3][2] <= 5:
                                                        uservalue[i][4][2] = self.d
                                                        uservalue[i][3][2] +=1
                                                        uservalue[i][2][2] +=1
                                                        userDane[5] += 1*count_word
                                                        userDane[7] += 1*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                         
                                                        app= W_ENG_WORD()
                                                elif   7 >= uservalue[i][3][2] > 5:
                                                        
                                                        uservalue[i][4][2] = self.d1
                                                        uservalue[i][3][2] +=1
                                                        uservalue[i][2][2] +=1
                                                        userDane[5] += 1*count_word
                                                        userDane[7] += 1*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
        
        
                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                        
                                                        app= W_ENG_WORD()
                                                elif  9>uservalue[i][3][2] > 7:
                                                        uservalue[i][4][2] = self.d2
                                                        uservalue[i][3][2] +=1
                                                        uservalue[i][2][2] +=1
                                                        userDane[5] += 2*count_word
                                                        userDane[7] += 2*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(2*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
        
        
                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.025 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                          
                                                        app= W_ENG_WORD()
                                                elif  uservalue[i][3][2] >=9:
                                                        uservalue[i][4][2] = "NAUCZONE"
                                                        uservalue[i][3][2] +=1
                                                        uservalue[i][2][2] +=1
                                                        userDane[5] += 10*count_word
                                                        userDane[7] += 10*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(10*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
        
        
                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.04 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                  
                                                        app= W_ENG_WORD()        
                                else:
                                                uservalue[i][2][2] +=1
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))                                           
                        else:
                                for word in cor_Word:
                                        if polword.lower() == word.lower() and  uservalue[i][3][2] <= 5:

                                                uservalue[i][4][2] = self.d
                                                uservalue[i][3][2] +=1
                                                uservalue[i][2][2] +=1
                                                userDane[5] += 1
                                                userDane[7] += 1
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                         
                                                app= W_ENG_WORD()
                                        elif polword.lower() == word.lower() and  7>=uservalue[i][3][2] > 5:

                                                uservalue[i][4][2] = self.d1
                                                uservalue[i][3][2] +=1
                                                uservalue[i][2][2] +=1
                                                userDane[5] += 1
                                                userDane[7] += 1
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )


                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                          
                                                app= W_ENG_WORD()
                                        elif polword.lower() == word.lower() and  9>uservalue[i][3][2] > 7:

                                                uservalue[i][4][2] = self.d2
                                                uservalue[i][3][2] +=1
                                                uservalue[i][2][2] +=1
                                                userDane[5] += 2
                                                userDane[7] += 2
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                          
                                                app= W_ENG_WORD()
                                        elif polword.lower() == word.lower() and  uservalue[i][3][2] ==9:

                                                uservalue[i][4][2] = "NAUCZONE"
                                                uservalue[i][3][2] +=1
                                                uservalue[i][2][2] +=1
                                                userDane[5] += 10
                                                userDane[7] += 10
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                           
                                                app= W_ENG_WORD()

                                        else:
                                                literwka = 0 
                                                dobra_litera = 0 
                                                zla_litera = 0  
                                                slownik = {"a":"ą","c":"ć" , "e" :"ę" , "s" : "ś" , "n" : "ń" , "u":"o" ,"o" :"ó" , "l" :"ł" , "z" : ["ź" , "ż"]}
                                                for word in cor_Word:

                                                        krotnosc = 0
                                                        litera_wys = 0

                                                        for g in range(len(polword)):

                                                                        if g-1+krotnosc>=0  :
                                                                                        try:
                                                                                                if polword[g].lower() == word[g-1+krotnosc].lower():
                                                                                                        if g+1<len(word):
                                                                                                                if polword[g+1].lower() == word[g+1+krotnosc].lower():
                                                                                                                        if krotnosc == 0:
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera +=1

                                                                                                                        elif krotnosc ==1 :
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                dobra_litera +=1
                                                                                                                                
                                                                                                                        else:
                                                                                                                                literwka +=1   
                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1
                                                                                                                                
                                                                                                                elif polword[g-1].lower() == word[g-1+krotnosc].lower():
                                                                                                                        
                                                                                                                        zla_litera +=1   
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold'), justify = 'center')

                                                                                                                else:
                                                                                                                        
                                                                                                                        literwka +=1   
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                        krotnosc -=1

                                                                                                        elif polword[g-1].lower() == word[g-1+krotnosc].lower():
                                                                                                                
                                                                                                                zla_litera +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold'), justify = 'center')
                                                                                                                
                                                                                                                
                                                                                                        else:
                                                                                                                
                                                                                                                literwka +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                krotnosc -=1
                                                                                                


                                                                                                elif polword[g].lower() in slownik and word[g-1+krotnosc] in slownik.values():

                                                                                                        try:
                                                                                                                if word[g-1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                        if polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower() and polword[g+krotnosc].lower() != word[g+krotnosc].lower():
                                                                                                                                literwka +=1  
                                                                                                                                
                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1

                                                                                                                        elif polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower() and polword[g+krotnosc].lower() == word[g+krotnosc].lower(): 
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera+=1
                                                                                                                        
                                                                                                                        else:
                                                                                                                                if polword[g].lower() == word[g-1+krotnosc].lower():
                                                                                                                                        if polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower():
                                                                                                                                                
                                                                                                                                                literwka +=1   
                                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                                krotnosc +=1
                                                                                                                                                litera_wys+=1
                                                                                                                                        else:
                                                                                                                                                
                                                                                                                                                literwka +=1   
                                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                
                                                                                                                                else: 
                                                                                                                                                        
                                                                                                                                                literwka +=1  
                                                                                                                                                
                                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                                krotnosc -=1
                                                                                                                                        
                                                                                                                elif polword[g].lower() == word[g+krotnosc].lower():

                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        if krotnosc ==0:
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera+=1

                                                                                                                        else:
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                literwka +=1 
                                                                                                                                
                                                                                                                elif polword[g].lower() in slownik and word[g+krotnosc] in slownik.values():

                                                                                                                        if word[g+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                
                                                                                                                                literwka +=1    
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                        elif polword[g].lower() == word[g+1+krotnosc].lower():

                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1._{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                                        elif polword[g].lower() in slownik and word[g+1] in slownik.values():

                                                                                                                                if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                        
                                                                                                                                        literwka +=1   
                                                                                                                                        
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1 
                                                                                                                                else: 
                                                                                                                                        
                                                                                                                                        zla_litera += 1
                                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                        else: 
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                                elif polword[g].lower() == word[g+1+krotnosc].lower():
                                                                                                                        
                                                                                                                        literwka +=1 
                                                                                                                        
                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                        krotnosc +=1
                                                                                                                        litera_wys+=1
                                                                                                                elif polword[g].lower() in slownik and word[g+1+krotnosc] in slownik.values():

                                                                                                                        if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                
                                                                                                                                literwka +=1 
                                                                                                                                
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1
                                                                                                                        else: 
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')


                                                                                                                else :
                                                                                                                        
                                                                                                                        zla_litera += 1
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center') 

                                                                                                        except ( IndexError , KeyError ) :

                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                

                                                                                                elif polword[g].lower() == word[g+krotnosc].lower():

                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        if krotnosc ==0:
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                dobra_litera +=1
                                                                                                                
                                                                                                        else:
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                elif polword[g].lower() in slownik and word[g+krotnosc] in slownik.values():
                                                                                                        
                                                                                                
                                                                                                        if word[g+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                        else: 
                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                elif polword[g].lower() == word[g+1+krotnosc].lower():

                                                                                                        if polword[g-1].lower() == word[g-1+krotnosc].lower()  :

                                                                                                                if g+1 <len(polword):

                                                                                                                        if polword[g+1].lower() == word[g+krotnosc].lower()  :
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                                        else:
                                                                                                                                
                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                                else:
                                                                                                                                
                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                        elif polword[g-1].lower() in slownik and word[g-1+krotnosc] in slownik.values():

                                                                                                                if word[g-1+krotnosc].lower() in slownik[polword[g-1].lower()]:
                                                                                                                        
                                                                                                                        if polword[g+1].lower() in slownik and word[g+krotnosc] in slownik.values() or polword[g+1].lower() == word[g+krotnosc].lower():
                                                                                                                                
                                                                                                                                if word[g+krotnosc].lower() in slownik[polword[g+1].lower()] or polword[g+1].lower() == word[g+krotnosc].lower():
                                                                                                                                        
                                                                                                                                        zla_litera += 1
                                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                                else:
                                                                                                                                        
                                                                                                                                        literwka +=1  
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1
                                                                                                                        else:
                                                                                                                                        
                                                                                                                                        literwka +=1  
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1
                                                                                                        else:
                                                                                                                
                                                                                                                literwka +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                
                                                                                                
                                                                                                
                                                                                                elif polword[g].lower() in slownik and word[g+1+krotnosc] in slownik.values():
                                                                                                        
                                                                                                
                                                                                                        if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                krotnosc+=1 
                                                                                                                litera_wys+=1 
                                                                                                        else: 
                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                else: 
                                                                                                        
                                                                                                        zla_litera += 1
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        except ( IndexError , KeyError ) :

                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                        else:
                                                                                try:
                                                                                        if polword[g].lower() == word[g].lower():
                                                                                                
                                                                                                dobra_litera += 1 
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                        elif polword[g].lower() in slownik and word[g] in slownik.values():
                                                                                                
                                                                                                if word[g].lower() in slownik[polword[g].lower()]:
                                                                                                        
                                                                                                        literwka +=1    
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                else :
                                                                                                        
                                                                                                        zla_litera += 1
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        elif polword[g].lower() == word[g+1].lower():
                                                                                                
                                                                                                literwka += 1 
                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                krotnosc+=1
                                                                                                litera_wys+=1
                                                                                        elif polword[g].lower() in slownik and word[g+1] in slownik.values():
                                                                                                
                                                                                                if word[g].lower() in slownik[polword[g+1].lower()]:
                                                                                                                
                                                                                                        literwka +=1    
                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                        krotnosc+=1
                                                                                                        litera_wys+=1
                                                                                                else :
                                                                                                        
                                                                                                        zla_litera += 1
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        else:
                                                                                                
                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                except ( IndexError , KeyError ) :

                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                                                                                
                                                        correct_text.config(state = "disabled")
                                                        correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                                        
                                                        for name in cor_Word:
                                                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)

                                                        if ((literwka+dobra_litera) / len(word))*10 >=10:

                                                                uservalue[i][4][2] = self.d
                                                                
                                                                uservalue[i][2][2] +=1
                                                                userDane[5] += 1
                                                                userDane[7] += 1
                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                
                                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )
                
                
                                                                for x in range(3,8):
                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                        label1.update()
                                                                        time.sleep(0.1)
                                                                        if x >=7:
                                                                                label1.place_forget()
                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                                        else:
                                                                print("do poprawy")

                def Lerned_word(event ):
                        polword = Ent_Pol.get()
                        cor_Word = uservalue[i][0]

                        Ent_Pol.destroy()
                        correct_text = Text(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,pady = 20 )
                        if len(cor_Word)>=2:
                                polword_split = []
                                
                                count_word=0
                                lengh_word =0
                                for word1 in polword.split(','):
                                        polword_split.append(word1.strip())
                                for ind , word in enumerate(polword_split):
                                        correct_word = 0

                                        for word3 in cor_Word:
                                                
                                        
                                                if word.lower() == word3.lower():
                                                        
                                                        correct_word+=1
                                                        count_word+=1

                                        if correct_word >0:
                                                
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                        
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"right") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3
                                
                                                correct_text.tag_config("{}".format(word+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"right0"), background="white", foreground="black" , justify = 'center')
                                                
                                        else:
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"wrong") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3

                                                                                                                        
                                                correct_text.tag_config("{}".format(word+"wrong"), background="white", foreground="red" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"wrong"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"wrong0"), background="white", foreground="red" , justify = 'center')
                                                
                                correct_text.config(state = "disabled")
                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                name = ','.join(cor_Word)
                                        
                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)    

                                if len(cor_Word)>count_word >0:

                                        uservalue[i][4][2] = self.d
                                        uservalue[i][3][2] = 0
                                        uservalue[i][2][2] +=1

                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                        
                                elif len(cor_Word)<=count_word :
                                                
                                        userDane[5] += 10*count_word
                                        userDane[7] += 10*count_word
                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                        
                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(10*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
                                        for x in range(3,8):
                                                label1.place(relwidth = 0.06 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                label1.update()
                                                time.sleep(0.1)
                                                if x >=7:
                                                        label1.place_forget()
                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
  
                                        app= W_ENG_WORD()

                                else:
                                        uservalue[i][4][2] = self.d
                                        uservalue[i][3][2] = 0
                                        uservalue[i][2][2] +=1
                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))    
                        else:
                                for word5 in cor_Word:
                                        if polword.lower() == word5.lower() :

                                                userDane[5] += 10
                                                userDane[7] += 10
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.04 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
  
                                                app= W_ENG_WORD()
                                        else:

                                                correct_text.insert(END, "{}".format(polword))
                                                correct_text.tag_add("{}".format(polword+"wrong0") , "1.{}".format(0),"1.{}".format(len(polword)))
                                                                        
                                                correct_text.tag_config("{}".format(polword+"wrong0"), background="white", foreground="red" , justify = 'center')

                                                correct_text.config(state = "disabled")
                                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                                        bd=2 , relief='ridge' , text = "{}".format(word5) ,bg = "green" ,  command =next_word )
                                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)


                                                uservalue[i][4][2] = self.d
                                                uservalue[i][3][2] = 0
                                                uservalue[i][2][2] +=1

                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                
                rand=randint(0,10)
                randomR = int(rand)
                if randomR != 0 :
                        for i in range(len(uservalue)):
                                date=uservalue[i][4][2]
                                
                                try:    
                                        if date <= self.today:
                                                licz_data +=1
 
                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                                name = ','.join(uservalue [i][1])  
                                                lbl_English = Label(frame21 , font = ('arial' , 18 , 'bold'), bg='#458B74' , bd=2 , relief='ridge' , text = "{}".format(name))
                                                lbl_English.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.05)
                                                Ent_Pol = Entry(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' )
                                                Ent_Pol.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                                Ent_Pol.bind('<Return>' ,lambda x = i : Chuck_word(x) )
                                                Ent_Pol.focus()
                                                break

                                except TypeError :
                                        continue
                else:
                        for i in range(len(uservalue)):
                                date=uservalue[i][4][2]
                                
                                try:    
                                        if date <= "NAUCZONE":
                                                licz_data +=1

                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                                name = ','.join(uservalue [i][1])  
                                                lbl_English = Label(frame21 , font = ('arial' , 18 , 'bold'), bg='#458B74' , bd=2 , relief='ridge' , text = "{}".format(name))
                                                lbl_English.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.05)
                                                Ent_Pol = Entry(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' )
                                                Ent_Pol.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                                Ent_Pol.bind('<Return>' ,lambda x = i : Lerned_word(x))
                                                Ent_Pol.focus()
                                                break

                                except TypeError :
                                        continue

                if licz_data <= 0 :
                        app3 = powtorki()

            count_cwicz3 =0

            for i in range(len(uservalue)):
                date=(uservalue[i][4][2])
                try:
                        if date <= self.today:
                                count_cwicz3 +=1

                except TypeError:
                        continue
            Polish= Button(frame20 ,font = ('arial', 14 , 'bold')  , bd = 2   , justify = 'left', bg='#458B74' ,
             text= "Ćwiczenie 3 - Wpisz Angielskie znaczenie{:>65} Słówek".format(count_cwicz3) ,command = W_ENG_WORD )
            if count_cwicz3 >=1 :
                Polish.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.27)

            def W_POL_WORD():
                shuffle(uservalue)
                licz_data =0

                def next_word():
                        frame21.destroy()
                        app= W_POL_WORD()

                def Chuck_word(event):
                        polword = Ent_Pol.get()
                        cor_Word = uservalue[i][1]

                        Ent_Pol.destroy()
                        correct_text = Text(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,pady = 20 )
                        if len(cor_Word)>=2:
                                polword_split = []
                                count_word=0
                                lengh_word =0
                                for word1 in polword.split(','):
                                        polword_split.append(word1.strip())
                                for ind , word in enumerate(polword_split):
                                        
                                        correct_word = 0
                                        
                                        for word3 in cor_Word:

                                                if word.lower() == word3.lower():

                                                        correct_word+=1
                                                        count_word+=1

                                        if correct_word >0:

                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                                        
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"right") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3
                                                        
                                                correct_text.tag_config("{}".format(word+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"right0"), background="white", foreground="black" , justify = 'center')
                                                
                                        else:

                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"wrong") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3
                                                                                                                        
                                                correct_text.tag_config("{}".format(word+"wrong"), background="white", foreground="red" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"wrong"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"wrong0"), background="white", foreground="red" , justify = 'center')
                                                
                                correct_text.config(state = "disabled")
                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                name = ','.join(cor_Word)
                                        
                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)
                
                                if len(cor_Word)>count_word >0:

                                                uservalue[i][4][3] = self.d
                                                uservalue[i][2][3] +=1
                                                userDane[5] += 1*count_word
                                                userDane[7] += 1*count_word
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                elif len(cor_Word)<=count_word :
                                                
                                                if   uservalue[i][3][3] <= 5:
                                                        uservalue[i][4][3] = self.d
                                                        uservalue[i][3][3] +=1
                                                        uservalue[i][2][3] +=1
                                                        userDane[5] += 1*count_word
                                                        userDane[7] += 1*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                          
                                                        app= W_POL_WORD()
                                                elif   7>=uservalue[i][3][3] > 5:
                                                        
                                                        uservalue[i][4][3] = self.d1
                                                        uservalue[i][3][3] +=1
                                                        uservalue[i][2][3] +=1
                                                        userDane[5] += 1*count_word
                                                        userDane[7] += 1*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
        
        
                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                         
                                                        app= W_POL_WORD()
                                                elif  9>uservalue[i][3][3] > 7:
                                                        
                                                        uservalue[i][4][3] = self.d2
                                                        uservalue[i][3][3] +=1
                                                        uservalue[i][2][3] +=1
                                                        userDane[5] += 2*count_word
                                                        userDane[7] += 2*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(2*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
        
        
                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                          
                                                        app= W_POL_WORD()
                                                elif uservalue[i][3][3] >=9:
                                                        
                                                        uservalue[i][4][3] = "NAUCZONE"
                                                        uservalue[i][3][3] +=1
                                                        uservalue[i][2][3] +=1
                                                        userDane[5] += 10*count_word
                                                        userDane[7] += 10*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(10*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
        
        
                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.04 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                           
                                                        app= W_POL_WORD()        
                                else:
                                                
                                                uservalue[i][2][3] +=1
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))                            
                                        
                        else:
                                for word in cor_Word:
                                        if polword.lower() == word.lower() and  uservalue[i][3][3] <= 5:
                                                
                                                uservalue[i][4][3] = self.d
                                                uservalue[i][3][3] +=1
                                                uservalue[i][2][3] +=1
                                                userDane[5] += 1
                                                userDane[7] += 1
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                
                                                app= W_POL_WORD()
                                        elif polword.lower() == word.lower() and  7>=uservalue[i][3][3] > 5:
                                                
                                                uservalue[i][4][3] = self.d1
                                                uservalue[i][3][3] +=1
                                                uservalue[i][2][3] +=1
                                                userDane[5] += 1
                                                userDane[7] += 1
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )


                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                  
                                                app= W_POL_WORD()
                                        elif polword.lower() == word.lower() and  9>uservalue[i][3][3] > 7:
                                                
                                                uservalue[i][4][3] = self.d2
                                                uservalue[i][3][3] +=1
                                                uservalue[i][2][3] +=1
                                                userDane[5] += 2
                                                userDane[7] += 2
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
  
                                                app= W_POL_WORD()
                                        elif polword.lower() == word.lower() and  uservalue[i][3][3] ==9:
                                                
                                                uservalue[i][4][3] = "NAUCZONE"
                                                uservalue[i][3][3] +=1
                                                uservalue[i][2][3] +=1
                                                userDane[5] += 10
                                                userDane[7] += 10
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                  
                                                app= W_POL_WORD()

                                        else:
                                                
                                                literwka = 0 
                                                dobra_litera = 0 
                                                zla_litera = 0  
                                                slownik = {"a":"ą","c":"ć" , "e" :"ę" , "s" : "ś" , "n" : "ń" , "u":"o" ,"o" :"ó" , "l" :"ł" , "z" : ["ź" , "ż"]}
                                                for word in cor_Word:

                                                        krotnosc = 0
                                                        litera_wys = 0

                                                        for g in range(len(polword)):

                                                                        if g-1+krotnosc>=0  :
                                                                                        try:

                                                                                                if polword[g].lower() == word[g-1+krotnosc].lower():
                                                                                                        if g+1<len(word):
                                                                                                                if polword[g+1].lower() == word[g+1+krotnosc].lower():
                                                                                                                        
                                                                                                                        if krotnosc == 0:
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera +=1
                                                                                                                                
                                                                                                                        elif krotnosc ==1 :
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                dobra_litera +=1
                                                                                                                                
                                                                                                                        else:
                                                                                                                                literwka +=1   
                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1
                                                                                                                                
                                                                                                                elif polword[g-1].lower() == word[g-1+krotnosc].lower():
                                                                                                                        
                                                                                                                        zla_litera +=1   
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold'), justify = 'center')
                                                                                                                
                                                                                                                
                                                                                                                else:
                                                                                                                        
                                                                                                                        literwka +=1   
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                        krotnosc -=1

                                                                                                        elif polword[g-1].lower() == word[g-1+krotnosc].lower():
                                                                                                                
                                                                                                                zla_litera +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold'), justify = 'center')
                                                                                                                
                                                                                                                
                                                                                                        else:
                                                                                                                
                                                                                                                literwka +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                krotnosc -=1
                                                                                                


                                                                                                elif polword[g].lower() in slownik and word[g-1+krotnosc] in slownik.values():
                                                                                                        
                                                                                                        try:
                                                                                                                if word[g-1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                        if polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower() and polword[g+krotnosc].lower() != word[g+krotnosc].lower():
                                                                                                                                
                                                                                                                                literwka +=1  
                                                                                                                                
                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1

                                                                                                                        elif polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower() and polword[g+krotnosc].lower() == word[g+krotnosc].lower(): 
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera+=1
                                                                                                                        else:
                                                                                                                                if polword[g].lower() == word[g-1+krotnosc].lower():
                                                                                                                                        if polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower():
                                                                                                                                                
                                                                                                                                                literwka +=1   
                                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                                krotnosc +=1
                                                                                                                                                litera_wys+=1
                                                                                                                                        else:
                                                                                                                                                
                                                                                                                                                literwka +=1   
                                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                
                                                                                                                                else: 
                                                                                                                                                
                                                                                                                                                literwka +=1  
                                                                                                                                                
                                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                                krotnosc -=1
                                                                                                                                        
                                                                                                                elif polword[g].lower() == word[g+krotnosc].lower():

                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        if krotnosc ==0:
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera+=1
                                                                                                                                
                                                                                                                        else:
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                literwka +=1 
                                                                                                                                
                                                                                                                elif polword[g].lower() in slownik and word[g+krotnosc] in slownik.values():

                                                                                                                        if word[g+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                
                                                                                                                                literwka +=1    
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                        elif polword[g].lower() == word[g+1+krotnosc].lower():

                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "_{}". format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                                        elif polword[g].lower() in slownik and word[g+1] in slownik.values():
                                                                                                                                
                                                                                                        
                                                                                                                                if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                        
                                                                                                                                        literwka +=1   
                                                                                                                                        
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1 
                                                                                                                                else: 
                                                                                                                                        
                                                                                                                                        zla_litera += 1
                                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                        else: 
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                                elif polword[g].lower() == word[g+1+krotnosc].lower():
                                                                                                                        
                                                                                                                        literwka +=1 
                                                                                                                        
                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                        krotnosc +=1
                                                                                                                        litera_wys+=1
                                                                                                                elif polword[g].lower() in slownik and word[g+1+krotnosc] in slownik.values():
                                                                                                                        
                                                                                                
                                                                                                                        if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                
                                                                                                                                literwka +=1 
                                                                                                                                
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1
                                                                                                                        else: 
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')


                                                                                                                else :
                                                                                                                        
                                                                                                                        zla_litera += 1
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center') 

                                                                                                        except ( IndexError , KeyError ) :

                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                

                                                                                                elif polword[g].lower() == word[g+krotnosc].lower():

                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        if krotnosc ==0:
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                dobra_litera +=1
                                                                                                                
                                                                                                        else:
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                elif polword[g].lower() in slownik and word[g+krotnosc] in slownik.values():

                                                                                                        if word[g+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                        else: 
                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                elif polword[g].lower() == word[g+1+krotnosc].lower():
                                                
                                                                                                        if polword[g-1].lower() == word[g-1+krotnosc].lower()  :
                                                                                                                
                                                                                                                if g+1 <len(polword):

                                                                                                                        if polword[g+1].lower() == word[g+krotnosc].lower()  :
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                                        else:
                                                                                                                                
                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                                else:
                                                                                                                                
                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                        elif polword[g-1].lower() in slownik and word[g-1+krotnosc] in slownik.values():
                                                                                                                
                                                                                                                if word[g-1+krotnosc].lower() in slownik[polword[g-1].lower()]:
                                                                                                                        
                                                                                                                        if polword[g+1].lower() in slownik and word[g+krotnosc] in slownik.values() or polword[g+1].lower() == word[g+krotnosc].lower():
                                                                                                                                
                                                                                                                                if word[g+krotnosc].lower() in slownik[polword[g+1].lower()] or polword[g+1].lower() == word[g+krotnosc].lower():
                                                                                                                                        
                                                                                                                                        zla_litera += 1
                                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                                else:
                                                                                                                                        
                                                                                                                                        literwka +=1  
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1
                                                                                                                        else:
                                                                                                                                        
                                                                                                                                        literwka +=1  
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1
                                                                                                        else:
                                                                                                                
                                                                                                                literwka +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                
                                                                                                
                                                                                                
                                                                                                elif polword[g].lower() in slownik and word[g+1+krotnosc] in slownik.values():

                                                                                                        if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                krotnosc+=1 
                                                                                                                litera_wys+=1 
                                                                                                        else: 
                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                else: 
                                                                                                        
                                                                                                        zla_litera += 1
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        except ( IndexError , KeyError ) :

                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                        else:
                                                                                try:
                                                                                        if polword[g].lower() == word[g].lower():
                                                                                                
                                                                                                dobra_litera += 1 
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                        elif polword[g].lower() in slownik and word[g] in slownik.values():
                                                                                                
                                                                                                if word[g].lower() in slownik[polword[g].lower()]:
                                                                                                        
                                                                                                        literwka +=1    
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                else :
                                                                                                        
                                                                                                        zla_litera += 1
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        else:
                                                                                                
                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                except ( IndexError , KeyError ) :

                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                        correct_text.config(state = "disabled")
                                                        correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                                        
                                                        for name in cor_Word:
                                                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)

                                                        if ((literwka+dobra_litera) / len(word))*10 >=8:

                                                                uservalue[i][4][3] = self.d
                                                                
                                                                uservalue[i][2][3] +=1
                                                                userDane[5] += 1
                                                                userDane[7] += 1
                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                
                                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                for x in range(3,8):
                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                        label1.update()
                                                                        time.sleep(0.1)
                                                                        if x >=7:
                                                                                label1.place_forget()
                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                
                                                        
                                                        else:
                                                                print("do poprawy")


                def Lerned_word(event ):
                        polword = Ent_Pol.get()
                        cor_Word = uservalue[i][1]

                        Ent_Pol.destroy()
                        correct_text = Text(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,pady = 20 )
                        if len(cor_Word)>=2:
                                polword_split = []
                                
                                count_word=0
                                lengh_word =0
                                for word1 in polword.split(','):
                                        polword_split.append(word1.strip())
                                for ind , word in enumerate(polword_split):
                                        correct_word = 0

                                        for word3 in cor_Word:
                                                
                                        
                                                if word.lower() == word3.lower():
                                                        
                                                        correct_word+=1
                                                        count_word+=1

                                        if correct_word >0:
                                                
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                        
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"right") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3
                                
                                                correct_text.tag_config("{}".format(word+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"right0"), background="white", foreground="black" , justify = 'center')
                                                
                                        else:
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"wrong") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3

                                                                                                                        
                                                correct_text.tag_config("{}".format(word+"wrong"), background="white", foreground="red" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"wrong"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"wrong0"), background="white", foreground="red" , justify = 'center')
                                                
                                correct_text.config(state = "disabled")
                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                name = ','.join(cor_Word)
                                        
                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)    

                                if len(cor_Word)>count_word >0:

                                        uservalue[i][4][3] = self.d
                                        uservalue[i][3][3] = 0
                                        uservalue[i][2][3] +=1

                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                        
                                elif len(cor_Word)<=count_word :
                                                
                                        userDane[5] += 10*count_word
                                        userDane[7] += 10*count_word
                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                        
                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(10*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
                                        for x in range(3,8):
                                                label1.place(relwidth = 0.06 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                label1.update()
                                                time.sleep(0.1)
                                                if x >=7:
                                                        label1.place_forget()
                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
  
                                        app= W_POL_WORD()

                                else:
                                        uservalue[i][4][3] = self.d
                                        uservalue[i][3][3] = 0
                                        uservalue[i][2][3] +=1
                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))    
                        else:
                                for word5 in cor_Word:
                                        if polword.lower() == word5.lower() :

                                                userDane[5] += 10
                                                userDane[7] += 10
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.04 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
  
                                                app= W_POL_WORD()
                                        else:

                                                correct_text.insert(END, "{}".format(polword))
                                                correct_text.tag_add("{}".format(polword+"wrong0") , "1.{}".format(0),"1.{}".format(len(polword)))
                                                                        
                                                correct_text.tag_config("{}".format(polword+"wrong0"), background="white", foreground="red" , justify = 'center')

                                                correct_text.config(state = "disabled")
                                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                                        bd=2 , relief='ridge' , text = "{}".format(word5) ,bg = "green" ,  command =next_word )
                                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)


                                                uservalue[i][4][3] = self.d
                                                uservalue[i][3][3] = 0
                                                uservalue[i][2][3] +=1

                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                rand=randint(0,10)
                randomR = int(rand)
                if randomR != 0 :
                        for i in range(len(uservalue)):
                                date=uservalue[i][4][3]
                                try:
                                        if date <= self.today:
                                                licz_data +=1
                                                

                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                                name = ','.join(uservalue [i][0])  
                                                lbl_English = Label(frame21 , font = ('arial' , 18 , 'bold'), bg='#458B74' , bd=2 , relief='ridge' , text = "{}".format(name))
                                                lbl_English.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.05)
                                                Ent_Pol = Entry(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' )
                                                Ent_Pol.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                                Ent_Pol.bind('<Return>' ,lambda x = i : Chuck_word(x) )
                                                Ent_Pol.focus()
                                                break

                                except TypeError:
                                                continue
                else:
                        for i in range(len(uservalue)):
                                date=uservalue[i][4][3]
                                try:
                                        if date <= "NAUCZONE":
                                                licz_data +=1
                                                

                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                                name = ','.join(uservalue [i][0])  
                                                lbl_English = Label(frame21 , font = ('arial' , 18 , 'bold'), bg='#458B74' , bd=2 , relief='ridge' , text = "{}".format(name))
                                                lbl_English.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.05)
                                                Ent_Pol = Entry(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' )
                                                Ent_Pol.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                                Ent_Pol.bind('<Return>' ,lambda x = i : Lerned_word(x) )
                                                Ent_Pol.focus()
                                                break

                                except TypeError:
                                                continue
                if licz_data <= 0 :
                                app3 = powtorki()
                    
            count_cwicz4 =0
            for i in range(len(uservalue)):
                date=(uservalue[i][4][3])
                try:
                        if date <= self.today:
                                count_cwicz4 +=1
                        
                except TypeError:
                        
                        continue

            English= Button(frame20 ,font = ('arial', 14 , 'bold')  , bd = 2   , justify = 'left' , bg='#458B74' ,
             text= "Ćwiczenie 4  - Wpisz Polskie znaczenie{:>65} Słówek".format(count_cwicz4), command = W_POL_WORD)
            if count_cwicz4 >=1 :
                English.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.38)

            def ze_S ():
                shuffle(uservalue)
                licz_data =0

                def next_word():
                        frame21.destroy()
                        app= ze_S()
                def Chuck_word_ze_S (event):
                        polword = ze_S_ENG.get()

                        cor_Word = uservalue[i][0]

                        ze_S_ENG.destroy()
                        correct_text = Text(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,pady = 20 )
                        if len(cor_Word)>=2:
                                polword_split = []
                                count_word=0

                                lengh_word =0
                                for word1 in polword.split(','):
                                        polword_split.append(word1.strip())
                                for ind , word in enumerate(polword_split):
                                        
                                        correct_word = 0
                                        
                                        for word3 in cor_Word:

                                                if word.lower() == word3.lower():
                                                        
                                                        correct_word+=1
                                                        count_word+=1

                                        if correct_word >0:
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                                        
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"right") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3
                                                                                                                        
                                                correct_text.tag_config("{}".format(word+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"right0"), background="white", foreground="black" , justify = 'center')
                                                
                                        else:

                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                                        
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"wrong") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3
                                                                                                                        
                                                correct_text.tag_config("{}".format(word+"wrong"), background="white", foreground="red" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"wrong"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"wrong0"), background="white", foreground="red" , justify = 'center')
                                                
                                correct_text.config(state = "disabled")
                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                word1 = ','.join(uservalue[i][0])
                                word_trans = Label(frame21 , font = ('arial' , 18 , 'bold') ,
                                bd=2 , relief='ridge', text = "{}".format(word1))
                                word_trans.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.08)

                                name = ','.join(cor_Word)
                                        
                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)

                                if len(cor_Word)>count_word >0:

                                                uservalue[i][4][4] = self.d
                                                
                                                uservalue[i][2][4] +=1
                                                userDane[5] += 1*count_word
                                                userDane[7] += 1*count_word
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )


                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                elif len(cor_Word)<=count_word :
                                                
                                                if   uservalue[i][3][4] <= 5:
                                                        uservalue[i][4][4] = self.d
                                                        uservalue[i][3][4] +=1
                                                        uservalue[i][2][4] +=1
                                                        userDane[5] += 1*count_word
                                                        userDane[7] += 1*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
                
                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                           
                                                        app= ze_S()
                                                elif   7>=uservalue[i][3][4] > 5:
                                                        
                                                        uservalue[i][4][4] = self.d1
                                                        uservalue[i][3][4] +=1
                                                        uservalue[i][2][4] +=1
                                                        userDane[5] += 1*count_word
                                                        userDane[7] += 1*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
        
        
                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                         
                                                        app= ze_S()
                                                elif  9>uservalue[i][3][4] > 7:
                                                        
                                                        uservalue[i][4][4] = self.d2
                                                        uservalue[i][3][4] +=1
                                                        uservalue[i][2][4] +=1
                                                        userDane[5] += 2*count_word
                                                        userDane[7] += 2*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(2*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
        
        
                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                          
                                                        app= ze_S()
                                                elif uservalue[i][3][4] >=9:
                                                        
                                                        uservalue[i][4][4] = "NAUCZONE"
                                                        uservalue[i][3][4] +=1
                                                        uservalue[i][2][4] +=1
                                                        userDane[5] += 10*count_word
                                                        userDane[7] += 10*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(10*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
        
        
                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.04 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                        
                                                        app= ze_S()        
                                else:
                                                
                                                uservalue[i][2][4] +=1
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))                            
                                
                        else:
                                for word in cor_Word:
                                        if polword.lower() == word.lower() and  uservalue[i][3][4] <= 5:
                                                
                                                uservalue[i][4][4] = self.d
                                                uservalue[i][3][4] +=1
                                                uservalue[i][2][4] +=1
                                                userDane[5] += 1
                                                userDane[7] += 1
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                 
                                                app= ze_S()
                                        elif polword.lower() == word.lower() and  7>=uservalue[i][3][4] > 5:
                                                
                                                uservalue[i][4][4] = self.d1
                                                uservalue[i][3][4] +=1
                                                uservalue[i][2][4] +=1
                                                userDane[5] += 1
                                                userDane[7] += 1
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )


                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                   
                                                app= ze_S()
                                        elif polword.lower() == word.lower() and  9>uservalue[i][3][4] > 7:
                                                
                                                uservalue[i][4][4] = self.d2
                                                uservalue[i][3][4] +=1
                                                uservalue[i][2][4] +=1
                                                userDane[5] += 2
                                                userDane[7] += 2
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )


                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                  
                                                app= ze_S()
                                        elif polword.lower() == word.lower() and  uservalue[i][3][4] ==9:
                                                
                                                uservalue[i][4][4] = "NAUCZONE"
                                                uservalue[i][3][4] +=1
                                                uservalue[i][2][4] +=1
                                                userDane[5] += 10
                                                userDane[7] += 10
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                  
                                                app= ze_S()

                                        else:
                                                
                                                literwka = 0 
                                                dobra_litera = 0 
                                                zla_litera = 0  
                                                slownik = {"a":"ą","c":"ć" , "e" :"ę" , "s" : "ś" , "n" : "ń" , "u":"o" ,"o" :"ó" , "l" :"ł" , "z" : ["ź" , "ż"]}
                                                for word in cor_Word:

                                                        krotnosc = 0
                                                        litera_wys = 0

                                                        for g in range(len(polword)):

                                                                        if g-1+krotnosc>=0  :
                                                                                        try:

                                                                                                if polword[g].lower() == word[g-1+krotnosc].lower():
                                                                                                        if g+1<len(word):
                                                                                                                if polword[g+1].lower() == word[g+1+krotnosc].lower():
                                                                                                                        if krotnosc == 0:
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera +=1
                                                                                                                                
                                                                                                                        elif krotnosc ==1 :
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                dobra_litera +=1
                                                                                                                                
                                                                                                                        else:
                                                                                                                                literwka +=1   
                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1
                                                                                                                                
                                                                                                                elif polword[g-1].lower() == word[g-1+krotnosc].lower():
                                                                                                                        
                                                                                                                        zla_litera +=1   
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold'), justify = 'center')
                                                                                                                
                                                                                                                
                                                                                                                else:
                                                                                                                        
                                                                                                                        literwka +=1   
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                        krotnosc -=1

                                                                                                        elif polword[g-1].lower() == word[g-1+krotnosc].lower():
                                                                                                                
                                                                                                                zla_litera +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold'), justify = 'center')
                                                                                                                
                                                                                                                
                                                                                                        else:
                                                                                                                
                                                                                                                literwka +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                krotnosc -=1
                                                                                                


                                                                                                elif polword[g].lower() in slownik and word[g-1+krotnosc] in slownik.values():
                                                                                                        
                                                                                                        try:
                                                                                                                if word[g-1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                        if polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower() and polword[g+krotnosc].lower() != word[g+krotnosc].lower():
                                                                                                                                literwka +=1  
                                                                                                                                
                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1
                                                                                                                        elif polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower() and polword[g+krotnosc].lower() == word[g+krotnosc].lower():
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera+=1
                                                                                                                        else:
                                                                                                                                if polword[g].lower() == word[g-1+krotnosc].lower():
                                                                                                                                        if polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower():
                                                                                                                                                literwka +=1   
                                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                                krotnosc +=1
                                                                                                                                                litera_wys+=1
                                                                                                                                        else:
                                                                                                                                                
                                                                                                                                                literwka +=1   
                                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                
                                                                                                                                else: 
                                                                                                                                                
                                                                                                                                                literwka +=1  
                                                                                                                                                
                                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                                krotnosc -=1
                                                                                                                                        
                                                                                                                elif polword[g].lower() == word[g+krotnosc].lower():

                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        if krotnosc ==0:
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera+=1
                                                                                                                                
                                                                                                                        else:
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                literwka +=1 
                                                                                                                                
                                                                                                                elif polword[g].lower() in slownik and word[g+krotnosc] in slownik.values():
                                                                                                                        
                                                                                                
                                                                                                                        if word[g+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                
                                                                                                                                literwka +=1    
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                        elif polword[g].lower() == word[g+1+krotnosc].lower():

                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                                        elif polword[g].lower() in slownik and word[g+1] in slownik.values():
                                                                                                                                
                                                                                                        
                                                                                                                                if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                        
                                                                                                                                        literwka +=1   
                                                                                                                                        
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1 
                                                                                                                                else: 
                                                                                                                                        
                                                                                                                                        zla_litera += 1
                                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                        else: 
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                                elif polword[g].lower() == word[g+1+krotnosc].lower():
                                                                                                                        
                                                                                                                        literwka +=1 

                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                        krotnosc +=1
                                                                                                                        litera_wys+=1
                                                                                                                elif polword[g].lower() in slownik and word[g+1+krotnosc] in slownik.values():
                                                                                                                        
                                                                                                
                                                                                                                        if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                
                                                                                                                                literwka +=1 
                                                                                                                                
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1
                                                                                                                        else: 
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')


                                                                                                                else :
                                                                                                                        
                                                                                                                        zla_litera += 1
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center') 

                                                                                                        except ( IndexError , KeyError ) :

                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                

                                                                                                elif polword[g].lower() == word[g+krotnosc].lower():
                                                                                                        
                                                                                                        
                                                                                                        
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        if krotnosc ==0:
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                dobra_litera +=1
                                                                                                                
                                                                                                        else:
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                elif polword[g].lower() in slownik and word[g+krotnosc] in slownik.values():
                                                                                                        
                                                                                                
                                                                                                        if word[g+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                        else: 
                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                elif polword[g].lower() == word[g+1+krotnosc].lower():

                                                                                                        if polword[g-1].lower() == word[g-1+krotnosc].lower()  :
                                                                                                                
                                                                                                                if g+1 <len(polword):

                                                                                                                        if polword[g+1].lower() == word[g+krotnosc].lower()  :
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                                        else:
                                                                                                                                
                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                                else:
                                                                                                                                
                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                        elif polword[g-1].lower() in slownik and word[g-1+krotnosc] in slownik.values():
                                                                                                                
                                                                                                                if word[g-1+krotnosc].lower() in slownik[polword[g-1].lower()]:
                                                                                                                        
                                                                                                                        if polword[g+1].lower() in slownik and word[g+krotnosc] in slownik.values() or polword[g+1].lower() == word[g+krotnosc].lower():
                                                                                                                                
                                                                                                                                if word[g+krotnosc].lower() in slownik[polword[g+1].lower()] or polword[g+1].lower() == word[g+krotnosc].lower():
                                                                                                                                        
                                                                                                                                        zla_litera += 1
                                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                                else:
                                                                                                                                        
                                                                                                                                        literwka +=1  
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1
                                                                                                                        else:
                                                                                                                                        
                                                                                                                                        literwka +=1  
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1
                                                                                                        else:
                                                                                                                
                                                                                                                literwka +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                
                                                                                                
                                                                                                
                                                                                                elif polword[g].lower() in slownik and word[g+1+krotnosc] in slownik.values():
                                                                                                        
                                                                                                
                                                                                                        if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                krotnosc+=1 
                                                                                                                litera_wys+=1 
                                                                                                        else: 
                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                else: 
                                                                                                        
                                                                                                        zla_litera += 1
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        except ( IndexError , KeyError ) :

                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                        else:
                                                                                try:
                                                                                        if polword[g].lower() == word[g].lower():
                                                                                                
                                                                                                dobra_litera += 1 
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                        elif polword[g].lower() in slownik and word[g] in slownik.values():
                                                                                                
                                                                                                if word[g].lower() in slownik[polword[g].lower()]:
                                                                                                        
                                                                                                        literwka +=1    
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                else :
                                                                                                        
                                                                                                        zla_litera += 1
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        elif polword[g].lower() == word[g+1].lower():
                                                                                                        
                                                                                                        literwka += 1 
                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                        krotnosc+=1
                                                                                                        litera_wys+=1
                                                                                        elif polword[g].lower() in slownik and word[g+1] in slownik.values():
                                                                                                        
                                                                                                        if word[g].lower() in slownik[polword[g+1].lower()]:
                                                                                                                
                                                                                                                literwka +=1    
                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                krotnosc+=1
                                                                                                                litera_wys+=1
                                                                                                        else :
                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        else:
                                                                                                
                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                except ( IndexError , KeyError ) :

                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        
                                                        correct_text.config(state = "disabled")
                                                        correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                                        word1 = ','.join(uservalue[i][1])
                                                        word_trans = Label(frame21 , font = ('arial' , 18 , 'bold') ,
                                                        bd=2 , relief='ridge', text = "{}".format(word1))
                                                        word_trans.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.08)

                                                        
                                                        for name in cor_Word:
                                                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                                        lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)

                                                        if ((literwka+dobra_litera) / len(word))*10 >=10:

                                                                uservalue[i][4][4] = self.d
                                                                
                                                                uservalue[i][2][4] +=1
                                                                userDane[5] += 1
                                                                userDane[7] += 1
                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                
                                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                for x in range(3,8):
                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                        label1.update()
                                                                        time.sleep(0.1)
                                                                        if x >=7:
                                                                                label1.place_forget()
                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))


                                                        else:
                                                                print("do poprawy")

                def Lerned_word(event ):
                        polword = ze_S_ENG.get()
                        cor_Word = uservalue[i][0]

                        ze_S_ENG.destroy()
                        correct_text = Text(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,pady = 20 )
                        if len(cor_Word)>=2:
                                polword_split = []
                                
                                count_word=0
                                lengh_word =0
                                for word1 in polword.split(','):
                                        polword_split.append(word1.strip())
                                for ind , word in enumerate(polword_split):
                                        correct_word = 0

                                        for word3 in cor_Word:
                                                
                                        
                                                if word.lower() == word3.lower():
                                                        
                                                        correct_word+=1
                                                        count_word+=1

                                        if correct_word >0:
                                                
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                        
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"right") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3
                                
                                                correct_text.tag_config("{}".format(word+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"right0"), background="white", foreground="black" , justify = 'center')
                                                
                                        else:
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"wrong") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3

                                                                                                                        
                                                correct_text.tag_config("{}".format(word+"wrong"), background="white", foreground="red" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"wrong"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"wrong0"), background="white", foreground="red" , justify = 'center')
                                                
                                correct_text.config(state = "disabled")
                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                name = ','.join(cor_Word)
                                        
                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)    

                                if len(cor_Word)>count_word >0:

                                        uservalue[i][4][4] = self.d
                                        uservalue[i][3][4] = 0
                                        uservalue[i][2][4] +=1

                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                        
                                elif len(cor_Word)<=count_word :
                                                
                                        userDane[5] += 10*count_word
                                        userDane[7] += 10*count_word
                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                        
                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(10*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
                                        for x in range(3,8):
                                                label1.place(relwidth = 0.06 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                label1.update()
                                                time.sleep(0.1)
                                                if x >=7:
                                                        label1.place_forget()
                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
   
                                        app= ze_S()

                                else:
                                        uservalue[i][4][4] = self.d
                                        uservalue[i][3][4] = 0
                                        uservalue[i][2][4] +=1
                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))    
                        else:
                                for word5 in cor_Word:
                                        if polword.lower() == word5.lower() :

                                                userDane[5] += 10
                                                userDane[7] += 10
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.04 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
 
                                                app= ze_S()
                                        else:

                                                correct_text.insert(END, "{}".format(polword))
                                                correct_text.tag_add("{}".format(polword+"wrong0") , "1.{}".format(0),"1.{}".format(len(polword)))
                                                                        
                                                correct_text.tag_config("{}".format(polword+"wrong0"), background="white", foreground="red" , justify = 'center')

                                                correct_text.config(state = "disabled")
                                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                                        bd=2 , relief='ridge' , text = "{}".format(word5) ,bg = "green" ,  command =next_word )
                                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)


                                                uservalue[i][4][4] = self.d
                                                uservalue[i][3][4] = 0
                                                uservalue[i][2][4] +=1

                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))


                rand=randint(0,10)
                randomR = int(rand)
                if randomR != 0 :
                        for i in range(len(uservalue)):
                                date=uservalue[i][4][4]

                                try:
                                        if date <= self.today:
                                                licz_data +=1
                                                
                
                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                                def PLAY():
                                                        Engine = pyttsx3.init()
                                                        rate = Engine.getProperty('rate')
                                                        Engine.setProperty('rate', rate-120)
                                                        Engine.say("{}".format(uservalue[i][0]))
                                                        Engine.runAndWait()

                                                Play_Button = Button(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , text = "PLAY" ,
                                                command = PLAY)
                                                Play_Button.place(relwidth = 0.5 , relheight = 0.1 ,relx=0.25 , rely = 0.08)

                                                ze_S_ENG = Entry(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' )
                                                ze_S_ENG.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                                ze_S_ENG.bind('<Return>' ,lambda x = i : Chuck_word_ze_S(x) )
                                                ze_S_ENG.focus()

                                                Engine = pyttsx3.init()
                                                frame21.update()
                                                rate = Engine.getProperty('rate')
                                                Engine.setProperty('rate', rate-100)
                                                
                                                Engine.say("{}".format(uservalue[i][0]))
                                                Engine.runAndWait()

                                                break

                                except TypeError:
                                
                                        continue
                else:
                        for i in range(len(uservalue)):
                                date=uservalue[i][4][4]

                                try:
                                        if date <= "NAUCZONE":
                                                licz_data +=1
                                                
                
                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                                def PLAY():
                                                        Engine = pyttsx3.init()
                                                        rate = Engine.getProperty('rate')
                                                        Engine.setProperty('rate', rate-120)
                                                        Engine.say("{}".format(uservalue[i][0]))
                                                        Engine.runAndWait()

                                                Play_Button = Button(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , text = "PLAY" ,
                                                command = PLAY)
                                                Play_Button.place(relwidth = 0.5 , relheight = 0.1 ,relx=0.25 , rely = 0.08)

                                                ze_S_ENG = Entry(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' )
                                                ze_S_ENG.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                                ze_S_ENG.bind('<Return>' ,lambda x = i : Lerned_word(x))
                                                ze_S_ENG.focus()

                                                Engine = pyttsx3.init()
                                                frame21.update()
                                                rate = Engine.getProperty('rate')
                                                Engine.setProperty('rate', rate-100)
                                                
                                                Engine.say("{}".format(uservalue[i][0]))
                                                Engine.runAndWait()

                                                break

                                except TypeError:
                                
                                        continue

                if licz_data <= 0 :
                        app4 = powtorki()
                       
            count_cwicz5 =0
            for i in range(len(uservalue)):
                date=(uservalue[i][4][4])
                try:
                        if date <= self.today:
                                count_cwicz5 +=1
                        
                except TypeError:
                       
                        continue

            Polish_S= Button(frame20 ,font = ('arial', 14 , 'bold')  , bd = 2   , justify = 'left' , bg='#458B74' ,
             text= "Ćwiczenie 5  - Wpisz Angielskie znaczenie ze słuchu{:>65} Słówek".format(count_cwicz5)  , command = ze_S)
            if count_cwicz5 >=1 :
                Polish_S.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.49)

            def ze_P ():
                shuffle(uservalue)
                licz_data =0

                def next_word():
                        frame21.destroy()
                        app= ze_P()
                def Chuck_word_ze_S (event):
                        polword = ze_S_ENG.get()

                        cor_Word = uservalue[i][1]

                        ze_S_ENG.destroy()
                        correct_text = Text(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,pady = 20 )
                        if len(cor_Word)>=2:
                                polword_split = []
                                count_word=0

                                lengh_word =0
                                for word1 in polword.split(','):
                                        polword_split.append(word1.strip())
                                for ind , word in enumerate(polword_split):
                                        
                                        correct_word = 0
                                        
                                        for word3 in cor_Word:

                                                if word.lower() == word3.lower():
                                                        
                                                        correct_word+=1
                                                        count_word+=1


                                        if correct_word >0:

                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                                        
                                                        correct_text.insert(END, "{}". format(word))
                                                        correct_text.tag_add("{}".format(word+"right0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}". format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"right") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}". format(word))
                                                        correct_text.tag_add("{}".format(word+"right") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3
                                                                                                                        
                                                correct_text.tag_config("{}".format(word+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"right0"), background="white", foreground="black" , justify = 'center')
                                                
                                        else:
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                                        
                                                        correct_text.insert(END, "{}". format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}". format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"wrong") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}". format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3
                                                                                                                        
                                                correct_text.tag_config("{}".format(word+"wrong"), background="white", foreground="red" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"wrong"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"wrong0"), background="white", foreground="red" , justify = 'center')
                                                
                                correct_text.config(state = "disabled")
                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                word1 = ','.join(uservalue[i][0])
                                word_trans = Label(frame21 , font = ('arial' , 18 , 'bold') ,
                                bd=2 , relief='ridge', text = "{}".format(word1))
                                word_trans.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.08)

                                name = ','.join(cor_Word)
                                        
                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)
                                print("do nauczenia",count_word)
                                if len(cor_Word)>count_word >0:

                                                uservalue[i][4][5] = self.d
                                                
                                                uservalue[i][2][5] +=1
                                                userDane[5] += 1*count_word
                                                userDane[7] += 1*count_word
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                

                                elif len(cor_Word)<=count_word :
                                                print("4438")
                                                print(uservalue[i][3][5])

                                                if   uservalue[i][3][5] <= 5:
                                                        print("4441")
                                                        uservalue[i][4][5] = self.d
                                                        uservalue[i][3][5] +=1
                                                        uservalue[i][2][5] +=1
                                                        userDane[5] += 1*count_word
                                                        userDane[7] += 1*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                          
                                                        app= ze_P()
                                                elif   7>=uservalue[i][3][5] > 5:
                                                        print("4463")
                                                        
                                                        uservalue[i][4][5] = self.d1
                                                        uservalue[i][3][5] +=1
                                                        uservalue[i][2][5] +=1
                                                        userDane[5] += 1*count_word
                                                        userDane[7] += 1*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(1*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                         
                                                        app= ze_P()
                                                elif  9>uservalue[i][3][5] > 7:
                                                        print("4486")
                                                        
                                                        uservalue[i][4][5] = self.d2
                                                        uservalue[i][3][5] +=1
                                                        uservalue[i][2][5] +=1
                                                        userDane[5] += 2*count_word
                                                        userDane[7] += 2*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(2*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                           
                                                        app= ze_P()
                                                elif   uservalue[i][3][5]>=9:
                                                
                                                        uservalue[i][4][5] = "NAUCZONE"
                                                        uservalue[i][3][5] +=1
                                                        uservalue[i][2][5] +=1
                                                        userDane[5] += 10*count_word
                                                        userDane[7] += 10*count_word
                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                        
                                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(10*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                        for x in range(3,8):
                                                                label1.place(relwidth = 0.04 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                label1.update()
                                                                time.sleep(0.1)
                                                                if x >=7:
                                                                        label1.place_forget()
                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                        
                                                        app= ze_P()        
                                else:
                                                
                                                uservalue[i][2][5] +=1
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))                            
                        
                        else:
                                for word in cor_Word:
                                        if polword.lower() == word.lower() and  uservalue[i][3][5] <= 5:
                                                
                                                uservalue[i][4][5] = self.d
                                                uservalue[i][3][5] +=1
                                                uservalue[i][2][5] +=1
                                                userDane[5] += 1
                                                userDane[7] += 1
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                 
                                                app= ze_P()
                                        elif polword.lower() == word.lower() and  7>=uservalue[i][3][5] > 5:
                                                
                                                uservalue[i][4][5] = self.d1
                                                uservalue[i][3][5] +=1
                                                uservalue[i][2][5] +=1
                                                userDane[5] += 1
                                                userDane[7] += 1
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                 
                                                app= ze_P()
                                        elif polword.lower() == word.lower() and  9>uservalue[i][3][5] > 7:
                                                
                                                uservalue[i][4][5] = self.d2
                                                uservalue[i][3][5] +=1
                                                uservalue[i][2][5] +=1
                                                userDane[5] += 2
                                                userDane[7] += 2
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                 
                                                app= ze_P()
                                        elif polword.lower() == word.lower() and  uservalue[i][3][5] ==9:
                                                
                                                uservalue[i][4][5] = "NAUCZONE"
                                                uservalue[i][3][5] +=1
                                                uservalue[i][2][5] +=1
                                                userDane[5] += 10
                                                userDane[7] += 10
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                
                                                app= ze_P()

                                        else:
                                                
                                                literwka = 0 
                                                dobra_litera = 0 
                                                zla_litera = 0  
                                                slownik = {"a":"ą","c":"ć" , "e" :"ę" , "s" : "ś" , "n" : "ń" , "u":"o" ,"o" :"ó" , "l" :"ł" , "z" : ["ź" , "ż"]}
                                                for word in cor_Word:

                                                        krotnosc = 0
                                                        litera_wys = 0

                                                        for g in range(len(polword)):

                                                                        if g-1+krotnosc>=0  :
                                                                                        try:

                                                                                                if polword[g].lower() == word[g-1+krotnosc].lower():
                                                                                                        if g+1<len(word):
                                                                                                                if polword[g+1].lower() == word[g+1+krotnosc].lower():
                                                                                                                        if krotnosc == 0:
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera +=1
                                                                                                                                
                                                                                                                        elif krotnosc ==1 :
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                dobra_litera +=1
                                                                                                                                
                                                                                                                        else:
                                                                                                                                literwka +=1   
                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1
                                                                                                                                
                                                                                                                elif polword[g-1].lower() == word[g-1+krotnosc].lower():
                                                                                                                        
                                                                                                                        zla_litera +=1   
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold'), justify = 'center')
                                                                                                                
                                                                                                                
                                                                                                                else:
                                                                                                                        
                                                                                                                        literwka +=1   
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                        krotnosc -=1

                                                                                                        elif polword[g-1].lower() == word[g-1+krotnosc].lower():
                                                                                                                
                                                                                                                zla_litera +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold'), justify = 'center')

                                                                                                        else:
                                                                                                                
                                                                                                                literwka +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                krotnosc -=1
                                                                                                


                                                                                                elif polword[g].lower() in slownik and word[g-1+krotnosc] in slownik.values():
                                                                                                        
                                                                                                        try:
                                                                                                                if word[g-1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                        if polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower() and polword[g+krotnosc].lower() != word[g+krotnosc].lower():
                                                                                                                                
                                                                                                                                literwka +=1  
                                                                                                                                
                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1
                                                                                                                        elif polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower() and polword[g+krotnosc].lower() == word[g+krotnosc].lower(): 
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera+=1
                                                                                                                        else:
                                                                                                                                if polword[g].lower() == word[g-1+krotnosc].lower():
                                                                                                                                        if polword[g+1+krotnosc].lower() == word[g+1+krotnosc].lower():
                                                                                                                                                
                                                                                                                                                literwka +=1   
                                                                                                                                                correct_text.insert(END, "{}_".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                                krotnosc +=1
                                                                                                                                                litera_wys+=1
                                                                                                                                        else:
                                                                                                                                                
                                                                                                                                                literwka +=1   
                                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                
                                                                                                                                else: 
                                                                                                                                                        
                                                                                                                                                literwka +=1  
                                                                                                                                                
                                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                                krotnosc -=1
                                                                                                                                        
                                                                                                                elif polword[g].lower() == word[g+krotnosc].lower():

                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        if krotnosc ==0:
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                                dobra_litera+=1
                                                                                                                                
                                                                                                                        else:
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                literwka +=1 
                                                                                                                                
                                                                                                                elif polword[g].lower() in slownik and word[g+krotnosc] in slownik.values():

                                                                                                                        if word[g+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                
                                                                                                                                literwka +=1    
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                        elif polword[g].lower() == word[g+1+krotnosc].lower():
                                                                                                                                
                                                                                                                                
                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                                        elif polword[g].lower() in slownik and word[g+1] in slownik.values():
                                                                                                                        
                                                                                                        
                                                                                                                                if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                        
                                                                                                                                        literwka +=1   
                                                                                                                                        
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1 
                                                                                                                                else: 
                                                                                                                                        
                                                                                                                                        zla_litera += 1
                                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                        else: 
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                                elif polword[g].lower() == word[g+1+krotnosc].lower():
                                                                                                                        
                                                                                                                        literwka +=1 
                                                                                                                        
                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                        krotnosc +=1
                                                                                                                        litera_wys+=1
                                                                                                                elif polword[g].lower() in slownik and word[g+1+krotnosc] in slownik.values():
                                                                                                                        
                                                                                                
                                                                                                                        if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                                
                                                                                                                                literwka +=1 
                                                                                                                                
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                                krotnosc +=1
                                                                                                                                litera_wys+=1
                                                                                                                        else: 
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')


                                                                                                                else :
                                                                                                                        
                                                                                                                        zla_litera += 1
                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center') 

                                                                                                        except ( IndexError , KeyError ) :

                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                

                                                                                                elif polword[g].lower() == word[g+krotnosc].lower():

                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        if krotnosc ==0:
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                                                dobra_litera +=1
                                                                                                                
                                                                                                        else:
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                elif polword[g].lower() in slownik and word[g+krotnosc] in slownik.values():
                                                                                                        
                                                                                                
                                                                                                        if word[g+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                        else: 
                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                elif polword[g].lower() == word[g+1+krotnosc].lower():

                                                                                                        if polword[g-1].lower() == word[g-1+krotnosc].lower()  :
                                                                                                                
                                                                                                                if g+1 <len(polword):

                                                                                                                        if polword[g+1].lower() == word[g+krotnosc].lower()  :
                                                                                                                                
                                                                                                                                zla_litera += 1
                                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                                        else:
                                                                                                                                
                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                                else:
                                                                                                                                
                                                                                                                                literwka +=1  
                                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                krotnosc+=1
                                                                                                                                litera_wys+=1
                                                                                                        elif polword[g-1].lower() in slownik and word[g-1+krotnosc] in slownik.values():
                                                                                                                
                                                                                                                if word[g-1+krotnosc].lower() in slownik[polword[g-1].lower()]:
                                                                                                                        
                                                                                                                        if polword[g+1].lower() in slownik and word[g+krotnosc] in slownik.values() or polword[g+1].lower() == word[g+krotnosc].lower():
                                                                                                                                
                                                                                                                                if word[g+krotnosc].lower() in slownik[polword[g+1].lower()] or polword[g+1].lower() == word[g+krotnosc].lower():
                                                                                                                                        
                                                                                                                                        zla_litera += 1
                                                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                                                                else:
                                                                                                                                        
                                                                                                                                        literwka +=1  
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1
                                                                                                                        else:
                                                                                                                                        
                                                                                                                                        literwka +=1  
                                                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                                                        krotnosc+=1
                                                                                                                                        litera_wys+=1
                                                                                                        else:
                                                                                                                
                                                                                                                literwka +=1   
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                
                                                                                                
                                                                                                
                                                                                                elif polword[g].lower() in slownik and word[g+1+krotnosc] in slownik.values():
                                                                                                        
                                                                                                
                                                                                                        if word[g+1+krotnosc].lower() in slownik[polword[g].lower()]:
                                                                                                                
                                                                                                                literwka +=1 
                                                                                                                
                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                krotnosc+=1 
                                                                                                                litera_wys+=1 
                                                                                                        else: 
                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                                                                else: 
                                                                                                        
                                                                                                        zla_litera += 1
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        except ( IndexError , KeyError ) :

                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                        else:
                                                                                try:
                                                                                        if polword[g].lower() == word[g].lower():
                                                                                                
                                                                                                dobra_litera += 1 
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="black" , justify = 'center')
                                                                                        elif polword[g].lower() in slownik and word[g] in slownik.values():
                                                                                                
                                                                                                if word[g].lower() in slownik[polword[g].lower()]:
                                                                                                        
                                                                                                        literwka +=1    
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                else :
                                                                                                        
                                                                                                        zla_litera += 1
                                                                                                        correct_text.insert(END, "{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        elif polword[g].lower() == word[g+1].lower():
                                                                                                        
                                                                                                        literwka += 1 
                                                                                                        correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                        correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                        correct_text.tag_config("{}".format(g), background="white", foreground="orange" , justify = 'center')
                                                                                                        krotnosc+=1
                                                                                                        litera_wys+=1
                                                                                        elif polword[g].lower() in slownik and word[g+1] in slownik.values():
                                                                                                        
                                                                                                        if word[g].lower() in slownik[polword[g+1].lower()]:
                                                                                                        
                                                                                                                literwka +=1    
                                                                                                                correct_text.insert(END, "_{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+2+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="orange" , font = ('arial' , 25 , 'bold') , justify = 'center')
                                                                                                                krotnosc+=1
                                                                                                                litera_wys+=1
                                                                                                        else :
                                                                                                                
                                                                                                                zla_litera += 1
                                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                        else:
                                                                                                
                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')
                                                                                except ( IndexError , KeyError ) :

                                                                                                zla_litera += 1
                                                                                                correct_text.insert(END, "{}".format(polword[g]))
                                                                                                correct_text.tag_add("{}".format(g) , "1.{}".format(g+litera_wys),"1.{}".format(g+1+litera_wys))
                                                                                                correct_text.tag_config("{}".format(g), background="white", foreground="red" , font = ('arial' , 27 , 'bold') , justify = 'center')

                                                        correct_text.config(state = "disabled")
                                                        correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                                        word1 = ','.join(uservalue[i][0])
                                                        word_trans = Label(frame21 , font = ('arial' , 18 , 'bold') ,
                                                        bd=2 , relief='ridge', text = "{}".format(word1))
                                                        word_trans.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.08)

                                                        
                                                        for name in cor_Word:
                                                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                                        lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)

                                                        if ((literwka+dobra_litera) / len(word))*10 >=10:

                                                                uservalue[i][4][5] = self.d
                                                                
                                                                uservalue[i][2][5] +=1
                                                                userDane[5] += 1
                                                                userDane[7] += 1
                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                
                                                                label1= Label(frame21 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                for x in range(3,8):
                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                        label1.update()
                                                                        time.sleep(0.1)
                                                                        if x >=7:
                                                                                label1.place_forget()
                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))

                                                        else:
                                                                print("do poprawy")

                def Lerned_word(event):
                        polword = ze_S_ENG.get()
                        cor_Word = uservalue[i][1]

                        ze_S_ENG.destroy()
                        correct_text = Text(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,pady = 20 )
                        if len(cor_Word)>=2:
                                polword_split = []
                                
                                count_word=0
                                lengh_word =0
                                for word1 in polword.split(','):
                                        polword_split.append(word1.strip())
                                for ind , word in enumerate(polword_split):
                                        correct_word = 0

                                        for word3 in cor_Word:
                                                
                                        
                                                if word.lower() == word3.lower():
                                                        
                                                        correct_word+=1
                                                        count_word+=1

                                        if correct_word >0:
                                                
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                        
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"right") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"right") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3
                                
                                                correct_text.tag_config("{}".format(word+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"right"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"right0"), background="white", foreground="black" , justify = 'center')
                                                
                                        else:
                                                
                                                if ind==0:
                                                        lengh_word+=len(polword_split[0])+3
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong0") , "1.{}".format(ind),"1.{}".format(ind+len(word)))
                                                else:

                                                        correct_text.insert(END, "{}".format(' , '))
                                                        correct_text.tag_add("{}".format(str(ind)+"wrong") , "1.{}".format(lengh_word-3),"1.{}".format(lengh_word))
                                                        correct_text.insert(END, "{}".format(word))
                                                        correct_text.tag_add("{}".format(word+"wrong") , "1.{}".format(lengh_word),"1.{}".format(lengh_word+1+len(word)))
                                                        lengh_word+=len(polword_split[ind])+3

                                                                                                                        
                                                correct_text.tag_config("{}".format(word+"wrong"), background="white", foreground="red" , justify = 'center')
                                                correct_text.tag_config("{}".format(str(ind)+"wrong"), background="white", foreground="black" , justify = 'center')
                                                correct_text.tag_config("{}".format(word+"wrong0"), background="white", foreground="red" , justify = 'center')
                                                
                                correct_text.config(state = "disabled")
                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                name = ','.join(cor_Word)
                                        
                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                bd=2 , relief='ridge' , text = "{}".format(name) ,bg = "green" ,  command =next_word )
                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)    
                                print("nauczone",count_word)
                                if len(cor_Word)>count_word >0:

                                        uservalue[i][4][5] = self.d
                                        uservalue[i][3][5] = 0
                                        uservalue[i][2][5] +=1

                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                        
                                elif len(cor_Word)<=count_word :
                                                
                                        userDane[5] += 10*count_word
                                        userDane[7] += 10*count_word
                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                        
                                        label1= Label(frame21 , bg = "yellow" , text = "+{}".format(10*count_word),   font = ('arial' , 20 , 'bold') , bd = 4 )
                                        for x in range(3,8):
                                                label1.place(relwidth = 0.06 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                label1.update()
                                                time.sleep(0.1)
                                                if x >=7:
                                                        label1.place_forget()
                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
  
                                        app= ze_P()

                                else:
                                        uservalue[i][4][5] = self.d
                                        uservalue[i][3][5] = 0
                                        uservalue[i][2][5] +=1
                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))    
                        else:
                                for word5 in cor_Word:
                                        if polword.lower() == word5.lower() :

                                                userDane[5] += 10
                                                userDane[7] += 10
                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                
                                                label1= Label(frame21 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                for x in range(3,8):
                                                        label1.place(relwidth = 0.04 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                        label1.update()
                                                        time.sleep(0.1)
                                                        if x >=7:
                                                                label1.place_forget()
                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
   
                                                app= ze_P()
                                        else:

                                                correct_text.insert(END, "{}".format(polword))
                                                correct_text.tag_add("{}".format(polword+"wrong0") , "1.{}".format(0),"1.{}".format(len(polword)))
                                                                        
                                                correct_text.tag_config("{}".format(polword+"wrong0"), background="white", foreground="red" , justify = 'center')

                                                correct_text.config(state = "disabled")
                                                correct_text.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)

                                                lbl_English_COR = Button(frame21 , font = ('arial' , 18 , 'bold') ,
                                                        bd=2 , relief='ridge' , text = "{}".format(word5) ,bg = "green" ,  command =next_word )
                                                lbl_English_COR.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.32)


                                                uservalue[i][4][5] = self.d
                                                uservalue[i][3][5] = 0
                                                uservalue[i][2][5] +=1

                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))


                rand=randint(0,10)
                randomR = int(rand)
                if randomR != 0 :
                        for i in range(len(uservalue)):
                                date=uservalue[i][4][5]

                                try:
                                        if date <= self.today:
                                                licz_data +=1
                                                

                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                                def PLAY():
                                                        Engine = pyttsx3.init()
                                                        rate = Engine.getProperty('rate')
                                                        Engine.setProperty('rate', rate-120)
                                                        Engine.say("{}".format(uservalue[i][0]))
                                                        Engine.runAndWait()

                                                Play_Button = Button(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , text = "PLAY" ,
                                                command = PLAY)
                                                Play_Button.place(relwidth = 0.5 , relheight = 0.1 ,relx=0.25 , rely = 0.08)
                                                

                                                ze_S_ENG = Entry(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' )
                                                ze_S_ENG.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                                ze_S_ENG.bind('<Return>' ,lambda x = i : Chuck_word_ze_S(x) )
                                                ze_S_ENG.focus()

                                                
                                                Engine = pyttsx3.init()
                                                frame21.update()
                                                rate = Engine.getProperty('rate')
                                                Engine.setProperty('rate', rate-100)
                                                
                                                Engine.say("{}".format(uservalue[i][0]))
                                                Engine.runAndWait()
                                                
                                                break

                                except TypeError:
                                
                                        continue
                else:
                        for i in range(len(uservalue)):
                                date=uservalue[i][4][5]

                                try:
                                        if date <= "NAUCZONE":
                                                licz_data +=1
                                                

                                                frame21 = Frame(self.frame1 , bg = "#CCCC99")
                                                frame21.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                                def PLAY():
                                                        Engine = pyttsx3.init()
                                                        rate = Engine.getProperty('rate')
                                                        Engine.setProperty('rate', rate-120)
                                                        Engine.say("{}".format(uservalue[i][0]))
                                                        Engine.runAndWait()

                                                Play_Button = Button(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , text = "PLAY" ,
                                                command = PLAY)
                                                Play_Button.place(relwidth = 0.5 , relheight = 0.1 ,relx=0.25 , rely = 0.08)
                                                

                                                ze_S_ENG = Entry(frame21 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' )
                                                ze_S_ENG.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.20)
                                                ze_S_ENG.bind('<Return>' ,lambda x = i : Lerned_word(x) )
                                                ze_S_ENG.focus()

                                                
                                                Engine = pyttsx3.init()
                                                frame21.update()
                                                rate = Engine.getProperty('rate')
                                                Engine.setProperty('rate', rate-100)
                                                
                                                Engine.say("{}".format(uservalue[i][0]))
                                                Engine.runAndWait()
                                                
                                                break

                                except TypeError:
                                
                                        continue
                if licz_data <= 0 :
                        app5 = powtorki()
            count_cwicz6 =0
            for i in range(len(uservalue)):
                date=(uservalue[i][4][5])
                try:
                        if date <= self.today:
                                count_cwicz6 +=1
                        
                except TypeError:
                        
                        continue

            English_S= Button(frame20 ,font = ('arial', 14 , 'bold')  , bd = 2   , justify = 'left' , bg='#458B74',
             text= "Ćwiczenie 6  - Wpisz Polskie znaczenie ze słuchu{:>65} Słówek".format(count_cwicz6) , command = ze_P)
            if count_cwicz6 >=1 :
                English_S.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.60 )

            def SE_ANG ():
                shuffle(uservalue)
                licz_data = 0
                for i in range(len(uservalue)):
                        date=uservalue[i][4][6]
                        try:

                                if date <= self.today:
                                        licz_data +=1
                                        
                                        frame31 = Frame(self.frame1 , bg = "#CCCC99")
                                        frame31.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                        def new_C():
                                                frame31.destroy()
                                                app=SE_ANG()
                                        def chuc_speak (event):
                                                Ent_speak.update()
                                                polword = Ent_speak.get()
                                            
                                                polword_split = []
                                                cor_Word = uservalue[i][0]
                      
                                                correct_word = 0
                                                for word1 in polword.split(','):
                                                        polword_split.append(word1.strip())
                                      
                                                for ind , word in enumerate(polword_split):
                                                        
                                                        for word3 in cor_Word:
                                                                if word.lower() == word3.lower():
                                                                        correct_word+=1
                                                        if correct_word>0 and  uservalue[i][3][6] < 9:
                                                                uservalue[i][4][6] = self.d
                                                                uservalue[i][3][6] +=1        
                                                                uservalue[i][2][6] +=1
                                                                userDane[5] += 1
                                                                userDane[7] += 1
                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                        
                                                                label1= Label(frame31 , bg = "yellow" , text = "+{}".format(1),   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                for x in range(3,8):
                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                        label1.update()
                                                                        time.sleep(0.1)
                                                                        if x >=7:
                                                                                label1.place_forget()
                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                app=SE_ANG()

                                                        elif correct_word >0 and  uservalue[i][3][6] >=9:
                                                                                      
                                                                uservalue[i][4][6] = "NAUCZONE"
                                                                uservalue[i][3][6] +=1
                                                                uservalue[i][2][6] +=1
                                                                userDane[5] += 10
                                                                userDane[7] += 10
                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                
                                                                label1= Label(frame31 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                for x in range(3,8):
                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                        label1.update()
                                                                        time.sleep(0.1)
                                                                        if x >=7:
                                                                                label1.place_forget()
                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                  
                                                                app=SE_ANG()
                                                        else:
                                                         
                                                                name = ','.join(uservalue[i][0])
                                                                BTN_speak = Button(frame31 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,justify = "center" ,
                                                                text=name , bg="red", command =new_C )
                                                                BTN_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.7)

                                        def speak_button():
                                                cor_Word = uservalue[i][0]
                                                button_Microphone.place_forget()
                                                write_text = 0
                                
                                                r= sr.Recognizer()
                                                with sr.Microphone() as source:

                                                        audio=r.adjust_for_ambient_noise(source)
                                                        speak_label = Label(frame31 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,text = "Say the sentences or word and wait. Don't repeat the word")
                                                        speak_label.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.4)
                                                        speak_label.update()
                                                        try:
                                                                audio =r.listen(source, timeout=10)
                        
                                                                try:
                                                                        text = r.recognize_google(audio , language="en-US")
                                                                
                                                                        Ent_speak.insert("end" ,"{}" .format(text))
                                                                        Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                        Ent_speak.update()
                                                                        
                                                                except:
                                                                
                                                                        speak_label["text"] =  "could you repeat "
                                                                        speak_label.update()
                                                                        time.sleep(0.5)
                                                                        
                                                                        with sr.Microphone() as source:
                                                                        
                                                                                audio=r.adjust_for_ambient_noise(source)
                                                                                audio =r.listen(source)
                                                                        
                                                                                try:
                                                                                        text = r.recognize_google(audio , language="en-US")
                                                                                        Ent_speak.insert("end" ,"{}" .format(text))
                                                                                        Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                                        Ent_speak.update()
                                                                                except:
                                                                                        write_text+=1

                                                                if UnboundLocalError == True or write_text == 1:
                                                                        time.sleep(2)
                                                                
                                                                        ze_S_ENG.place_forget()
                                                                        Ent_speak.delete(0, 'end')
                                                                        Ent_speak.configure(background='white')
                                                                        Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                        Ent_speak.focus()
                                                                        speak_label["text"] =  "type the word"
                                                                                        
                                                                        Ent_speak.bind('<Return>' ,chuc_speak )
                                                                else:
                        
                                                                        if len(cor_Word)>=2:
                                                                                        correct_word=0
                        
                                                                                        for word in cor_Word:
                        
                                                                                                if text.lower() == word.lower():
                                                                                                        correct_word+=1

                                                                                        if correct_word >0 and  uservalue[i][3][6] <= 5:
                                                                        
                                                                                                uservalue[i][4][6] = self.d
                                                                                                uservalue[i][3][6] +=1
                                                                                                uservalue[i][2][6] +=1
                                                                                                userDane[5] += 1
                                                                                                userDane[7] += 1
                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                        
                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                for x in range(3,8):
                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                        label1.update()
                                                                                                        time.sleep(0.1)
                                                                                                        if x >=7:
                                                                                                                label1.place_forget()
                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                           
                                                                                                app=SE_ANG()
                                                                                        elif correct_word >0 and  7>=uservalue[i][3][6] > 5:
                                                                                        
                                                                                                uservalue[i][4][6] = self.d1
                                                                                                uservalue[i][3][6] +=1
                                                                                                uservalue[i][2][6] +=1
                                                                                                userDane[5] += 1
                                                                                                userDane[7] += 1
                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                        
                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                for x in range(3,8):
                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                        label1.update()
                                                                                                        time.sleep(0.1)
                                                                                                        if x >=7:
                                                                                                                label1.place_forget()
                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                         
                                                                                                app=SE_ANG()
                                                                                        elif correct_word >0 and  9>uservalue[i][3][6] > 7:
                                                                                
                                                                                                uservalue[i][4][6] = self.d2
                                                                                                uservalue[i][3][6] +=1
                                                                                                uservalue[i][2][6] +=1
                                                                                                userDane[5] += 2
                                                                                                userDane[7] += 2
                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                        
                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                for x in range(3,8):
                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                        label1.update()
                                                                                                        time.sleep(0.1)
                                                                                                        if x >=7:
                                                                                                                label1.place_forget()
                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                          
                                                                                                app=SE_ANG()
                                                                                        elif correct_word >0 and  uservalue[i][3][6] >=9:
                                                                                        
                                                                                                uservalue[i][4][6] = "NAUCZONE"
                                                                                                uservalue[i][3][6] +=1
                                                                                                uservalue[i][2][6] +=1
                                                                                                userDane[5] += 10
                                                                                                userDane[7] += 10
                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                        
                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                for x in range(3,8):
                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                        label1.update()
                                                                                                        time.sleep(0.1)
                                                                                                        if x >=7:
                                                                                                                label1.place_forget()
                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                         
                                                                                                app=SE_ANG()

                                                                                        else:

                                                                                                Ent_speak.configure(background='red')
                                                                                                
                                                                                                Ent_speak.insert("end" ,"{}" .format(text))
                                                                                                Ent_speak.update()
                                                                                                time.sleep(0.5)

                                                                                                with sr.Microphone() as source:

                                                                                                        audio=r.adjust_for_ambient_noise(source)
                                                                                                        speak_label["text"] =  "Wrong word could you repeat"
                                                                                                        speak_label.update()
                                                                                                
                                                                                                        audio =r.listen(source)
                        
                                                                                                        try:
                                                                                                                text = r.recognize_google(audio , language="en-US")
                                                                                                                Ent_speak.delete(0, 'end')
                                                                                                                Ent_speak.insert("end" ,"{}" .format(text))
                                                                                                                
                                                                                                                Ent_speak.update()
                                                                                                        except:

                                                                                                                with sr.Microphone() as source:
                                                                                                                        
                                                                                                                        audio=r.adjust_for_ambient_noise(source)
                                                                                                                        speak_label["text"] =  "could you repeat "
                                                                                                                        speak_label.update()
                                                                                                        
                                                                                                                        audio =r.listen(source)

                                                                                                                        try:
                                                                                                                                text = r.recognize_google(audio , language="en-US")
                                                                                                                                Ent_speak.insert("end" ,"{}" .format(text))
                                                                                                                                Ent_speak.update()
                                                                                                                        except:
                                                                                                                                write_text+=1
                                                                                                                        
                                                                                                if UnboundLocalError == True or write_text == 1:
                                                                                                
                                                                                                        time.sleep(2)
                                                                                                
                                                                                                        ze_S_ENG.place_forget()
                                                                                                        Ent_speak.delete(0, 'end')
                                                                                                        Ent_speak.configure(background='white')
                                                                                                        Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                                                        Ent_speak.focus()
                                                                                                        speak_label["text"] =  "type the word"
                                                                                                        
                                                                                                        Ent_speak.bind('<Return>' ,chuc_speak )
                                                                                                else:
                                                                                                        correct_word=0
                                                                                                        for word in cor_Word:
                        
                                                                                                                if text.lower() == word.lower():
                                                                                                                
                                                                                                                        correct_word+=1
                                                                                                                
                                                                                                        if correct_word >0 and  uservalue[i][3][6] <= 5:
                                                                                                        
                                                                                                                uservalue[i][4][6] = self.d
                                                                                                                uservalue[i][3][6] +=1
                                                                                                                uservalue[i][2][6] +=1
                                                                                                                userDane[5] += 1
                                                                                                                userDane[7] += 1
                                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                        
                                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                                for x in range(3,8):
                                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                        label1.update()
                                                                                                                        time.sleep(0.1)
                                                                                                                        if x >=7:
                                                                                                                                label1.place_forget()
                                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                         
                                                                                                                app=SE_ANG()
                                                                                                        elif correct_word >0 and  7>=uservalue[i][3][6] > 5:
                                                                                                        
                                                                                                                uservalue[i][4][6] = self.d1
                                                                                                                uservalue[i][3][6] +=1
                                                                                                                uservalue[i][2][6] +=1
                                                                                                                userDane[5] += 1
                                                                                                                userDane[7] += 1
                                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                        
                                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                                        
                                                                                        
                                                                                                                for x in range(3,8):
                                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                        label1.update()
                                                                                                                        time.sleep(0.1)
                                                                                                                        if x >=7:
                                                                                                                                label1.place_forget()
                                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                         
                                                                                                                app=SE_ANG()
                                                                                                        elif correct_word >0 and  9>uservalue[i][3][6] > 7:
                                                                                                        
                                                                                                                uservalue[i][4][6] = self.d2
                                                                                                                uservalue[i][3][6] +=1
                                                                                                                uservalue[i][2][6] +=1
                                                                                                                userDane[5] += 2
                                                                                                                userDane[7] += 2
                                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                        
                                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                                for x in range(3,8):
                                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                        label1.update()
                                                                                                                        time.sleep(0.1)
                                                                                                                        if x >=7:
                                                                                                                                label1.place_forget()
                                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                          
                                                                                                                app=SE_ANG()
                                                                                                        elif correct_word >0 and  uservalue[i][3][6] >=9:
                                                                                                        
                                                                                                                uservalue[i][4][6] = "NAUCZONE"
                                                                                                                uservalue[i][3][6] +=1
                                                                                                                uservalue[i][2][6] +=1
                                                                                                                userDane[5] += 10
                                                                                                                userDane[7] += 10
                                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                        
                                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                                for x in range(3,8):
                                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                        label1.update()
                                                                                                                        time.sleep(0.1)
                                                                                                                        if x >=7:
                                                                                                                                label1.place_forget()
                                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                          
                                                                                                                app=SE_ANG()
                                                                                                        else:
                                                                                                                write_text+=1
                                                                                                        
                                                                                        if write_text>0:
                                                                                                time.sleep(1)
                                                                                        
                                                                                                ze_S_ENG.place_forget()
                                                                                                Ent_speak.configure(background='white')
                                                                                                
                                                                                                speak_label["text"] =  "type the word"
                                                                                                
                                                                                                Ent_speak.bind('<Return>' ,chuc_speak )
                                                                                                
                                                                                                
                                                                        else:
                                                                                if UnboundLocalError == True or write_text == 1:
                                                                                
                                                                                        time.sleep(2)
                                                                                
                                                                                        ze_S_ENG.place_forget()
                                                                                        Ent_speak.delete(0, 'end')
                                                                                        Ent_speak.configure(background='white')
                                                                                        Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                                        Ent_speak.focus()
                                                                                        speak_label["text"] =  "type the word"
                                                                                                
                                                                                        Ent_speak.bind('<Return>' ,chuc_speak )
                                                                                else:
                                                                                        for word in cor_Word:
                                                                                                
                                                                                                if text.lower() == word.lower() and  uservalue[i][3][6] <= 5:
                                                                                        
                                                                                                        uservalue[i][4][6] = self.d
                                                                                                        uservalue[i][3][6] +=1
                                                                                                        uservalue[i][2][6] +=1
                                                                                                        userDane[5] += 1
                                                                                                        userDane[7] += 1
                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                        
                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                        for x in range(3,8):
                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                label1.update()
                                                                                                                time.sleep(0.1)
                                                                                                                if x >=7:
                                                                                                                        label1.place_forget()
                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                          
                                                                                                        app=SE_ANG()
                                                                                                elif text.lower() == word.lower() and  7>=uservalue[i][3][6] > 5:
                                                                                        
                                                                                                        uservalue[i][4][6] = self.d1
                                                                                                        uservalue[i][3][6] +=1
                                                                                                        uservalue[i][2][6] +=1
                                                                                                        userDane[5] += 1
                                                                                                        userDane[7] += 1
                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                        
                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                        for x in range(3,8):
                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                label1.update()
                                                                                                                time.sleep(0.1)
                                                                                                                if x >=7:
                                                                                                                        label1.place_forget()
                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                          
                                                                                                        app=SE_ANG()
                                                                                                elif text.lower() == word.lower() and  9>uservalue[i][3][6] > 7:
                                                                                                
                                                                                                        uservalue[i][4][6] = self.d2
                                                                                                        uservalue[i][3][6] +=1
                                                                                                        uservalue[i][2][6] +=1
                                                                                                        userDane[5] += 2
                                                                                                        userDane[7] += 2
                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                        
                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                        for x in range(3,8):
                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                label1.update()
                                                                                                                time.sleep(0.1)
                                                                                                                if x >=7:
                                                                                                                        label1.place_forget()
                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                         
                                                                                                        app=SE_ANG()
                                                                                                elif text.lower() == word.lower() and  uservalue[i][3][6] >=9:
                                                                                                
                                                                                                        uservalue[i][4][6] = "NAUCZONE"
                                                                                                        uservalue[i][3][6] +=1
                                                                                                        uservalue[i][2][6] +=1
                                                                                                        userDane[5] += 10
                                                                                                        userDane[7] += 10
                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                        
                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                        for x in range(3,8):
                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                label1.update()
                                                                                                                time.sleep(0.1)
                                                                                                                if x >=7:
                                                                                                                        label1.place_forget()
                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                        
                                                                                                        app=SE_ANG()
                                                                                                        
                                                                                                else:

                                                                                                        Ent_speak.configure(background='red')
                                                                                                        Ent_speak.update()

                                                                                                        with sr.Microphone() as source:

                                                                                                                audio=r.adjust_for_ambient_noise(source)
                                                                                                                speak_label["text"] =  "wrong word could you repeat"
                                                                                                                speak_label.update()
                                                                                                                audio =r.listen(source)
                                                                                                                try:
                                                                                                                        text = r.recognize_google(audio , language="en-US")
                                                                                                                
                                                                                                                        Ent_speak.delete(0, 'end')
                                                                                                                        Ent_speak.insert("end" ,"{}" .format(text))
                                                                                                                        Ent_speak.update()
                                                                                                                        
                                                                                                                except:
                                                                                                                        with sr.Microphone() as source:
                                                                                                                                
                                                                                                                                audio=r.adjust_for_ambient_noise(source)
                                                                                                                                speak_label["text"] =  "could you repeat "
                                                                                                                                speak_label.update()
                                                                                                                        
                                                                                                                                audio =r.listen(source)

                                                                                                                                try:
                                                                                                                                        text = r.recognize_google(audio , language="en-US")
                                                                                                                                
                                                                                                                                        Ent_speak.insert("end" ,"{}" .format(text))
                                                                                                                                
                                                                                                                                        Ent_speak.update()
                                                                                                                                except:
                                                                                                                                        write_text+=1
                                                                                                                                        
                                                                                                        if UnboundLocalError == True  or write_text == 1:
                                                                                                        
                                                                                                                time.sleep(2)
                                                                                                        
                                                                                                                ze_S_ENG.place_forget()
                                                                                                                Ent_speak.delete(0, 'end')
                                                                                                                Ent_speak.configure(background='white')
                                                                                                                Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                                                                Ent_speak.focus()
                                                                                                                speak_label["text"] =  "type the word"
                                                                                                                
                                                                                                                Ent_speak.bind('<Return>' ,chuc_speak )
                                                                                                        else:
                                                                                                                correct_word = 0
                                                                                                                for word in cor_Word:
                                                                                                                        
                                                                                                                        if text.lower() == word.lower():
                                                                                                                        
                                                                                                                                correct_word+=1
                                                                                                                        
                                                                                                                if correct_word >0 and  uservalue[i][3][6] <= 5:
                                                                                                        
                                                                                                                        uservalue[i][4][6] = self.d
                                                                                                                        uservalue[i][3][6] +=1
                                                                                                                        uservalue[i][2][6] +=1
                                                                                                                        userDane[5] += 1
                                                                                                                        userDane[7] += 1
                                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                                
                                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                                        for x in range(3,8):
                                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                                label1.update()
                                                                                                                                time.sleep(0.1)
                                                                                                                                if x >=7:
                                                                                                                                        label1.place_forget()
                                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                                   
                                                                                                                        app=SE_ANG()
                                                                                                                elif correct_word >0 and  7>=uservalue[i][3][6] > 5:

                                                                                                                        uservalue[i][4][6] = self.d1
                                                                                                                        uservalue[i][3][6] +=1
                                                                                                                        uservalue[i][2][6] +=1
                                                                                                                        userDane[5] += 1
                                                                                                                        userDane[7] += 1
                                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                                
                                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                                                
                                                                                                
                                                                                                                        for x in range(3,8):
                                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                                label1.update()
                                                                                                                                time.sleep(0.1)
                                                                                                                                if x >=7:
                                                                                                                                        label1.place_forget()
                                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                                  
                                                                                                                        app=SE_ANG()
                                                                                                                elif correct_word >0 and  9>uservalue[i][3][6] > 7:
                                                                                                                
                                                                                                                        uservalue[i][4][6] = self.d2
                                                                                                                        uservalue[i][3][6] +=1
                                                                                                                        uservalue[i][2][6] +=1
                                                                                                                        userDane[5] += 2
                                                                                                                        userDane[7] += 2
                                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                                
                                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                                        for x in range(3,8):
                                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                                label1.update()
                                                                                                                                time.sleep(0.1)
                                                                                                                                if x >=7:
                                                                                                                                        label1.place_forget()
                                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                                 
                                                                                                                        app=SE_ANG()
                                                                                                                elif correct_word >0 and  uservalue[i][3][6] >=9:

                                                                                                                        uservalue[i][4][6] = "NAUCZONE"
                                                                                                                        uservalue[i][3][6] +=1
                                                                                                                        uservalue[i][2][6] +=1
                                                                                                                        userDane[5] += 10
                                                                                                                        userDane[7] += 10
                                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                                
                                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                                        for x in range(3,8):
                                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                                label1.update()
                                                                                                                                time.sleep(0.1)
                                                                                                                                if x >=7:
                                                                                                                                        label1.place_forget()
                                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                                  
                                                                                                                        app=SE_ANG()
                                                                                                                else:
                                                                                                                        write_text+=1
                                                                                                                
                                                                                                if write_text>0:
                                                                                                        time.sleep(2)
                                                                                                
                                                                                                        ze_S_ENG.place_forget()
                                                                                                        Ent_speak.delete(0, 'end')
                                                                                                        Ent_speak.configure(background='white')
                                                                                                        Ent_speak.focus()
                                                                                                        speak_label["text"] =  "type the word"
                                                                                                        
                                                                                                        Ent_speak.bind('<Return>' ,chuc_speak )
                                                        except sr.WaitTimeoutError: 
                                                                tkinter.messagebox.showinfo("check the microphone" , "check the microphone and repeat the exercise ")
  
                                                                app=SE_ANG()

                                        Microphone_image = PhotoImage(file = 'Microphone.png')
                                        button_Microphone = Button(frame31 , image = Microphone_image , justify = "center" , command=speak_button)
                                        button_Microphone.place(relwidth = 0.11, relheight = 0.2 ,relx=0.45, rely = 0.16)
                                        button_Microphone.update()

                                        name = ','.join(uservalue[i][0])

                                        ze_S_ENG = Label(frame31 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,text = name )
                                        ze_S_ENG.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.05)
                
                                        Ent_speak = Entry(frame31 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,justify = "center"  )
 
                                        self.Master.mainloop()
                                        break
                
                                
                                else:
                                        print("słowa już nie ma w powtórce") 
                        except TypeError:
                                continue

                if licz_data <= 0 :
                        app6 = powtorki()    
            count_cwicz7 =0
            for i in range(len(uservalue)):
                date=(uservalue[i][4][6])
                try:
                        if date <= self.today:
                                count_cwicz7 +=1
                        
                except TypeError:
                        
                        continue
            English_P= Button(frame20 ,font = ('arial', 14 , 'bold')  , bd = 2   , justify = 'left', bg='#458B74' , 
            text= "Ćwiczenie 7  - Powiedz Angielskie znaczenie ze słuchu{:>65} Słówek".format(count_cwicz7)  , command = SE_ANG)
            if count_cwicz7 >=1 :
                English_P.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.71)

            def SE_ANG_W ():
                shuffle(uservalue)
                licz_data = 0
                for i in range(len(uservalue)):
                        date=uservalue[i][4][7]
                        try:

                                if date <= self.today:
                                        licz_data +=1
                                        
                                        frame31 = Frame(self.frame1 , bg = "#CCCC99")
                                        frame31.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
                                        def new_C():
                                                frame31.destroy()
                                                app=SE_ANG_W()
                                        def chuc_speak (event):
                                                Ent_speak.update()
                                                polword = Ent_speak.get()
                                             
                                                polword_split = []
                                                cor_Word = uservalue[i][0]
                      
                                                correct_word = 0
                                                for word1 in polword.split(','):
                                                        polword_split.append(word1.strip())
                                     
                                                for ind , word in enumerate(polword_split):
                                                        
                                                        for word3 in cor_Word:

                                                                if word.lower() == word3.lower():
                                                                        correct_word+=1
                                          
                                                        if correct_word>0 and  uservalue[i][3][7] < 9:
                                                                uservalue[i][4][7] = self.d
                                                                uservalue[i][3][7] +=1        
                                                                uservalue[i][2][7] +=1
                                                                userDane[5] += 1
                                                                userDane[7] += 1
                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                        
                                                                label1= Label(frame31 , bg = "yellow" , text = "+{}".format(1),   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                for x in range(3,8):
                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                        label1.update()
                                                                        time.sleep(0.1)
                                                                        if x >=7:
                                                                                label1.place_forget()
                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                             
                                                                app=SE_ANG_W()
                                                        elif correct_word >0 and  uservalue[i][3][7] >=9:
                                                                                      
                                                                uservalue[i][4][7] = "NAUCZONE"
                                                                uservalue[i][3][7] +=1
                                                                uservalue[i][2][7] +=1
                                                                userDane[5] += 10
                                                                userDane[7] += 10
                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                
                                                                label1= Label(frame31 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                for x in range(3,8):
                                                                        label1.place(relwidth = 0.04 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                        label1.update()
                                                                        time.sleep(0.1)
                                                                        if x >=7:
                                                                                label1.place_forget()
                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                   
                                                                app=SE_ANG()
                                                        else:
                                                         
                                                                name = ','.join(uservalue[i][0])
                                                                BTN_speak = Button(frame31 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,justify = "center" ,
                                                                text=name , bg="red", command =new_C )
                                                                BTN_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.7)

                                        def speak_button():
                                                cor_Word = uservalue[i][0]
                                                button_Microphone.place_forget()
                                                write_text = 0
                
                                                r= sr.Recognizer()
                                                with sr.Microphone() as source:

                                                        audio=r.adjust_for_ambient_noise(source)
                                                        speak_label = Label(frame31 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,text = "Say the sentences or word and wait. Don't repeat the word")
                                                        speak_label.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.4)
                                                        speak_label.update()
                                                        try:
                                                                audio =r.listen(source, timeout = 10)
                        
                                                                try:
                                                                        text = r.recognize_google(audio , language="en-US")
                                                                
                                                                        Ent_speak.insert("end" ,"{}" .format(text))
                                                                        Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                        Ent_speak.update()
                                                                        
                                                                except:
                                                                
                                                                        speak_label["text"] =  "could you repeat "
                                                                        speak_label.update()
                                                                        time.sleep(0.5)
                                                                        
                                                                        with sr.Microphone() as source:
                                                                        
                                                                                audio=r.adjust_for_ambient_noise(source)
                                                                                audio =r.listen(source)
                                                                        
                                                                                try:
                                                                                        text = r.recognize_google(audio , language="en-US")
                                                                                
                                                                                        Ent_speak.insert("end" ,"{}" .format(text))
                                                                                        Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                                        Ent_speak.update()
                                                                                except:
                                                                                        write_text+=1

                                                                if UnboundLocalError == True or write_text == 1:
                                                                
                                                                        time.sleep(2)
                                                                        ze_S_ENG.place_forget()
                                                                        Ent_speak.delete(0, 'end')
                                                                        Ent_speak.configure(background='white')
                                                                        Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                        Ent_speak.focus()
                                                                        speak_label["text"] =  "type the word"
                                                                                        
                                                                        Ent_speak.bind('<Return>' ,chuc_speak )
                                                                else:
                        
                                                                        if len(cor_Word)>=2:
                                                                                        correct_word=0
                        
                                                                                        for word in cor_Word:
                        
                                                                                                if text.lower() == word.lower():
                                                                                                
                                                                                                        correct_word+=1
                                                                                                
                                                                                        
                                                                                        if correct_word >0 and  uservalue[i][3][7] <= 5:
                                                                                        
                                                                                                uservalue[i][4][7] = self.d
                                                                                                uservalue[i][3][7] +=1
                                                                                                uservalue[i][2][7] +=1
                                                                                                userDane[5] += 1
                                                                                                userDane[7] += 1
                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                        
                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                for x in range(3,8):
                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                        label1.update()
                                                                                                        time.sleep(0.1)
                                                                                                        if x >=7:
                                                                                                                label1.place_forget()
                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                         
                                                                                                app=SE_ANG_W()
                                                                                        elif correct_word >0 and  7>=uservalue[i][3][7] > 5:
                                                                                        
                                                                                                uservalue[i][4][7] = self.d1
                                                                                                uservalue[i][3][7] +=1
                                                                                                uservalue[i][2][7] +=1
                                                                                                userDane[5] += 1
                                                                                                userDane[7] += 1
                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                        
                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                for x in range(3,8):
                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                        label1.update()
                                                                                                        time.sleep(0.1)
                                                                                                        if x >=7:
                                                                                                                label1.place_forget()
                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                        
                                                                                                app=SE_ANG_W()
                                                                                        elif correct_word >0 and  9>uservalue[i][3][7] > 7:
                                                                                        
                                                                                                uservalue[i][4][7] = self.d2
                                                                                                uservalue[i][3][7] +=1
                                                                                                uservalue[i][2][7] +=1
                                                                                                userDane[5] += 2
                                                                                                userDane[7] += 2
                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                        
                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                        
                                                        
                                                                                                for x in range(3,8):
                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                        label1.update()
                                                                                                        time.sleep(0.1)
                                                                                                        if x >=7:
                                                                                                                label1.place_forget()
                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                         
                                                                                                app=SE_ANG_W()
                                                                                        elif correct_word >0 and  uservalue[i][3][7] >=9:
                                                                                        
                                                                                                uservalue[i][4][7] = "NAUCZONE"
                                                                                                uservalue[i][3][7] +=1
                                                                                                uservalue[i][2][7] +=1
                                                                                                userDane[5] += 10
                                                                                                userDane[7] += 10
                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                        
                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                        
                                                        
                                                                                                for x in range(3,8):
                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                        label1.update()
                                                                                                        time.sleep(0.1)
                                                                                                        if x >=7:
                                                                                                                label1.place_forget()
                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                          
                                                                                                app=SE_ANG_W()

                                                                                        else:

                                                                                                Ent_speak.configure(background='red')
                                                                                                
                                                                                                Ent_speak.insert("end" ,"{}" .format(text))
                                                                                                Ent_speak.update()
                                                                                                time.sleep(0.5)
                                                                                                
                                
                                                                                                with sr.Microphone() as source:
                                                                                                        
                                                                                                        
                                                                                                        audio=r.adjust_for_ambient_noise(source)
                                                                                                        speak_label["text"] =  "Wrong word could you repeat"
                                                                                                        speak_label.update()
                                                                                                
                                                                                                        audio =r.listen(source)
                        
                                                                                                        try:
                                                                                                                text = r.recognize_google(audio , language="en-US")
                                                                                                                
                                                                                                                Ent_speak.delete(0, 'end')
                                                                                                                Ent_speak.insert("end" ,"{}" .format(text))
                                                                                                                
                                                                                                                Ent_speak.update()
                                                                                                        except:

                                                                                                                with sr.Microphone() as source:
                                                                                                                        
                                                                                                                        audio=r.adjust_for_ambient_noise(source)
                                                                                                                        speak_label["text"] =  "could you repeat "
                                                                                                                        speak_label.update()
                                                                                                                
                                                                                                                        audio =r.listen(source)
                        
                                                                                                                        try:
                                                                                                                                text = r.recognize_google(audio , language="en-US")
                                                                                                                                Ent_speak.insert("end" ,"{}" .format(text))
                                                                                                                        
                                                                                                                                Ent_speak.update()
                                                                                                                        except:
                                                                                                                                write_text+=1
                                                                                                                        
                                                                                                if UnboundLocalError == True or write_text == 1:
                                                                                                        time.sleep(2)
                                                                                                        ze_S_ENG.place_forget()
                                                                                                        Ent_speak.delete(0, 'end')
                                                                                                        Ent_speak.configure(background='white')
                                                                                                        Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                                                        Ent_speak.focus()
                                                                                                        speak_label["text"] =  "type the word"
                                                                                                        
                                                                                                        Ent_speak.bind('<Return>' ,chuc_speak )
                                                                                                else:
                                                                                                        correct_word=0
                                                                                                        for word in cor_Word:
                        
                                                                                                                if text.lower() == word.lower():
                                                                                                                
                                                                                                                        correct_word+=1
                                                                                                                
                                                                                                        if correct_word >0 and  uservalue[i][3][7] <= 5:
                                                                                                        
                                                                                                                uservalue[i][4][7] = self.d
                                                                                                                uservalue[i][3][7] +=1
                                                                                                                uservalue[i][2][7] +=1
                                                                                                                userDane[5] += 1
                                                                                                                userDane[7] += 1
                                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                        
                                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                                                
                                                                                                
                                                                                                                for x in range(3,8):
                                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                        label1.update()
                                                                                                                        time.sleep(0.1)
                                                                                                                        if x >=7:
                                                                                                                                label1.place_forget()
                                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                         
                                                                                                                app=SE_ANG_W()
                                                                                                        elif correct_word >0 and  7>=uservalue[i][3][7] > 5:
                                                                                                        
                                                                                                                uservalue[i][4][7] = self.d1
                                                                                                                uservalue[i][3][7] +=1
                                                                                                                uservalue[i][2][7] +=1
                                                                                                                userDane[5] += 1
                                                                                                                userDane[7] += 1
                                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                        
                                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )

                                                                                                                for x in range(3,8):
                                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                        label1.update()
                                                                                                                        time.sleep(0.1)
                                                                                                                        if x >=7:
                                                                                                                                label1.place_forget()
                                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                        
                                                                                                                app=SE_ANG_W()
                                                                                                        elif correct_word >0 and  9>uservalue[i][3][7] > 7:
                                                                                                                
                                                                                                                uservalue[i][4][7] = self.d2
                                                                                                                uservalue[i][3][7] +=1
                                                                                                                uservalue[i][2][7] +=1
                                                                                                                userDane[5] += 2
                                                                                                                userDane[7] += 2
                                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                        
                                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                                        
                                                                                        
                                                                                                                for x in range(3,8):
                                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                        label1.update()
                                                                                                                        time.sleep(0.1)
                                                                                                                        if x >=7:
                                                                                                                                label1.place_forget()
                                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                         
                                                                                                                app=SE_ANG_W()
                                                                                                        elif correct_word >0 and  uservalue[i][3][7] >=9:
                                                                                                        
                                                                                                                uservalue[i][4][7] = "NAUCZONE"
                                                                                                                uservalue[i][3][7] +=1
                                                                                                                uservalue[i][2][7] +=1
                                                                                                                userDane[5] += 10
                                                                                                                userDane[7] += 10
                                                                                                                self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                        
                                                                                                                label1= Label(frame31 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                                        
                                                                                        
                                                                                                                for x in range(3,8):
                                                                                                                        label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                        label1.update()
                                                                                                                        time.sleep(0.1)
                                                                                                                        if x >=7:
                                                                                                                                label1.place_forget()
                                                                                                                pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                          
                                                                                                                app=SE_ANG_W()
                                                                                                        else:
                                                                                                                write_text+=1
                                                                                                                
                                                                                        if write_text>0:
                                                                                                time.sleep(1)
                                                                                        
                                                                                                ze_S_ENG.place_forget()
                                                                                                Ent_speak.configure(background='white')
                                                                                                
                                                                                                speak_label["text"] =  "type the word"
                                                                                                
                                                                                                Ent_speak.bind('<Return>' ,chuc_speak )
                        
                                                                        else:
                                                                                if UnboundLocalError == True or write_text == 1:
                                                                                
                                                                                        time.sleep(2)
                                                                                
                                                                                        ze_S_ENG.place_forget()
                                                                                        Ent_speak.delete(0, 'end')
                                                                                        Ent_speak.configure(background='white')
                                                                                        Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                                        Ent_speak.focus()
                                                                                        speak_label["text"] =  "type the word"
                                                                                                
                                                                                        Ent_speak.bind('<Return>' ,chuc_speak )
                                                                                else:
                                                                                        for word in cor_Word:
                                                                                                
                                                                                                if text.lower() == word.lower() and  uservalue[i][3][7] <= 5:
                                                                                                
                                                                                                        uservalue[i][4][7] = self.d
                                                                                                        uservalue[i][3][7] +=1
                                                                                                        uservalue[i][2][7] +=1
                                                                                                        userDane[5] += 1
                                                                                                        userDane[7] += 1
                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                        
                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                                
                                                                                
                                                                                                        for x in range(3,8):
                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                label1.update()
                                                                                                                time.sleep(0.1)
                                                                                                                if x >=7:
                                                                                                                        label1.place_forget()
                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                          
                                                                                                        app=SE_ANG_W()
                                                                                                elif text.lower() == word.lower() and  7>=uservalue[i][3][7] > 5:
                                                                                                
                                                                                                        uservalue[i][4][7] = self.d1
                                                                                                        uservalue[i][3][7] +=1
                                                                                                        uservalue[i][2][7] +=1
                                                                                                        userDane[5] += 1
                                                                                                        userDane[7] += 1
                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                        
                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                        
                                                                        
                                                                                                        for x in range(3,8):
                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                label1.update()
                                                                                                                time.sleep(0.1)
                                                                                                                if x >=7:
                                                                                                                        label1.place_forget()
                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                          
                                                                                                        app=SE_ANG_W()
                                                                                                elif text.lower() == word.lower() and  9>uservalue[i][3][7] > 7:
                                                                                                
                                                                                                        uservalue[i][4][7] = self.d2
                                                                                                        uservalue[i][3][7] +=1
                                                                                                        uservalue[i][2][7] +=1
                                                                                                        userDane[5] += 2
                                                                                                        userDane[7] += 2
                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                        
                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                        
                                                                        
                                                                                                        for x in range(3,8):
                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                label1.update()
                                                                                                                time.sleep(0.1)
                                                                                                                if x >=7:
                                                                                                                        label1.place_forget()
                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                           
                                                                                                        app=SE_ANG_W()
                                                                                                elif text.lower() == word.lower() and  uservalue[i][3][7] >=9:
                                                                                                
                                                                                                        uservalue[i][4][7] = "NAUCZONE"
                                                                                                        uservalue[i][3][7] +=1
                                                                                                        uservalue[i][2][7] +=1
                                                                                                        userDane[5] += 10
                                                                                                        userDane[7] += 10
                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                        
                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                        
                                                                        
                                                                                                        for x in range(3,8):
                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                label1.update()
                                                                                                                time.sleep(0.1)
                                                                                                                if x >=7:
                                                                                                                        label1.place_forget()
                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                          
                                                                                                        app=SE_ANG_W()
                                                                                                        
                                                                                                else:

                                                                                                        Ent_speak.configure(background='red')
                                                                                                        Ent_speak.update()

                                                                                                        with sr.Microphone() as source:

                                                                                                                audio=r.adjust_for_ambient_noise(source)
                                                                                                                speak_label["text"] =  "wrong word could you repeat"
                                                                                                                speak_label.update()
                                                                                                                audio =r.listen(source)
                                                                                                                try:
                                                                                                                        text = r.recognize_google(audio , language="en-US")
                                                                                                                
                                                                                                                        Ent_speak.delete(0, 'end')
                                                                                                                        Ent_speak.insert("end" ,"{}" .format(text))
                                                                                                                        Ent_speak.update()
                                                                                                                        
                                                                                                                except:
                                                                                                                        with sr.Microphone() as source:
                                                                                                                                
                                                                                                                                audio=r.adjust_for_ambient_noise(source)
                                                                                                                                speak_label["text"] =  "could you repeat "
                                                                                                                                speak_label.update()
                                                                                                                        
                                                                                                                                audio =r.listen(source)
                        
                                                                                                                        
                                                                                                                                try:
                                                                                                                                        text = r.recognize_google(audio , language="en-US")
                                                                                                                                
                                                                                                                                        Ent_speak.insert("end" ,"{}" .format(text))
                                                                                                                                
                                                                                                                                        Ent_speak.update()
                                                                                                                                except:
                                                                                                                                        write_text+=1
                                                                                                                                
                                                                                                        if UnboundLocalError == True  or write_text == 1:
                                                                                                        
                                                                                                                time.sleep(2)
                                                                                                        
                                                                                                                ze_S_ENG.place_forget()
                                                                                                                Ent_speak.delete(0, 'end')
                                                                                                                Ent_speak.configure(background='white')
                                                                                                                Ent_speak.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.55)
                                                                                                                Ent_speak.focus()
                                                                                                                speak_label["text"] =  "type the word"
                                                                                                                
                                                                                                                Ent_speak.bind('<Return>' ,chuc_speak )
                                                                                                        else:
                                                                                                                correct_word = 0
                                                                                                                for word in cor_Word:
                                                                                                                        
                                                                                                                        if text.lower() == word.lower():
                                                                                                                        
                                                                                                                                correct_word+=1
                                                                                                                        
                                                                                                                if correct_word >0 and  uservalue[i][3][7] <= 5:
                                                                                                                
                                                                                                                        uservalue[i][4][7] = self.d
                                                                                                                        uservalue[i][3][7] +=1
                                                                                                                        uservalue[i][2][7] +=1
                                                                                                                        userDane[5] += 1
                                                                                                                        userDane[7] += 1
                                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                                
                                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                                                        
                                                                                                        
                                                                                                                        for x in range(3,8):
                                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                                label1.update()
                                                                                                                                time.sleep(0.1)
                                                                                                                                if x >=7:
                                                                                                                                        label1.place_forget()
                                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
 
                                                                                                                        app=SE_ANG_W()
                                                                                                                elif correct_word >0 and  7>=uservalue[i][3][7] > 5:
                                                                                                                
                                                                                                                        uservalue[i][4][7] = self.d1
                                                                                                                        uservalue[i][3][7] +=1
                                                                                                                        uservalue[i][2][7] +=1
                                                                                                                        userDane[5] += 1
                                                                                                                        userDane[7] += 1
                                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                                
                                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+1",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                                                
                                                                                                
                                                                                                                        for x in range(3,8):
                                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                                label1.update()
                                                                                                                                time.sleep(0.1)
                                                                                                                                if x >=7:
                                                                                                                                        label1.place_forget()
                                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                                   
                                                                                                                        app=SE_ANG_W()
                                                                                                                elif correct_word >0 and  9>uservalue[i][3][7] > 7:
                                                                                                                
                                                                                                                        uservalue[i][4][7] = self.d2
                                                                                                                        uservalue[i][3][7] +=1
                                                                                                                        uservalue[i][2][7] +=1
                                                                                                                        userDane[5] += 2
                                                                                                                        userDane[7] += 2
                                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                                
                                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+2",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                                                
                                                                                                
                                                                                                                        for x in range(3,8):
                                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                                label1.update()
                                                                                                                                time.sleep(0.1)
                                                                                                                                if x >=7:
                                                                                                                                        label1.place_forget()
                                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                                  
                                                                                                                        app=SE_ANG_W()
                                                                                                                elif correct_word >0 and  uservalue[i][3][7] >=9:
                                                                                                                
                                                                                                                        uservalue[i][4][7] = "NAUCZONE"
                                                                                                                        uservalue[i][3][7] +=1
                                                                                                                        uservalue[i][2][7] +=1
                                                                                                                        userDane[5] += 10
                                                                                                                        userDane[7] += 10
                                                                                                                        self.Liczba_punktow_today.config(text = "liczba punktów dzisiaj :{}".format(userDane[7]) )
                                                                                                                        self.calkowita_liczba_punktow.config( text = "liczba punktów  :{}".format(userDane[5]))
                                                                                                                                
                                                                                                                        label1= Label(frame31 , bg = "yellow" , text = "+10",   font = ('arial' , 20 , 'bold') , bd = 4 )
                                                                                                
                                                                                                
                                                                                                                        for x in range(3,8):
                                                                                                                                label1.place(relwidth = 0.02 , relheight = 0.02 ,relx=x/10 , rely=x/10)
                                                                                                                                label1.update()
                                                                                                                                time.sleep(0.1)
                                                                                                                                if x >=7:
                                                                                                                                        label1.place_forget()
                                                                                                                        pickle.dump(USERDANE , open("USERDANE.py" , "wb"))
                                                                                                                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                                                                                                                                   
                                                                                                                        app=SE_ANG_W()
                                                                                                                else:
                                                                                                                        write_text+=1
                                                                                                                
                                                                                                if write_text>0:
                                                                                                        time.sleep(2)
                                                                                                        ze_S_ENG.place_forget()
                                                                                                        Ent_speak.delete(0, 'end')
                                                                                                        Ent_speak.configure(background='white')
                                                                                                        Ent_speak.focus()
                                                                                                        speak_label["text"] =  "type the word"
                                                                                                        
                                                                                                        Ent_speak.bind('<Return>' ,chuc_speak )
                                                        
                                                        except sr.WaitTimeoutError: 
                                                                tkinter.messagebox.showinfo("check the microphone" , "check the microphone and repeat the exercise ")  
                                                                app=SE_ANG()       

                                        Microphone_image = PhotoImage(file = 'Microphone.png')
                                        button_Microphone = Button(frame31 , image = Microphone_image , justify = "center" , command=speak_button)
                                        button_Microphone.place(relwidth = 0.11, relheight = 0.2 ,relx=0.45, rely = 0.16)
                                        button_Microphone.update()
           
                                        name = ','.join(uservalue[i][1])
              
                                        ze_S_ENG = Label(frame31 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,text = name )
                                        ze_S_ENG.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.05)
                
                                        Ent_speak = Entry(frame31 ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,justify = "center"  )
               
                                        self.Master.mainloop()
                                        break
                               
                                else:
                                        print("słowa już nie ma w powtórce") 
                        except TypeError:
                                continue

                if licz_data <= 0 :
                        app4 = powtorki() 
            count_cwicz8 =0
            for i in range(len(uservalue)):
                date=(uservalue[i][4][7])
                try:
                        if date <= self.today:
                                count_cwicz8 +=1
                        
                except TypeError:
                        
                        continue
                
            Polish_P= Button(frame20 ,font = ('arial', 14 , 'bold')  , bd = 2   , justify = 'left', bg='#458B74' ,
             text= "Ćwiczenie 8  - Powiedz Angielskie znaczenie ze słuchu{:>65} Słówek".format(count_cwicz8) ,command = SE_ANG_W)
            if count_cwicz8 >=1 :
                Polish_P.place(relwidth = 0.9 , relheight = 0.1 ,relx=0.05 , rely = 0.82)

        self.powtorki = Button(self.frame2 , text='POWTÓRKI' , width=13, bg='#458B74' , font = ('arial' , 19 , 'bold'), bd=3 , justify = 'center',command = powtorki)
        self.powtorki.place(relwidth =1 , relheight = 0.07 , relx =0.08 , rely = 0.05)
#=======================================LISTA====================================================================================
        def Lista():
            USERWARD = pickle.load(open("USERWARD.py" , "rb"))
            uservalue = USERWARD[self.User]
            frame5 = Frame(self.frame1 , bg = 'white')
            frame5.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
            tree_columns = ("English ward", "Polisch ward", "liczba \n Wyświetleń" , " poprawne \n odpowiedzi"  , "Data powtórki")
            k=0
            new_entries = []
            polish_ward = []
            liczba_wyswietlen = []
            liczba_poprawnych = []
            data_dodania = []

            def sort( element):
                return element[0]
            def sort_pol ( element):
                return element[1]
            def sort_liczba_WY (element):
                return element[2]
            def sort_liczba_PO (element):
                return element[3]
            def sort_liczba_DATA (element):
                return element[4]

            def save_list (event):
                date = datetime.date.today()
                for indx, entry in enumerate(new_entries)  :
                    englishword = new_entries[indx].get() 
                    polishword = polish_ward[indx].get()

                    if  englishword.split(',')  == uservalue[indx][0] and  polishword.split(',')  == uservalue[indx][1] :
                        new_entries[indx].configure( state = 'disabled' )
                        polish_ward[indx].configure( state = 'disabled' )
                    else:
                        english = new_entries[indx].get()
                        english_strip =[]
                
                        for word in english.split(','):
                            english_strip.append(word.strip())
                        
                        polish_strip =[]
                        polish = polish_ward[indx].get()
                
                        for word1 in polish.split(','):
                            polish_strip.append(word1.strip())

                
                        uservalue[indx]=[english_strip, polish_strip, [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [ date, date, date, date, date, date, date, date] ]
                        new_entries[indx].configure( state = 'disabled' )
                        polish_ward[indx].configure( state = 'disabled' )

                USERWARD[self.User]=uservalue
                pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
            def find_word ():
 
                root = Toplevel()
                root.title("FIND")
                root.resizable( width = False , height= False)
                root.geometry ('1100x450+0+0')

                frame = Frame(root , bg= "#E0EEEE")
                frame.place(relwidth = 1 , relheight = 1)
                lab_eng = Label(frame ,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' ,bg='#458B74', justify = 'center', text = "Write word in english" )
                lab_eng.place(relwidth = 0.43 , relheight = 0.1 ,relx=0.05 , rely = 0.15)

                txt_ent= Entry(frame,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , justify = 'center')
                txt_ent.configure (state = 'normal')
                txt_ent.place(relwidth = 0.44 , relheight = 0.1 ,relx=0.05 , rely = 0.30)
                
                txt_ent.focus()
                txt_pol= Entry(frame,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , justify = 'center')
                txt_pol.configure (state = 'disable')
                txt_pol.place(relwidth = 0.44 , relheight = 0.1 ,relx=0.49 , rely = 0.30)
                def Del():
                       
                        englishward = txt_ent.get()
                        englishword_strip =[]
                                        
                        for word in englishward.split(','):
                                englishword_strip.append(word.strip())
                        licz = 0
                        for indx, entry in enumerate(uservalue):
                                
                                for k in range(0, len(englishword_strip)):

                                        if englishword_strip[k] in entry[0]:

                                                uservalue.remove(entry)
                                                pickle.dump(USERWARD , open("USERWARD.py" , "wb")) 
                                                txt_ent.config(state= "normal")
                                                txt_ent.delete(0, 'end')
                                                self.find_liczbe =0
                                                txt_pol.config(state= "normal")
                                                txt_pol.delete(0, 'end')
                                                frame5.destroy()
                                                app_lista = Lista()
                                                licz +=1
                                                break
                        if licz <=0 :
                            
                                txt_ent.config(state= "normal")
                                txt_ent.delete(0, 'end')
                                self.find_liczbe =0
                                txt_pol.config(state= "normal")
                                txt_pol.delete(0, 'end')
                                tkinter.messagebox.showinfo("NO WORD" , "The word does not appear")
                               

                but_DEL = Button(frame,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , justify = 'center' , text ="DELETE" ,command = Del)
                but_DEL.place(relwidth = 0.18 , relheight = 0.1 ,relx=0.77 , rely = 0.15)

                def find ():
                    txt_ent.config(state= "normal")
                    eng_word =  txt_ent.get()

                    if self.find_liczbe >0 :
                        txt_ent.config(state= "normal")
                        txt_ent.delete(0, 'end')
                        txt_pol.config(state= "normal")
                        txt_pol.delete(0, 'end')
                        txt_pol.config(state= "disable")

                        self.find_liczbe =0
                    else:   

                        licz = 0
                        for i in range(0 , len(uservalue)):

                            if eng_word in uservalue[i][0]:
                                word0= ','.join(uservalue[i][0])
                                word1= ','.join(uservalue[i][1])
                                txt_ent.delete(0, 'end')
                                txt_ent.insert(0,word0)
                                txt_ent.config(state= "disable")
                                txt_pol.config(state= "normal")
                                txt_pol.insert(0,word1)
                                txt_pol.config(state= "disable")
                                self.find_liczbe +=1
                                self.liczba_wys = i

                                licz +=1
                                break
                        if licz <=0 :
                            txt_ent.delete(0, 'end')
                            find_liczbe = 0
                            tkinter.messagebox.showinfo("NO WORD" , "The word does not appear")

                but_1 = Button(frame,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , justify = 'center' , text ="FIND" , command = find)
                but_1.place(relwidth = 0.18 , relheight = 0.1 ,relx=0.05 , rely = 0.70)

                def edit():
                    txt_ent.config(state= "normal")
                        
                    txt_pol.config(state= "normal")

                but_2 = Button(frame,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , justify = 'center' , text ="EDIT" , command =edit)
                but_2.place(relwidth = 0.18 , relheight = 0.1 ,relx=0.23 , rely = 0.70)

                def learned():
                    uservalue[self.liczba_wys][4] = ["NAUCZONE","NAUCZONE","NAUCZONE","NAUCZONE","NAUCZONE","NAUCZONE","NAUCZONE","NAUCZONE"]
                    tkinter.messagebox.showinfo("Word is Learned" , "The word is learned")

                but_3 = Button(frame,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , justify = 'center' , text ="LEARNED" , command = learned)
                but_3.place(relwidth = 0.18 , relheight = 0.1 ,relx=0.41 , rely = 0.70)

                def repeat():
                    date = datetime.date.today()
                    uservalue[self.liczba_wys][4] = [date,date,date,date,date,date,date,date]
                    tkinter.messagebox.showinfo("Word to repeat" , "you have to repeat this word")

                but_4 = Button(frame,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , justify = 'center' , text ="REPEAT" , command = repeat)
                but_4.place(relwidth = 0.18 , relheight = 0.1 ,relx=0.59 , rely = 0.70)
                def save():
                    englishward = txt_ent.get()
                    englishword_strip =[]
                                
                    for word in englishward.split(','):
                        englishword_strip.append(word.strip())
                    polishward = txt_pol.get()
                    polishward_strip=[]
                    for word1 in polishward.split(','):
                        polishward_strip.append(word1.strip())

                    if self.liczba_wys > 0 :
                        uservalue[self.liczba_wys][0] = englishword_strip
                        uservalue[self.liczba_wys][1] = polishward_strip
                        pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                        txt_ent.config(state= "normal")
                        txt_pol.config(state= "normal")
                        txt_ent.delete(0, 'end')
                        txt_pol.delete(0 , 'end')
                        txt_pol.config(state= "disable")
                    else:
                        tkinter.messagebox.showinfo("Find Word" , "you should find word")

                but_5 = Button(frame,font = ('arial' , 22 , 'bold') , bd=2 , relief='ridge' , justify = 'center' , text ="SAVE" , command = save)
                but_5.place(relwidth = 0.18 , relheight = 0.1 ,relx=0.77 , rely = 0.70)

                #======================================================FIND WORD===================================================
            btn_find = Button(frame5 , font = ('arial', 14 , 'bold')  , bd = 3 , text = "Find word" , command = find_word)
            btn_find. place(relx=0.90 , rely = 0.94)
            frame21 = Frame(frame5 , bg="white")
            frame21.place(relwidth = 0.3 , relheight = 0.85,rely = 0.05 ,relx=0.1)
            

            frame31 = Frame(frame5 , bg="white")
            frame31.place(relwidth = 0.3 , relheight = 0.85 , relx=0.4,rely = 0.05)

            frame41 = Frame(frame5 , bg="white")
            frame41.place(relwidth = 0.07 , relheight = 0.85 , relx=0.7,rely = 0.05)

            frame51 = Frame(frame5 , bg="white")
            frame51.place(relwidth = 0.07 , relheight = 0.85 , relx=0.77,rely = 0.05)

            frame61 = Frame(frame5 , bg="white")
            frame61.place(relwidth = 0.10 , relheight = 0.85 , relx=0.84,rely = 0.05)
            frame71 = Frame(frame5 , bg = "white")
            frame81 = Frame(frame5 , bg="white")
            frame81.place(relwidth = 0.7 , relheight = 0.7 , relx=0.15,rely = 0.92)

            def n_Button(m):
                
                if m == 0 :
                    for widget in frame21.winfo_children():
                        widget.grid_forget()
                    for widget in frame31.winfo_children():
                        widget.grid_forget()
                    for widget in frame41.winfo_children():
                        widget.grid_forget()
                    for widget in frame51.winfo_children():
                        widget.grid_forget()
                    for widget in frame61.winfo_children():
                        widget.grid_forget()
                
                        
                    for  i in range(0,30):
                        new_entries[i].grid(row = i , column =0, ipadx =5)
                        polish_ward[i].grid(row=i , column =0 , ipadx =0)
                        liczba_wyswietlen[i].grid(row=i , column =0 , ipadx =0)
                        liczba_poprawnych[i].grid(row=i , column =0 , ipadx =0)
                        data_dodania[i].grid(row=i , column =0 , ipadx =0)
                        
                        
                elif m >0 and len(new_entries)-m*30 <30:
                    for widget in frame21.winfo_children():
                        widget.grid_forget()
                    for widget in frame31.winfo_children():
                        widget.grid_forget()
                    for widget in frame41.winfo_children():
                        widget.grid_forget()
                    for widget in frame51.winfo_children():
                        widget.grid_forget()
                    for widget in frame61.winfo_children():
                        widget.grid_forget()
                        
                    for  i in range(0 , len(new_entries)-m*30):
                        
                        new_entries[i+m*30].grid(row = i , column =0, ipadx =0)
                        polish_ward[i+m*30].grid(row=i , column =0 , ipadx =0)
                        liczba_wyswietlen[i+m*30].grid(row=i , column =0 , ipadx =0)
                        liczba_poprawnych[i+m*30].grid(row=i , column =0 , ipadx =0)
                        data_dodania[i+m*30].grid(row=i , column =0 , ipadx =0)

                elif m >0 and len(new_entries)-m*30 >=30:
                    for widget in frame21.winfo_children():
                        widget.grid_forget()
                    for widget in frame31.winfo_children():
                        widget.grid_forget()
                    for widget in frame41.winfo_children():
                        widget.grid_forget()
                    for widget in frame51.winfo_children():
                        widget.grid_forget()
                    for widget in frame61.winfo_children():
                        widget.grid_forget()
                        
                    for  i in range(0 , 30):
                        
                        new_entries[i+m*30].grid(row = i , column =0, ipadx =0)
                        polish_ward[i+m*30].grid(row=i , column =0 , ipadx =0)
                        liczba_wyswietlen[i+m*30].grid(row=i , column =0 , ipadx =0)
                        liczba_poprawnych[i+m*30].grid(row=i , column =0 , ipadx =0)
                        data_dodania[i+m*30].grid(row=i , column =0 , ipadx =0)

            def editEntry(event):
                        
                        for ind  , entr2 in enumerate(polish_ward):
                                if event.widget == entr2  :
                                                new_entries[ind].configure( state = 'normal')
                                                polish_ward[ind].configure( state = 'normal')
                                                polish_ward[ind].bind('<Return>', save_list)
                        for indx, entry in enumerate(new_entries)  :
                                        if event.widget == entry  :
                                                new_entries[indx].configure( state = 'normal')
                                                polish_ward[indx].configure( state = 'normal') 
                                                new_entries[indx].bind('<Return>', save_list)
            n=1+int(len(uservalue)/30)
            btn=[]
            g=0
            for m in range(0,n): 
                btn.append(Button(frame81 , font = ('arial', 14 , 'bold')  , bd = 2  , text = m ))
                btn[g].grid(row = 0 , column = g)
                btn[g]["command"] = lambda x = m : n_Button(x)
                g+=1

            for  i in range(0,len(uservalue)):
                
                word0= ','.join(uservalue[i][0])
                word1= ','.join(uservalue[i][1])

                new_entries.append( Entry(frame21 ,font = ('arial', 12 , 'bold')  , bd = 2   , justify = 'left' , width = 38))
        
                new_entries[k].insert("end",word0)
                
                new_entries[k].configure( state = 'disabled' )
        
                new_entries[k].bind( "<Double-Button> "  , editEntry)

                polish_ward.append( Entry(frame31 ,font = ('arial', 12 , 'bold')  , bd = 2   , justify = 'left' , width = 38))
        
        
                polish_ward[k].insert("end",word1)
                
                polish_ward[k].configure( state = 'disabled' )
        
                polish_ward[k].bind( "<Double-Button> "  , editEntry)

                liczba_wyswietlen.append(Entry(frame41 ,font = ('arial', 12 , 'bold')  , bd = 2   , justify = 'center' , width = 8))
                liczba_wyswietlen[k].insert("end",int(sum(uservalue[i][2])/len(uservalue[i][2])))
                liczba_wyswietlen[k].configure( state = 'disabled' )

                liczba_poprawnych.append(Entry(frame51 ,font = ('arial', 12 , 'bold')  , bd = 2   , justify = 'center' , width = 8))
                liczba_poprawnych[k].insert("end",int(sum(uservalue[i][3])/len(uservalue[i][3])))
                liczba_poprawnych[k].configure( state = 'disabled' )

                data_dodania.append(Entry(frame61 ,font = ('arial', 12 , 'bold')  , bd = 2   , justify = 'center' , width = 13))
                if  uservalue[i][4].count('NAUCZONE') > 0:
                        
                        DATA_POP = uservalue[i][4]
                        g =list(filter(("NAUCZONE").__ne__, DATA_POP))
                        data_dodania[k].insert("end",min(g))
                else:
                        
                        data_dodania[k].insert("end",min(uservalue[i][4]))
                data_dodania[k].configure( state = 'disabled' )

                k+=1
            if len(uservalue)< 30:
                    for indx, entry in enumerate(new_entries):
                            new_entries[indx].grid(row = indx , column =0 , ipadx =0)
                    for ind  , entr2 in enumerate(polish_ward):
                            polish_ward[ind].grid(row=ind , column =0 , ipadx =0 )
                    for indl  , entrl in enumerate(liczba_wyswietlen):
                            liczba_wyswietlen[indl].grid(row=indl , column =0 , ipadx =0 )
                    for indp  , entrp in enumerate(liczba_poprawnych):
                            liczba_poprawnych[indp].grid(row=indp , column =0 , ipadx =0 )
                    for indd  , entrd in enumerate(data_dodania):
                            data_dodania[indd].grid(row=indd , column =0 , ipadx =0 )
            if len(uservalue)> 30:
                    for  i in range(0,30):
                        new_entries[i].grid(row = i , column =0, ipadx =5)
                        polish_ward[i].grid(row=i , column =0 , ipadx =0)
                        liczba_wyswietlen[i].grid(row=i , column =0 , ipadx =0)
                        liczba_poprawnych[i].grid(row=i , column =0 , ipadx =0)
                        data_dodania[i].grid(row=i , column =0 , ipadx =0)

           
            def cos(event):
    
                    for it in str(event.num):

                        if it == "1" :
                            self.numer += 1

                        if self.numer%2 == 0:
                            uservalue.sort(key=sort , reverse = True)
                        else:
                            uservalue.sort(key=sort)

                        for indx, entry in enumerate(new_entries)  :
                 
                                new_entries[indx].configure( state = 'normal')
                                polish_ward[indx].configure( state = 'normal')
                                liczba_wyswietlen[indx].configure( state = 'normal')
                                liczba_poprawnych[indx].configure( state = 'normal')
                                data_dodania[indx].configure( state = 'normal')

                                new_entries[indx].delete(0, 'end')
                                polish_ward[indx].delete(0, 'end')
                                liczba_wyswietlen[indx].delete(0, 'end')
                                liczba_poprawnych[indx].delete(0, 'end')
                                data_dodania[indx].delete(0, 'end')
                                word= ','.join(uservalue[indx][0])
                                word1= ','.join(uservalue[indx][1])
                                    
                                new_entries[indx].insert("end",word)
                               
                                polish_ward[indx].insert("end",word1)
                                liczba_wyswietlen[indx].insert("end",int(sum(uservalue[i][2])/len(uservalue[i][2])))
                                liczba_poprawnych[indx].insert("end",int(sum(uservalue[i][3])/len(uservalue[i][3])))
                                if  uservalue[i][4].count('NAUCZONE') > 0:
                        
                                        DATA_POP = uservalue[i][4]
                                        g =list(filter(("NAUCZONE").__ne__, DATA_POP))
                                        data_dodania[indx].insert("end",min(g))
                                else:
                                        
                                        data_dodania[indx].insert("end",min(uservalue[i][4]))
                                
                                

                                new_entries[indx].configure( state = 'disabled')
                                polish_ward[indx].configure( state = 'disabled')
                                liczba_wyswietlen[indx].configure( state = 'disabled')
                                liczba_poprawnych[indx].configure( state = 'disabled')
                                data_dodania[indx].configure( state = 'disabled')
            def SortPL(event):
        
                    for it in str(event.num):

                        if it == "1" :
                            self.numerP += 1
                
                            
                        if self.numerP%2 == 0:
                            uservalue.sort(key=sort_pol , reverse = True)
                        else:
                            uservalue.sort(key=sort_pol)

                        for indx, entry in enumerate(new_entries)  :
                 
                                new_entries[indx].configure( state = 'normal')
                                polish_ward[indx].configure( state = 'normal')
                                liczba_wyswietlen[indx].configure( state = 'normal')
                                liczba_poprawnych[indx].configure( state = 'normal')
                                data_dodania[indx].configure( state = 'normal')

                                new_entries[indx].delete(0, 'end')
                                polish_ward[indx].delete(0, 'end')
                                liczba_wyswietlen[indx].delete(0, 'end')
                                liczba_poprawnych[indx].delete(0, 'end')
                                data_dodania[indx].delete(0, 'end')
                                word= ','.join(uservalue[indx][0])
                                word1= ','.join(uservalue[indx][1])
                                      
                                new_entries[indx].insert("end",word)
                                
                                polish_ward[indx].insert("end",word1)
                                liczba_wyswietlen[indx].insert("end",int(sum(uservalue[i][2])/len(uservalue[i][2])))
                                liczba_poprawnych[indx].insert("end",int(sum(uservalue[i][3])/len(uservalue[i][3])))
                                if  uservalue[i][4].count('NAUCZONE') > 0:
                        
                                        DATA_POP = uservalue[i][4]
                                        g =list(filter(("NAUCZONE").__ne__, DATA_POP))
                                        data_dodania[indx].insert("end",min(g))
                                else:
                                        
                                        data_dodania[indx].insert("end",min(uservalue[i][4]))

                                new_entries[indx].configure( state = 'disabled')
                                polish_ward[indx].configure( state = 'disabled')
                                liczba_wyswietlen[indx].configure( state = 'disabled')
                                liczba_poprawnych[indx].configure( state = 'disabled')
                                data_dodania[indx].configure( state = 'disabled')

            frame71.place(relwidth = 1 , relheight = 0.05 )
            lalEnglish = Label(frame71 ,font = ('arial', 14 , 'bold')  , bd = 4   , justify = 'center' , width = 51 , text =tree_columns[0] ,
             relief='ridge' , bg='#458B74')
            lalEnglish.place(relwidth = 0.3 , relheight = 1 , relx=0.1)
            lalEnglish.bind("<Button-1>", cos)

            lalpolish = Label(frame71 ,font = ('arial', 14 , 'bold')  , bd = 4   , justify = 'center' , width = 51 , text =tree_columns[1] ,
             relief='ridge' , bg='#458B74')
            lalpolish.place(relwidth = 0.3 , relheight = 1 , relx=0.4)
            lalpolish.bind("<Button-1>", SortPL)

            lalLW = Label(frame71 ,font = ('arial', 7 , 'bold')  , bd = 4   , justify = 'center' , width = 51 , text =tree_columns[2] ,
             relief='ridge' ,bg='#458B74' )
            lalLW.place(relwidth = 0.07 , relheight = 1 , relx=0.7)
            lalLP = Label(frame71 ,font = ('arial', 7 , 'bold')  , bd = 4   , justify = 'center' , width = 51 , text =tree_columns[3] ,
             relief='ridge' ,bg='#458B74' )
            lalLP.place(relwidth = 0.07 , relheight = 1 , relx=0.77)
            lalDATE = Label(frame71 ,font = ('arial', 7 , 'bold')  , bd = 4   , justify = 'center' , width = 51 , text =tree_columns[4] ,
             relief='ridge' ,bg='#458B74' )
            lalDATE.place(relwidth = 0.10 , relheight = 1 , relx=0.84)   


        self.Lista = Button(self.frame2 , text='Moje Słówka' , width=13, bg='#458B74' , font = ('arial' , 19 , 'bold'), bd=3 , command = Lista , justify = 'center')
        self.Lista.place(relwidth =1 , relheight = 0.07 , relx =0.08 , rely = 0.15)
#================================================================================================================================
        self.dodajslowka = Button(self.frame2 , text='Dodaj Słówka' , width=13, bg='#458B74' , font = ('arial' , 19 , 'bold'), bd=3 , command = dodaj_slowka ,justify = 'center')
        self.dodajslowka.place(relwidth =1 , relheight = 0.07 , relx =0.08 , rely = 0.7)
#=======================================================TRANSLATOR================================================
        def Translator_APP ():
            self.frame6 = Frame(self.frame1 , bg = 'white')
            
            self.frame6.place(relwidth = 0.65 , relheight = 0.9 , relx = 0.30 , rely = 0.05)
            self.slowka_angielskie = Label(self.frame6 , text = 'Słówko Angielskie' , font = ('arial', 20 , 'bold') , bg = 'white')
            self.slowka_angielskie.place(   relx = 0.15 , rely = 0.15)
            self.txtslowka_angielskie = Entry(self.frame6 ,font = ('arial', 19 , 'bold')  , bd = 2  ,  bg = 'white', relief='ridge' ,)
            self.txtslowka_angielskie.place(relwidth = 0.7 , relheight = 0.08 ,  relx = 0.15 , rely = 0.22)
            self.slowka_polskie = Label(self.frame6 , text = 'Słówko Polskie' , font = ('arial', 20 , 'bold') , bg = 'white')
            self.slowka_polskie.place(   relx = 0.15 , rely = 0.4)
            self.txtslowka_polskie = Entry(self.frame6 ,font = ('arial', 19 , 'bold')  , bd = 2  ,  bg = 'white', relief='ridge' , )
            self.txtslowka_polskie.place(relwidth = 0.7 , relheight = 0.08 ,  relx = 0.15 , rely = 0.48)
            
            def reverse_C ():

                    self.reserv_count+=1

                    if self.reserv_count%2 == 0:
                            self.slowka_angielskie.place(   relx = 0.15 , rely = 0.4)
                            self.txtslowka_angielskie.place(relwidth = 0.7 , relheight = 0.08 ,  relx = 0.15 , rely = 0.48)
                            self.slowka_polskie.place(   relx = 0.15 , rely = 0.15)
                            self.txtslowka_polskie.place(relwidth = 0.7 , relheight = 0.08 ,  relx = 0.15 , rely = 0.22)
                    else:
                            self.slowka_angielskie.place(   relx = 0.15 , rely = 0.15)
                            self.txtslowka_angielskie.place(relwidth = 0.7 , relheight = 0.08 ,  relx = 0.15 , rely = 0.22)
                            self.slowka_polskie.place(   relx = 0.15 , rely = 0.4)
                            self.txtslowka_polskie.place(relwidth = 0.7 , relheight = 0.08 ,  relx = 0.15 , rely = 0.48)

            def trans ():

                        pol_word = self.txtslowka_polskie.get()
                        eng_word = self.txtslowka_angielskie.get()
                        if len(pol_word)>0 and len(eng_word)>0:
                                self.txtslowka_polskie.delete(0, 'end')
                                self.txtslowka_angielskie.delete(0, 'end')
                        else:

                                if len(pol_word)>0:

                                        translator = Translator()
                                        translations = translator.translate(pol_word, dest='EN')

                                        self.txtslowka_angielskie.insert('end' , translations.text)
                                elif len(eng_word)>0:

                                        translator = Translator()
                                        translations = translator.translate(eng_word, dest='pl')

                                        self.txtslowka_polskie.insert('end' , translations.text)
                                else:

                                        tkinter.messagebox.showinfo("one window" , "one window must be filled")

                        
            reverse = PhotoImage(file = 'reverse.png',width=65, height=65)
            
            self.button_reverse = Button(self.frame4 , image = reverse , justify = "center" ,command = reverse_C)
            self.button_reverse.place(relx=0.48, rely = 0.35)
            
            
            def addword ():
                USERWARD = pickle.load(open("USERWARD.py" , "rb"))
                englishward = self.txtslowka_angielskie.get()
                englishword_strip =[]
                
                for word in englishward.split(','):
                    englishword_strip.append(word.strip())
                polishward = self.txtslowka_polskie.get()
                polishward_strip=[]
                for word1 in polishward.split(','):
                    polishward_strip.append(word1.strip())

                uservalue = USERWARD[self.User]

                date = datetime.date.today()
                
                if list(uservalue).count(englishward) >= 1:

                    tkinter.messagebox.showinfo("Word" , "The word exists ")

                else:
                    uservalue.append([englishword_strip, polishward_strip , [0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0], [ date, date, date, date, date, date, date, date]])
                    USERWARD[self.User] = uservalue

                    pickle.dump(USERWARD , open("USERWARD.py" , "wb"))
                    englishward = self.txtslowka_angielskie.delete(0, 'end')
                    polishward = self.txtslowka_polskie.delete(0, 'end')
                    self.calkowita_liczba_slow.config(text = "liczba słów :{}".format(len(uservalue)) )

            self.addslowko_T = Button(self.frame4 , text = "Dodaj Słówko" , width=12 , bg='#458B74' , font = ('arial' , 20 , 'bold'), bd=3,
            command =addword , justify = 'center')
            self.Translator_btn = Button(self.frame4 , text = "Translator" , width=12 , bg='#458B74' , font = ('arial' , 20 , 'bold'), bd=3,
            command = trans , justify = 'center')
            self.Translator_btn .place (relx = 0.15 , rely = 0.7)
            
            self.addslowko_T.place (relx = 0.65 , rely = 0.7)
            self.Master.mainloop()

        self.losujslowka = Button(self.frame2 , text='Translator' , width=13, bg='#458B74' , font = ('arial' , 19 , 'bold'), bd=3 ,justify = 'center',
        command = Translator_APP)
        self.losujslowka.place(relwidth =1 , relheight = 0.07 , relx =0.08 , rely = 0.8)

#=============================================AVATAR===============================================================      
        def open_file():
            filename = fd.askopenfilename(filetypes=[("Plik PNG","*.PNG"),("Plik JPG","*.JPG")]) # wywołanie okna dialogowego open file
        
            if filename:
                with Image.open(filename ) as file:
                    file.save("{}.png".format(self.User))
                    self.test = PhotoImage(file ="{}.png".format(self.User))
                    self.avatar = Button ( self.frame3 , image = self.test  ,  width=13, bg='white' , font = ('arial' , 15 , 'bold'), bd=3 , command = open_file)
                    self.avatar.place(relwidth = 0.3 , relheight = 0.4 , relx = 0.3 , rely = 0.1)

        self.frame3 = Frame(self.frame2, bg = 'white')
        self.frame3.place(relwidth = 1 , relheight = 0.4 , relx = 0.08 , rely = 0.25)

        
        self.fname = "{}.png".format(self.User)
        if os.path.isfile(self.fname):
            self.test = PhotoImage(file ="{}.png".format(self.User))
            self.avatar = Button ( self.frame3 , image = self.test  ,  width=13, bg='white' , font = ('arial' , 15 , 'bold'), bd=3 , command = open_file)
            self.avatar.place(relwidth = 0.3 , relheight = 0.4 , relx = 0.3 , rely = 0.1)
    
        else:
            
            self.avatar = Button ( self.frame3 , text='AVATAR'  ,  width=4, bg='white' , font = ('arial' , 15 , 'bold'), bd=3 , command = open_file)
            self.avatar.place(relwidth = 0.3 , relheight = 0.4 , relx = 0.3 )
#=======================================================================================================================
        self.LoginName = Label (self.frame3 , text =self.User , bg='white' , font = ('arial' , 20 , 'bold'))
        self.LoginName.place( rely = 0.58 , relx = 0.15 , relwidth = 0.6 )
        self.Liczba_punktow_today = Label (self.frame3 , text ="liczba punktów dzisiaj :{}".format(userDane1[7]) , bg='white' , font = ('arial' , 10 , 'bold'))
        self.Liczba_punktow_today.place( rely = 0.68 , relx = 0.15 , relwidth = 0.6 )
        self.calkowita_liczba_punktow = Label (self.frame3 , text ="liczba punktów  :{}".format(userDane1[5]) , bg='white' , font = ('arial' , 10 , 'bold'))
        self.calkowita_liczba_punktow.place( rely = 0.76 , relx = 0.15 , relwidth = 0.6 )
        
        uservalue = USERWARD[self.User]
        
        self.calkowita_liczba_slow = Label (self.frame3 , text ="liczba Słów :{}".format(len(uservalue)) , bg='white' , font = ('arial' , 10 , 'bold'))
        self.calkowita_liczba_slow .place( rely = 0.86 , relx = 0.15 , relwidth = 0.6 )
#=================================================EXIT==============================================================
        def Exit ():
                self.Master.destroy()
                file = open('key.key', 'rb')
                key = file.read()
                USERDANE = pickle.load(open("USERDANE.py" , "rb"))
                pickle.dump( USERDANE, open( "USERDANE.py", "wb" ))
                with open('USERDANE.py', 'rb') as f:
                                data = f.read()

                fernet = Fernet(key)
                encrypted = fernet.encrypt(data)
                with open('USERDANE.py', 'wb') as f:
                                f.write(encrypted)

                USERWARD = pickle.load(open("USERWARD.py" , "rb"))

                pickle.dump( USERWARD, open( "USERWARD.py", "wb" ))
                with open("USERWARD.py", 'rb') as f1:
                                data1 = f1.read()

                password_provided = self.User

                password = password_provided.encode() 
                salt = b'\xc4:\xe3\xa9\x14x` ?\xee\xa7\xa7\xd3 >h' 
                kdf = PBKDF2HMAC(
                                algorithm=hashes.SHA256(),
                                length=32,
                                salt=salt,
                                iterations=100000,
                                backend=default_backend()
                                )
                key = base64.urlsafe_b64encode(kdf.derive(password)) 
                val_ferenet = Fernet(key)
                encrypted = val_ferenet.encrypt(data1)
                with open("USERWARD.py", 'wb') as f:
                                f.write(encrypted)

                mainWindow = Users()
                

        self.Exit = Button(self.frame2 , text='EXIT' , width=13, bg='#458B74' , font = ('arial' , 19 , 'bold'), bd=3 , command = Exit , justify = 'center')
        self.Exit.place(relwidth =1 , relheight = 0.07 , relx =0.08 , rely = 0.9)
#====================================================================================================================
        self.Master.mainloop()

#if  __name__ == "__main__":
   
    
    #for User in list(USERDANE):
            #User = Users()
User = Users()
       
