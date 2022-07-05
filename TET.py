#from socket import J1939_EE_INFO_NONE
from tkinter import*
import tkinter as tk
import json
import sys
from tkinter import ttk
from tkinter import messagebox, filedialog
#import mysql.connector
from PIL import ImageTk, Image
from os import listdir
import os
from os.path import isfile, join
def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', 'end', values=1)

def toggle2(event):
    for t in trv.get_children():
        trv.item(t, tags="unchecked")
        toggleCheck(event)

def toggleCheck(event):
    rowid = trv.identify_row(event.y)
    tag = trv.item(rowid, "tags")[0]
    tags=list(trv.item(rowid, "tags"))
    tags.remove(tag)
    trv.item(rowid, tags-tags)
    if tag == "checked":
        trv.tten(rowid, tags="unchecked")
    else:
        trv.item(rowid, tags="checked")

        
def search():
    q2 = q.get()
    cursor.execute(query)
    rows = cursor.fetchall()
    update (rows)
    query = "SELECT id, first_name, last_name, age FROM customers WHERE first_name LIKE '%"+q2+"%' OR last_name LIKE '%"+q2+"%'" 
    
def clear():
    query = "SELECT id, first name, last_name, age FROM customers"
    cursor.execute(query)
    rows = cursor.fetchall()
    update (rows)
    

def getrow():
    #rowid = trv.identify_row(event.y)
    item= trv.item(trv. focus())
    t1.set(item [ 'values' ][0])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
    t4.set(item[ 'values'][3])
    
def update_customer():
    fname=t2.get()
    Lname = t3.get()
    age = t4.get()
    custid = t1.get()
    mydb.commit()
    clear()
    if messagebox.askyesno("Confirm Please", "Are You Sure you want to update this customer?"):
        query = "UPDATE customers SET first_name = %s, last_name = %s, age= %s WHERE id = %s"
        cursor.execute(query, (fname, Lname, age, custid))
    else:
        return True
    
def add_new():
    fname=t2.get()
    Lname = t3.get()
    age = t4.get()
    query = "INSERT INTO customers(id, first_name, last_name, age, date) VALUES(NULL, %s, %s, %s, NOW())"
    cursor.execute(query, (fname, Lname, age))

    mydb.commit()
    clear()
    
def delete_customer ():

    customer_id = t1.get()
    if messagebox.askyesno ("Confirm Delete?", "Are you sure you want to delete this customer?"):
        query = "DELETE FROM customers WHERE id = "+customer_id
        cursor.execute(query)
        mydb.commit()
        clear()
    else:
        return True
    
root = Tk()
q= StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()
#mydb = mysql.connector.connect(host="localhost", user="codeworked", passwd="elephant", database="sample", auth_plugin="mysql_native_password")
#cursor = mydb.cursor()
mypath="{relative_path}"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
fjson=[]
for i in onlyfiles:

    taille=os.path.getsize(mypath+f"\{i}")
   
    if i[-5:]=='.json'and taille!=0 :
       
       fjson.append(i) 
f = open(mypath+f"\{fjson[0]}")
a=json.load(f)
rows=[ a['Informations']['nomQuestionnaire'],a['Informations']['nomProfesseur'],a['Informations']['nNiveau'],a['Informations']['tDate']]

wrapper1 = LabelFrame (root, text="Customer List")
#wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame (root, text="Customer Data")
wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
#wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)
#tn_checked = ImageTk.PhotoImage(Image.open("checked.png"))
#tn_unchecked = ImageTk.PhotoImage(Image.open("unchecked.png"))
trv = ttk.Treeview(wrapper1, columns=(1,2,3,4))
style= ttk.Style(trv)
style.configure('Treeview', rowheight=30)
#trv.tag_configure('checked', image=tn_checked)
#trv.tag_configure('unchecked', image=tn_unchecked)
trv.pack()
trv.heading('#0', text="")
trv.heading ('#1', text="nomQuestionnaire")
trv.heading('#2', text="nomProfesseur")
trv.heading('#3', text="nNiveau")
trv.heading('#4', text="tDate")
#trv.bind('<Double 1>', getrow)
trv.bind('<Button 1>', toggle2)



#query = "SELECT id, first_name, last_name, age from customers"
#cursor.execute(query)
#rows = cursor.fetchall()
update(rows)
#Search Section

#User Data Section


up_btn = Button (wrapper3, text="Update", command=update_customer)
add_btn = Button(wrapper3, text="Add New", command=add_new)
delete_btn = Button (wrapper3, text="Delete", command=delete_customer)
add_btn.grid(row=4, column=0, padx=5, pady=3)
up_btn.grid(row=4, column=1, padx=5, pady=3)
delete_btn.grid(row=4, column=2, padx=5, pady=3)
root.title("My Application")
root.geometry("800x700")
root.mainloop()