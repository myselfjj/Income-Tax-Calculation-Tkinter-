# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 20:33:48 2019

@author: hp
"""
from tkinter import *
import os

def login_sucess():
  global screen3
  screen3 = Toplevel(screen2)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login Sucess").pack()
  Button(screen3, text = "OK", command =calculator()).pack()
  
def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen2)
  screen4.title("Success")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack() 

def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Success")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()   
  
def notmatch():
  global screen6
  screen6 = Toplevel(screen1)
  screen6.title("NOT MATCH!!")
  screen6.geometry("150x100")
  Label(screen6, text = "Password Doesn't Match!!",fg="red").pack()
  Button(screen6, text = "OK", command =delete5).pack()
  
def already():
  global screen7
  screen7 = Toplevel(screen1)
  screen7.title("Username")
  screen7.geometry("150x100")
  Label(screen7, text = "Username already exist!!",fg="red").pack()
  Button(screen7, text = "OK", command =delete6).pack()

def register_user():
  print("working")
  username_info = username.get()
  password_info = password.get() 
  confirm_info=confirm_password.get()
  list_of_files = os.listdir()
  if username_info not in list_of_files:
      if  password_info==confirm_info and password_info!="":
          file=open(username_info, "w")
          file.write(username_info+"\n")
          file.write(password_info)
          file.close()
          Label(screen1, text = "Registration Sucess", fg = "green" ,font = ("calibri", 11)).pack()
          username_entry.delete(0, END)
          name.delete(0, END)
      else:
          notmatch()
  else:
      already()
  password_entry.delete(0, END) 
  confirm_password_entry.delete(0, END)
  
  
  
def login_verify():
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_sucess()
    else:
        password_not_recognised()
  else:
        user_not_found()
        
def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x420") 
  global l1
  global username
  global password
  global username_entry
  global password_entry
  global confirm_password_entry
  global confirm_password
  global user_name
  username = StringVar()
  password = StringVar()
  confirm_password= StringVar()
  Label(screen1, text = "Please enter details below", bg="grey",width="300",fg="white").pack()
  Label(screen1, text = "").pack()
  
  Label(screen1, text = "Name : ").pack()
  user_name = Entry(screen1, textvariable ="")
  user_name.pack()
  Label(screen1, text = "").pack()
  
  Label(screen1, text = "Gender : ").pack()
  gender=Radiobutton(screen1,text="Male",value=1).pack()
  gender=Radiobutton(screen1,text="Female",value=2).pack()
  Label(screen1, text = "").pack()
  
  Label(screen1, text = "Username: ").pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Password * ").pack()
  password_entry =  Entry(screen1, textvariable = password,show="*")
  password_entry.pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Confirm  * ").pack()
  confirm_password_entry =  Entry(screen1, textvariable = confirm_password,show="*")
  confirm_password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()
def login():
  global screen2
  screen2 = Toplevel(screen)
  screen2.title("Login")
  screen2.geometry("250x175")
  global username_verify
  global password_verify 
  username_verify = StringVar()
  password_verify = StringVar()
  global username_entry1
  global password_entry1
  Label(screen2,text="Enter Details Below \n", font = ("Times", 11,"bold")).grid(row=0,column=4)
  Label(screen2, text = "Username ").grid(row=1,column=3)
  username_entry1 = Entry(screen2, textvariable = username_verify)
  username_entry1.grid(row=1,column=4)
  Label(screen2,text=" ").grid(row=2,column=0)
  Label(screen2, text = "Password ").grid(row=3,column=3)
  password_entry1 = Entry(screen2, textvariable = password_verify ,show="*")
  password_entry1.grid(row=3,column=4)
  Label(screen2,text=" ").grid(row=4,column=0)
  Button(screen2, text = "Login",bg="yellow", width = 10, height = 1, command = login_verify).grid(row=5,column=4)

def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x230")
  screen.title("ITC")
  Label(text = "INCOME TAX CALCULATION", bg = "grey",fg="white", width = "300", height = "2", font = ("Times", 13,"bold")).pack()
  Label(text = "").pack()
  Button(text = "Login", bg="blue", fg="white", height = "2", width = "30", command = login).pack()
  Label(text = "").pack()
  Button(text = "Register", bg="blue", fg="white",height = "2", width = "30", command = register).pack()
  screen.mainloop()
main_screen()

def calculator():
  global screen8
  screen8 = Toplevel(screen)
  screen8.geometry("300x260")
  screen8.title("Calculator")
  Label(screen8,text = "CLICK TO CALCULATE", bg = "grey",fg="white", width = "300", height = "2", font = ("Times", 13, "bold")).pack()
  Label(screen8,text = " ").pack()
  Button(screen8, text = "ADVANCE INCOME TAX",bg="CadetBlue3", width = "30", height = "2",command=AIT).pack()
  Label(screen8,text = " ").pack()
  Button(screen8, text = "QUICK INCOME TAX",bg="CadetBlue3", width = "30", height = "2").pack()
  Label(screen8,text = " ").pack()
  Button(screen8, text = "EXIT",bg="red3", width = "10", height = "2",command=delete).pack()
  screen3.destroy()
  screen2.destroy()
  
def cal1():
    global screen10
    screen10=Toplevel(screen9)
    screen10.geometry("200x300")
    screen10.title("Result")
    Label(screen10,text="Tax Report",bg="grey",width="200",height="2").pack()
    year1=year.get()
    age1=age.get()
    income1=int(income.get())
    other1=int(other.get())
    
    Label(screen10,text=" ").pack()
    Label(screen10,text="Total Income Rs.",fg="red").pack()
    Entry(screen10,textvariable=tincome,bd=10).pack()
    
    Label(screen10,text=" ").pack()
    Label(screen10,text="Tax to be Paid Rs.",fg="red").pack()
    Entry(screen10,textvariable=result,bd=10).pack()
    
    
    def cal_tax(income1,other1):
        
        if (income1 >= 0) and (income1 <= 250000):
            tax = (0*income1)
        elif (income1 > 250000) and (income1 <= 500000):
            tax = (0.05 * (income1-250000-other1))
        elif (income1 > 500000) and (income1 <= 1000000):
            tax = (12500 + (0.20*(income1-500000-other1)))
        else:
            tax=(112500+(0.30*(income1-1000000-other1)))
        return tax;
        
    result.set(cal_tax(income1,other1))
    tincome.set(int(income.get())-int(other.get()))  
    
    Button(screen10,text="OK",bd=5,command=delete7).pack()
  
  

  
def AIT():
  global screen9
  screen9=Toplevel(screen8)
  screen9.geometry("300x400")
  global year
  global age
  global income
  global result
  global tincome
  global other
  year=StringVar()
  age=StringVar()
  income=StringVar()
  other=StringVar()
  result=StringVar()
  tincome=StringVar()
  frame=Frame(screen9)
  label1=Label(frame,text="Financial Year")
  label2=Label(frame,text="Age Category")
  label6=Label(frame,text="Tax Payer")
  label3=Label(frame,text="Income")
  label4=Label(frame,text="Other deductions u/s 80C")
  label5=Label(frame,text="Residential Status")


  entry1=Entry(frame,textvariable= year ,bd=9)
  entry2=Entry(frame,textvariable= age ,bd=9)
  entry3=Entry(frame,textvariable= income ,bd=9)
  entry4=Entry(frame,textvariable= other ,bd=9)
  entry5=Label(frame,text="Individual",fg="red")
  entry6=Label(frame,text="Resident",fg="red")

  button=Button(frame,text="Calculate",bg="green",fg="white",bd=12,command=cal1)


  Label(frame,text=" ").grid(row=0,column=0)
  label1.grid(row=1,column=0)
  Label(frame,text=" ").grid(row=2,column=0)
  label2.grid(row=3,column=0)
  Label(frame,text=" ").grid(row=4,column=0)
  label3.grid(row=5,column=0)
  Label(frame,text=" ").grid(row=6,column=0)
  label4.grid(row=7,column=0)
  Label(frame,text=" ").grid(row=8,column=0)
  label5.grid(row=9,column=0)
  Label(frame,text=" ").grid(row=10,column=0)
  label6.grid(row=11,column=0)
  Label(frame,text=" ").grid(row=12,column=0)

  Label(frame,text=" ").grid(row=0,column=1)
  entry1.grid(row=1,column=1)
  Label(frame,text=" ").grid(row=12,column=1)
  entry2.grid(row=3,column=1)
  Label(frame,text=" ").grid(row=4,column=1)
  entry3.grid(row=5,column=1)
  Label(frame,text=" ").grid(row=6,column=1)
  entry4.grid(row=7,column=1)
  Label(frame,text=" ").grid(row=8,column=1)
  entry6.grid(row=9,column=1)
  Label(frame,text=" ").grid(row=10,column=1)
  entry5.grid(row=11,column=1)
  Label(frame,text=" ").grid(row=12,column=1)

  button.grid(row=13,column=0,columnspan=3)

  frame.grid(row=0,column=3)

  
def delete():
   screen8.destroy();
   screen.destroy();
    
def delete3():
  screen4.destroy()
  
def delete4():
  screen5.destroy()
def delete5():
  screen6.destroy()
def delete6():
  screen7.destroy()
def delete7():
  screen10.destroy()
