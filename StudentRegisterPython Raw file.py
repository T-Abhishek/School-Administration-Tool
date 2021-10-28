import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import csv
from os import _fspath

def about():
    messagebox.showinfo("Created by","T Abhishek\n196N1A05C0")

def proces():
    s1=Ea.get()
    s2=Eb.get()
    r=v0.get()
    s3=box_value.get()
    s4=Ed.get()
    student_info=[s1,r,s2,s3,s4]
    msg='Entered information is successfully saved as student_info.csv in '+str(os.getcwd())
    messagebox.showinfo("Message",msg)
    
    if os.path.exists('student_info.csv')==True:
        with open('student_info.csv','a',newline='') as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow(student_info)
    else:
        with open('student_info.csv','a',newline='') as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow(['NAME','GENDER','ROLL NO','BRANCH','OTHER INFO'])
            writer.writerow(student_info)

top=tk.Tk()
top.geometry("350x200")
top.title('SRINIET STUDENT REGISTER')

L=tk.Label(top,text='Enter student Information',font=('Cambria',11,'bold')).place(x=80,y=0)
# LABEL 1 NAME AND ENTRY 1
L1=tk.Label(top,text='Name',font=('Ubuntu',10)).place(x=30,y=30)
Ea=tk.StringVar()
E1=tk.Entry(top,textvariable=Ea,width=30).place(x=130,y=30)

# MALE FEMALE RADIO BUTTON
v0=tk.StringVar()
v0.set(1)
r1=tk.Radiobutton(top,text="male",variable=v0,value='Male').place(x=130,y=50)
r2=tk.Radiobutton(top,text="female",variable=v0,value='Female').place(x=180,y=50)

# LABEL 2 ID AND ENTRY 2
L2=tk.Label(top,text='ID',font=('Ubuntu',10)).place(x=30,y=80)
Eb=tk.StringVar()
E3=tk.Entry(top,textvariable=Eb,width=30).place(x=130,y=80)

# LABEL 3 BRANCH AND COMBOBOX
L3=tk.Label(top,text='BRANCH',font=('Ubuntu',10)).place(x=30,y=110)
box_value=tk.StringVar()
branch=("CSE", "ECE", "EEE", "MECH","CIVIL")
cb=ttk.Combobox(top,values=branch,textvariable=box_value,state='readonly',width=27).place(x=130,y=110)

# LABEL 4 OTHER INFO AND ENTRY 4
L4=tk.Label(top,text='OTHER INFO',font=('Ubuntu',10)).place(x=30,y=140)
Ed=tk.StringVar()
E4=tk.Entry(top,textvariable=Ed,width=30).place(x=130,y=140)

# SAVE RADIO BUTTON
B=tk.Button(top,text ="Save",command=proces).place(x=180,y=170)
# INFO RADIO BUTTON
B=tk.Button(top,text ="About",command=about).place(x=220,y=170)


top.mainloop()
