from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog as fd
import json

with open ("monnaies.json") as monnaie:
    argent = json.load(monnaie)

def database(amount:int,fromdevice:str,todevice:str,result:float): 
    dictresult = {"amount":amount,"fromDevice":fromdevice,"toDevice":todevice,"amountConverted":result}    
    with open ("historique.json","r+") as fichier:
        donnees = json.load(fichier)
        donnees["historique"].append(dictresult)
        fichier.seek(0)
        json.dump(donnees,fichier,indent=4)


        
def fromCur(choix):
    return choix
  
def toCur(choix):
    return choix  
def clear(): #cette fonction va effacer les entry, mettre les menu par defaults et les actualiser, actualiser argent
    global menu1,menu2,amount_entry,convertamount_entry, newcurrencyEntry, newcurrencyvalueEntry,crypto,fromcurrencyMenu,tocurrencyMenu, argent
    with open ("monnaies.json") as monnaie:
        argent = json.load(monnaie)
    menu1.set('Monnaie')
    menu2.set('Monnaie')
    fromcurrencyMenu = OptionMenu(frame,menu1,*crypto,command=fromCur)
    fromcurrencyMenu.grid(column=1,row=1)
    tocurrencyMenu = OptionMenu(frame,menu2,*crypto,command=toCur)
    tocurrencyMenu.grid(column=1,row=2)
    amount_entry.delete(0,END)
    convertamount_entry.delete(0,END)
    newcurrencyEntry.delete(0,END)
    newcurrencyvalueEntry.delete(0,END)
    convertamount_entry.config(state=DISABLED)


def convert():
    global amount_entry,fromcurrencyMenu,tocurrencyMenu, convertamount_entry
    convertamount_entry.config(state=NORMAL),error
    try:
        convertamount_entry.delete(0,END)
        valeur = amount_entry.get()
        change =  (int(valeur) * argent["monnaies"][menu1.get()]) / argent["monnaies"][menu2.get()]
        convertamount_entry.insert(0,change)
        database(int(valeur),menu1.get(),menu2.get(),change)
        error.config(fg="grey")
    except:
        error.config(text="Erreur, vérifiez la valeur donnée et les devises",fg="red")
        clear()

def addMonnaie():
    global newcurrencyEntry, newcurrencyvalueEntry, crypto, error, menu1, menu2, frame, fromcurrencyMenu, tocurrencyMenu
    try:
        name = newcurrencyEntry.get()
        value = newcurrencyvalueEntry.get()
        with open ("monnaies.json","r+") as fichier:
            argent = json.load(fichier)
            argent["monnaies"][name]=float(value)
            fichier.seek(0)
            json.dump(argent,fichier,indent=3)
        crypto.append(name)
        clear() 
        error.config(fg="grey")
    except:
        error.config(text="Erreur Lors de l'ajout d'une monnaie",fg="red")
        clear()
        
fenetre = Tk()
fenetre.title("Accueuil")
fenetre.geometry("1080x720")
fenetre.minsize(480,360)
fenetre.config(background="grey")
frame = Frame(fenetre)
frame.config(background="grey")
frame.pack(expand=YES)
amountText = Label(frame, text="Amount :",background="grey",font=("Arial",20))
amountText.grid(column=0,row=0)
amount_entry= Entry(frame)
amount_entry.grid(column=1,row=0)
fromcurrencyText = Label(frame, text="From Currency :",background="grey",font=("Arial",20))
fromcurrencyText.grid(column=0,row=1)
crypto = []
for i in argent["monnaies"].keys():
    crypto.append(i)
menu1 = StringVar(fenetre)
menu1.set('Monnaie')
menu2 = StringVar(fenetre)
menu2.set('Monnaie')
fromcurrencyMenu = OptionMenu(frame,menu1,*crypto,command=fromCur)
fromcurrencyMenu.grid(column=1,row=1)
tocurrencyMenu = OptionMenu(frame,menu2,*crypto,command=toCur)
tocurrencyMenu.grid(column=1,row=2)
tocurrencyText = Label(frame, text="To Currency :",background="grey",font=("Arial",20))
tocurrencyText.grid(column=0,row=2)
convertButton = Button(frame, text="Convert",font=("Arial",20),width=10, background="Blue",fg="white",command=convert)
convertButton.grid(column=0,row=3)
convertamountText = Label(frame, text="Converted Amount :",background="grey",font=("Arial",20))
convertamountText.grid(column=0,row=4)
convertamount_entry= Entry(frame,state=DISABLED)
convertamount_entry.grid(column=1,row=4)
clearButton = Button(frame, text="Clear all",font=("Arial",20),width=10, background="white",fg="red",command=clear)
clearButton.grid(column=0,row=5)
newcurrencyText = Label(frame,text="New Currency Name",background="grey",font=("Arial",20))
newcurrencyText.grid(column=0,row=6)
newcurrencyEntry = Entry(frame)
newcurrencyEntry.grid(column=1,row=6)
newcurrencyvalueText = Label(frame,text="New Currency Change number",background="grey",font=("Arial",20))
newcurrencyvalueText.grid(column=0,row=7)
newcurrencyvalueEntry = Entry(frame)
newcurrencyvalueEntry.grid(column=1,row=7)
newcurrencyButton =Button(frame, text="Add New Currency",font=("Arial",10),width=15, background="blue",fg="white",command=addMonnaie)
newcurrencyButton.grid(column=0,row=8)
error = Label(frame,text="Erreur",font=("Arial",10),fg="grey",background="grey")
error.grid(column=0,row=9)
fenetre.mainloop()