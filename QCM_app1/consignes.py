"""
Created on Tue Feb  8 18:47:59 2022

@author: Landry SANON 
"""
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import Image, ImageTk
from tkcalendar import Calendar
from styleApp import FgColor, BgColor


class fenetreConsigne(Tk):
    # Declare constants
 
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
        _sStyle.configure('TRadiobutton',
                          foreground = FgColor(),
                          background = BgColor(),
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
        self.store = dict()
        self.autre            =Text(self, wrap = WORD, width= 80, height= 8)
        self.opt1_selected    = IntVar()
        self.opt_selected     = IntVar()
        self.bonpoint         = StringVar()
        #self.mauvaispoint     = StringVar()
        self.NbrQuestions     = StringVar()
        self.nomQuestionnaire = StringVar()
        self.nomProfesseur    = StringVar()
        self.nNiveau          = StringVar()
        self.tDepart          = StringVar()
        self.tDuree           = StringVar()
        #self.minsize(1023,810)
        self.geometry('1080x600')
        self.configure(bg = "#261934")
        self.title('Junia Maroc [QCM]')
        self.applyStyle()
        self.suivant = False
        # Fixate parameters
        _dParams            = dict()
        _dParams['padx']    = 11
        _dParams['ipadx']   = 11
        _dParams['pady']    = 11
        _dParams['sticky']  = W + N
        # Prepare labels
        _lTitre             = Label(self, text = 'Junia QCM', font = ("Times New Roman (Titres CS)", 40))
        _lsousTitre         = Label(self, text = 'Consigne', font = ("Times New Roman (Titres CS)", 30))		
        _lcalcu             = Label(self, text = 'Calculatrice autorisée ?: ')
        _ldoc               = Label(self, text = 'Documents autorisés ?: ')
        _lbonpoint          = Label(self, text = 'Pts bonne rep /Pts mauvaise rep(ex: 3/-1): ')
        _lautre             = Label(self, text = 'Autres consignes :')
		                        #_lmauvaispoint      = Label(self, text = 'Pts/mauvaises reponses: ')


        # Prepare edits
        _ecao                = Radiobutton (self, text = "Oui",variable=self.opt_selected ,value="1")
        _ecan                = Radiobutton (self, text = "Non",variable=self.opt_selected ,value="0")
        _edoco               = Radiobutton (self, text = "Oui",variable=self.opt1_selected ,value="1")
        _edocn               = Radiobutton (self, text = "Non",variable=self.opt1_selected ,value="0")
        _ebonPoint           = Entry(self, textvariable = self.bonpoint)
        _eautre               = Entry(self, textvariable = self.autre)
        

       
        #

        _bSuivant           = Button(self, text = 'Suivant',
                                     command = self.executionBoutonSuivant)

        # Position elements
        _lTitre.grid(row = 0, column = 1, **_dParams)
        _lsousTitre.grid(row = 3, column = 1, **_dParams)

        _lcalcu.grid(row = 4, column = 0, **_dParams)
        _ldoc.grid(row = 5, column = 0, **_dParams)
        _lbonpoint.grid(row = 6, column = 0, **_dParams)
        _lautre.grid(row = 7 , column = 0,**_dParams)
        _ebonPoint.grid(row = 6 , column = 1,**_dParams)
        #_lmauvaispoint.grid(row = 9, column = 0,**_dParams)
        #_emauvaisPoint.grid(row = 9 , column = 1,**_dParams)

        #

        _ecao.grid(row = 4 , column = 1,**_dParams)
        _ecan.grid(row = 4 , column = 1,pady = 10 ,ipadx = 10)
        _edoco.grid(row = 5 , column = 1,**_dParams)
        _edocn.grid(row = 5 , column = 1,pady = 10 ,ipadx = 10)

        self.autre.grid(row = 7 , column = 1,padx = 11, pady = 10 )
		
       #
        _bSuivant.grid(row = 8, column = 1, **_dParams)
        #
        

		
    def executionBoutonSuivant(self):
        #print( "Le nom du questionnaire est :  " + self.nomQuestionnaire.get() )
        #print( "Le nom du professeur est :  " + self.nomProfesseur.get() )
        #print( "Le Niveau :  " + self.nNiveau.get() )
        #print( "Le nombre de questions est : ", self.numQuestions.get())
        #print( "La date du QCM est : " , self.cCalendrier.get_date())
        #print( "L'heur de départ est : ", self.tDepart.get())
        #print( "La durée du QCM est : ", self.tDuree.get())
        if (self.bonpoint.get()[1]!='/'):
                messagebox.showerror(title="Mauvaise syntaxe", message="Suivez bien la syntaxe x/y ou x les le nombre de points par bonne reponse , et y le nobre de points par mauvaise reponse")
                self.suivant = False
        else:
            self.store['label-text']=self.autre.get(1.0, END) 
            self.suivant = True
            self.destroy()
            
            
    
    

        



									 
						  
					  