# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:21:12 2022

@author: Hatim NAQOS
"""


from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import Image, ImageTk
from tkcalendar import Calendar
from datetime import date
from styleApp import FgColor, BgColor


Today = date.today()
def estListeElementsVide(Liste):
            for l in Liste:
                if(l != ""):
                    return False
            return True
def verification(self):
    """
    Verify that the user has entered a valid date and that the number of questions is valid.
    @param self - the object itself
    @returns nothing
    """
    y1, m1, j1 = [int(x) for x in Today.split('-')]
    y2, m2, j2 = [int(x) for x in self.cCalendrier.get().split('/')]
    B1 = date(y1,m1,j1)
    B2 = date(y2,m2,j2)
    if B2 < B1 :
        messagebox.showerror(title="Mauvaise syntaxe", message="Donner une date valide")

    if self.NbrQuestions.get() <= 0 :
        messagebox.showerror(title="Mauvaise syntaxe", message="Donner un nombre valide")

class questionFenetre(Tk):
        """
        This is the window that will be used to ask the user for input.
        @param Tk - the Tkinter module
        """
       
        def applyStyle(self):
            _sStyle = ttk.Style(self)
            #_iImg   = Image.open("E://Projet QCM//bg1.png")
            #_iBack  = ImageTk.PhotoImage(_iImg, master = self)
            #_lBack  = Label(self, image = _iBack)
            #_lBack.grid(row=0, column=0)
            _sStyle.theme_use('clam')
            _sStyle.configure('TButton',
                              foreground = 'white',
                              background = FgColor(),
                              font = ('Times New Roman (Titres CS)', 12, 'bold'))
            _sStyle.configure('TLabel',
                              foreground = FgColor(),
                              background = BgColor(),
                              font = ('Times New Roman (Titres CS)', 12, 'bold'))
            _sStyle.configure('TEntry',
                              font = ('Times New Roman (Titres CS)', 12, 'bold'))
            _sStyle.configure('TFrame',
                              foreground = FgColor(),
                              background = BgColor(),
                              font = ('Times New Roman (Titres CS)', 12, 'bold'))
            _sStyle.configure('TRadiobutton',
                              foreground = FgColor(),
                              background = BgColor(),
                              font = ('Times New Roman (Titres CS)', 12, 'bold'))
        

        
        def __init__(self, nombreQuestions : int):
            # Prepare the window
            Tk.__init__(self)
            self.question = StringVar()
            self.numeroQuestion = 1
            self.titre = StringVar()
            self.titre.set('Question Numéro ' + str(self.numeroQuestion))
            self.bonneReponse = StringVar()
            self.reponseA = StringVar()
            self.reponseB = StringVar()
            self.reponseC = StringVar()
            self.reponseD = StringVar()
            self.nombreQuestions  = nombreQuestions
            self.bareme = [[i+1]+["" for i in range(6) ] for i in range(nombreQuestions) ]
            self.suivant= False
            #print(self.bareme)
            
            self.geometry('1080x600')
            self.configure(bg = "#261934")
            self.title('Junia Maroc [QCM]')
            self.applyStyle() 
            frameReponse = Frame(self)
            #frameReponse.config(Background = "#261934")
            # Fixate parameters
            _dParams            = dict()
            _dParams['padx']    = 10
            _dParams['ipadx']   = 10
            _dParams['pady']    = 10
            _dParams['sticky']  = W + N
            #Prepare Labels
            self._lTitre             = Label(self, textvariable = self.titre ,font = ("Courier", 30))
            _lReponses          = Label(self, text = "Reponses : ")
            _lReponseA          = Label(frameReponse, text = "A")
            _lReponseB          = Label(frameReponse, text = "B")
            _lReponseC          = Label(frameReponse, text = "C")
            _lReponseD          = Label(frameReponse, text = "D")
            #Prepare edits
            self._eQuestion  = Text(self, wrap = WORD, width= 80, height= 8)
            self._eA = Entry(frameReponse, textvariable = self.reponseA)
            self._eA.focus_set()
            _eB = Entry(frameReponse, textvariable = self.reponseB)
            _eC = Entry(frameReponse, textvariable = self.reponseC)
            _eD = Entry(frameReponse, textvariable = self.reponseD)
            #Prepare Bonne réponse
            self._RadioBoutonA = Radiobutton(frameReponse, text="A", variable=self.bonneReponse, value="A")
            self._RadioBoutonB = Radiobutton(frameReponse, text="B", variable=self.bonneReponse, value="B")
            self._RadioBoutonC = Radiobutton(frameReponse, text="C", variable=self.bonneReponse, value="C")
            self._RadioBoutonD = Radiobutton(frameReponse, text="D", variable=self.bonneReponse, value="D")
            #Prepare Buttons
            self._bSuivant           = Button(self, text = 'Suivant',
                                     command = self.executionBoutonSuivant)
            self._bPrecedent           = Button(self, text = 'Précédent',
                                     command = self.executionBoutonPrecedent
                                     ,state= DISABLED)
            # Position elements
            
            self._lTitre.grid(row = 0, column = 0, **_dParams)
            self._eQuestion.grid(row = 1 , column = 0,  padx = 10 , pady = 10 )
            _lReponses.grid(row = 2 , column = 0 , **_dParams)
            #_lReponseA.grid(row = 3 , column = 0 , **_dParams)
            self._eA.grid(row = 3 , column = 1 , padx = 10 , pady = 10 ,ipadx = 100)
            self._RadioBoutonA.grid(row = 3 , column = 0,  padx = 10 , pady = 10)
            #_lReponseB.grid(row = 4 , column = 0 , **_dParams)
            _eB.grid(row = 4 , column = 1 , padx = 10 , pady = 10 ,ipadx = 100 )
            self._RadioBoutonB.grid(row = 4 , column = 0)
            #_lReponseC.grid(row = 5 , column = 0 , **_dParams)
            _eC.grid(row = 5 , column = 1, padx = 10 , pady = 10 ,ipadx = 100 )
            self._RadioBoutonC.grid(row = 5 , column = 0 )            
            #_lReponseD.grid(row = 6 , column = 0 , **_dParams)
            _eD.grid(row = 6 , column = 1, padx = 10 , pady = 10 ,ipadx = 100 )
            self._RadioBoutonD.grid(row = 6 , column = 0)            
            frameReponse.grid(row = 7 , column = 0)
            self._bSuivant.grid(row = 8 , column = 1 , padx = 10 , pady = 10)
            self._bPrecedent.grid(row = 8 , column = 0 , padx = 10 , pady = 10)

        def executionBoutonSuivant(self):
            #print( "Le nom du questionnaire est :  " + self.nomQuestionnaire.get() )
            #print( "Le nom du professeur est :  " + self.nomProfesseur.get() )
            #print( "Le Niveau :  " + self.nNiveau.get() )
            #print( "Le nombre de questions est : ", self.numQuestions.get())
            #print( "La date du QCM est : " , self.cCalendrier.get_date())
            #print( "L'heur de départ est : ", self.tDepart.get())
            #print( "La durée du QCM est : ", self.tDuree.get())
            if(self.numeroQuestion == self.nombreQuestions):
                self.suivant = True
                self.bareme[self.numeroQuestion - 1] = [self.numeroQuestion,
                                        self._eQuestion.get(1.0, END),
                                        self.reponseA.get(),
                                        self.reponseB.get(),
                                        self.reponseC.get(),
                                        self.reponseD.get(),
                                        self.bonneReponse.get()]
                self.destroy()
                
                return None
            #print(estListeElementsVide(self._eQuestion.get(1.0,END).split()))
            if (estListeElementsVide(self._eQuestion.get(1.0,END).split())):
                messagebox.showerror(title="Titre manquant", message="Veuillez remplir la question!")
            elif (estListeElementsVide(self.reponseA.get().split())):
                messagebox.showerror(title="Reponse A manquante", message="Veuillez remplir la réponse A!")
            elif (estListeElementsVide(self.reponseB.get().split())):
                messagebox.showerror(title="Reponse A manquante", message="Veuillez remplir la réponse B!")
            elif (estListeElementsVide(self.reponseC.get().split())):
                messagebox.showerror(title="Reponse A manquante", message="Veuillez remplir la réponse C!")   
            elif (estListeElementsVide(self.reponseD.get().split())):
                messagebox.showerror(title="Reponse A manquante", message="Veuillez remplir la réponse D!")
            elif self.bonneReponse.get() not in ["A","B","C","D"]:
                print(self.bonneReponse.get())
                messagebox.showerror(title="Bonne réponse manquante", message="Veuillez sélectionner la bonne réponse!")
            else:
                if(self.numeroQuestion == self.nombreQuestions-1):
                    self._bSuivant.configure(text = "Exporter en PDF")
                    
                if(self.numeroQuestion > 1):
                    self._bPrecedent.configure(state= NORMAL)
                
                if(self.numeroQuestion < self.nombreQuestions):
                    """print(f"Question {self.numeroQuestion}:", self._eQuestion.get(1.0, END))
                    print("Réponse A:",self.reponseA.get())
                    print("Réponse B:",self.reponseB.get())
                    print("Réponse C:",self.reponseC.get())
                    print("Réponse D:",self.reponseD.get())
                    print(f"Bonne réponse: {self.bonneReponse.get()}")
                    print("")"""
                    self.bareme[self.numeroQuestion - 1] = [self.numeroQuestion,
                                        self._eQuestion.get(1.0, END),
                                        self.reponseA.get(),
                                        self.reponseB.get(),
                                        self.reponseC.get(),
                                        self.reponseD.get(),
                                        self.bonneReponse.get()]
                    print(self.bareme)
                    self._eQuestion.delete(1.0, END)
                    print(self.bareme[self.numeroQuestion][1])
                    self._eQuestion.insert(1.0,self.bareme[self.numeroQuestion][1])
                    self.reponseA.set(self.bareme[self.numeroQuestion][2])
                    self.reponseB.set(self.bareme[self.numeroQuestion][3])
                    self.reponseC.set(self.bareme[self.numeroQuestion][4])
                    self.reponseD.set(self.bareme[self.numeroQuestion][5])
                    self.bonneReponse.set(self.bareme[self.numeroQuestion][6])              
                    self.numeroQuestion+=1
                    self.titre.set('Question Numéro ' + str(self.numeroQuestion))
                if(self.numeroQuestion > 1):
                    self._bPrecedent.configure(state= NORMAL)                

            
        

            
        def executionBoutonPrecedent(self):
            #print( "Le nom du questionnaire est :  " + self.nomQuestionnaire.get() )
            #print( "Le nom du professeur est :  " + self.nomProfesseur.get() )
            #print( "Le Niveau :  " + self.nNiveau.get() )
            #print( "Le nombre de questions est : ", self.numQuestions.get())
            #print( "La date du QCM est : " , self.cCalendrier.get_date())
            #print( "L'heur de départ est : ", self.tDepart.get())
            #print( "La durée du QCM est : ", self.tDuree.get())
            if (self.numeroQuestion > 1):
                self.numeroQuestion -= 1
            self.titre.set('Question Numéro ' + str(self.numeroQuestion))
            self._eQuestion.delete(1.0, END)
            self._eQuestion.insert(1.0,self.bareme[self.numeroQuestion - 1][1])
            self.reponseA.set(self.bareme[self.numeroQuestion -1][2])
            self.reponseB.set(self.bareme[self.numeroQuestion -1][3])
            self.reponseC.set(self.bareme[self.numeroQuestion -1][4])
            self.reponseD.set(self.bareme[self.numeroQuestion -1][5])
            self.bonneReponse.set(self.bareme[self.numeroQuestion -1][6])
            self._bSuivant.configure(text = "Suivant")

               
            if(self.numeroQuestion > 1):
                self._bPrecedent.configure(state= NORMAL)
            else:
                 self._bPrecedent.configure(state= DISABLED)
            
"""nombreQuestions = 5  
                    
PageQuestion = questionFenetre(nombreQuestions)  
PageQuestion.mainloop()   """

            
            