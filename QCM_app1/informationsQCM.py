# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:47:59 2022

@author: Landry SANON 
"""
import os 
import sys
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import Image, ImageTk
from tkcalendar import Calendar
from styleApp import FgColor, BgColor
#from datetime import date
#Today = date.today()




class fenetreInformations(Tk):
    """
    Check the validity of the input data. If the data is valid, create a new window with the informations.
    @param self - the window itself
    """
    # Declare constants
    _Niveau     = ('JMA1',
                   'JMA2',
                   'JMA3')
    
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

    
    def __init__(self):
        Tk.__init__(self)
        # Prepare the window
        self.NbrQuestions     = StringVar()
        self.nomQuestionnaire = StringVar()
        self.nomProfesseur    = StringVar()
        self.nNiveau          = StringVar()
        self.tDepart          = StringVar()
        self.tDuree           = StringVar()
        self.geometry('1080x600')
        self.configure(bg = "#261934")
        self.title('Junia Maroc [QCM]')
        self.applyStyle()
        self.suivant = False
        # Fixate parameters
        _dParams            = dict()
        _dParams['padx']    = 10
        _dParams['ipadx']   = 10
        _dParams['pady']    = 10
        _dParams['sticky']  = W + N
        # Prepare labels
        _lTitre             = Label(self, text = 'Junia QCM', font = ("Times New Roman (Titres CS)", 40))
        _lNomQuestionnaire  = Label(self, text = 'Nom du questionnaire: ')
        _lNomProfesseur     = Label(self, text = 'Nom du professeur: ')
        _lNiveau            = Label(self, text = 'Niveau: ')
        _lNbrQuestions      = Label(self, text = 'Nombre de Questions: ')
        _lCalendrier        = Label(self, text = 'Calendrier: ')
        _lDepart            = Label(self, text = 'Heure de départ: ')
        _lDuree             = Label(self, text = 'Durée: ')
        # Prepare edits
        _eNomQuestionnaire  = Entry(self, textvariable = self.nomQuestionnaire)
        _eNomProfesseur     = Entry(self, textvariable = self.nomProfesseur)
        _eNbrQuestions      = Entry(self, textvariable = self.NbrQuestions)
        _eDepart            = Entry(self, textvariable = self.tDepart)
        _eDuree             = Entry(self, textvariable = self.tDuree)
        #
        _mNiveau            = OptionMenu(self, self.nNiveau, "Niveau", *self._Niveau)
        self.cCalendrier    = Calendar(self)
        _bSuivant           = Button(self, text = 'Suivant',
                                     command = self.executionBoutonSuivant)
        
        self._bPrecedent= Button(self, text = 'Précédent',
                                     command = self.executionBoutonPrecedent)
        
        # Position elements
        _lTitre.grid(row = 0, column = 1, **_dParams)
        _lNomQuestionnaire.grid(row = 2, column = 0, **_dParams)
        _lNomProfesseur.grid(row = 3, column = 0, **_dParams)
        _lNiveau.grid(row = 5, column = 0, **_dParams)
        _lNbrQuestions.grid(row = 4, column = 0, **_dParams)
        _lCalendrier.grid(row = 6, column = 0, **_dParams)
        _lDepart.grid(row = 7, column = 0, **_dParams)
        _lDuree.grid(row = 8, column = 0, **_dParams)
        #
        _eNomQuestionnaire.grid(row = 2, column = 1, **_dParams)
        _eNomProfesseur.grid(row = 3, column = 1, **_dParams)
        _eNbrQuestions.grid(row = 4, column = 1, **_dParams)
        _eDepart.grid(row = 7, column = 1, **_dParams)
        _eDuree.grid(row  = 8, column = 1, **_dParams)
        _mNiveau.grid(row = 5, column = 1, **_dParams)
        _mNiveau.config(width = 16)
        self.cCalendrier.grid(row = 6, column = 1, **_dParams)
        #
        _bSuivant.grid(row = 9, column = 2, **_dParams)
        #
        self._bPrecedent.grid(row = 9, column = 1, **_dParams)
        
    def executionBoutonPrecedent(self):
        """
        When the user clicks the previous button, destroy the current window and open the menu window.
        @param self - the current window
        """
        self.Precedent = True
        
        self._bPrecedent.configure(state= NORMAL)
        self.destroy()
        from QCM_app import fenetreMenu
        fenetreMenu().mainloop()     

    def executionBoutonSuivant(self):
        """
        When the user clicks on the "Next" button, we check that the syntax of the input is correct before moving on to the next window
        @returns nothing
        """
        #print( "Le nom du questionnaire est :  " + self.nomQuestionnaire.get() )
        #print( "Le nom du professeur est :  " + self.nomProfesseur.get() )
        #print( "Le Niveau :  " + self.nNiveau.get() )
        #print( "Le nombre de questions est : ", self.numQuestions.get())
        #print( "La date du QCM est : " , self.cCalendrier.get_date())
        #print( "L'heur de départ est : ", self.tDepart.get())
        #print( "La durée du QCM est : ", self.tDuree.get())
        #y1, m1, j1 = [int(x) for x in Today.split("-")]
        #y2, m2, j2 = [int(x) for x in self.cCalendrier.get().split("/")]
        #B1 = date(y1,m1,j1)
        #B2 = date(y2,m2,j2)
       # b2 = Today.strftime("%d")
        #b1 = self.cCalendrier.split("/")
       # if B1 < B2 :
            #messagebox.showerror(title="Mauvaise syntaxe", message="Donner une date valide")
        #if self.NbrQuestions.get() <= 0 :
            #messagebox.showerror(title="Mauvaise syntaxe", message="Donner un nombre valide")
   
       # else :
        try:
            print(self.nNiveau.get())
            x=int(self.NbrQuestions.get()) 
            if self.nomQuestionnaire.get() =="" or self.nomProfesseur.get() =="" or self.nNiveau.get() =="Niveau" or self.tDepart.get() =="" or self.tDuree.get() =="":
                messagebox.showerror(title="Mauvaise syntaxe", message="Ne Laissez aucun champs vide")
            else:
                test =[]
                for i in self.nomQuestionnaire.get().split(" "):
                    test.append(i)
                for i in self.nomProfesseur.get().split(" "):
                    test.append(i)
                
                test=[i.isalpha() for i in test]
                if False in test:
                        messagebox.showerror(title="Mauvaise syntaxe", message="Characteres spéciales non acceptés")
                heure_minute=self.tDepart.get().split('H') 
                if len(heure_minute)!=2 or False in [i.isdigit() for i in heure_minute]:
                    messagebox.showerror(title="Mauvaise syntaxe", message="Syntaxe pour l'heure ex : 11H30")
                heure_duree=self.tDuree.get().split('H') 
                if len(heure_duree)!=2 or False in [i.isdigit() for i in heure_duree]:
                        messagebox.showerror(title="Mauvaise syntaxe", message="Syntaxe pour la durée ex : 11H30 ou 00H30 pour 30 min")
                else: 
                    
                    self.suivant = True
                    self.destroy()            
        except:
            messagebox.showerror(title="Mauvaise syntaxe", message="Le Nombre de question est un nombre")
        

    
    





