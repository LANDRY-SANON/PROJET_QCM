"""
Created on Tue Feb  8 18:47:59 2022

@author: Hatim NAQOS
"""
import sys
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import Image, ImageTk
from tkcalendar import Calendar
from correction import *
from styleApp import FgColor, BgColor
import os
from PIL import Image,ImageTk

from correctionLatex import *
#import Application.window

relative_path = os.getcwd()    
class fenetreCorrection(Tk):
    """
    Create the GUI for the correction.
    """

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
        _sStyle.configure('TLabel',
                          foreground = FgColor(),
                          background = BgColor(),
                          font = ('Times New Roman (Titres CS)', 12, 'bold'))
        
        
    def browseFilespdf(self):
        """
        Browse for a PDF file. 
        @returns the filename of the PDF file
        """
        self.filenamepdf = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("Text files",
                                                            "*.pdf*"),
                                                           ("all files",
                                                            "*.*")))

    def browseFilesjson(self):
        """
        Browse for a json file.
        @returns the filename of the json file
        """
        self.filenamejson = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.json*"),
                                                       ("all files",
                                                        "*.*")))
        try:
            NOTATION, NOMBRE_QUESTIONS, MATIERE, PROFESSEUR, NIVEAU, DATE_EXAMEN ,QUESTIONS = charger_quesionnaire(self.filenamejson)
        except:
            messagebox.showwarning(title="Erreur", message="Veuillez choisir un fichier valid!")
        
        self._matiere.config(text = "Matière: " + MATIERE)
        self._prof.config(text = "Professeur: " + PROFESSEUR)
        self._niveau.config(text = "Niveau: " + NIVEAU)
        self._date.config(text = "Date: " + DATE_EXAMEN)
    global store
    store = dict()


    
    def __init__(self):
        Tk.__init__(self)


        # Prepare the window
        self.filenamepdf      = StringVar()
        self.filenamejson     = StringVar()
        #self.minsize(1023,810)
        self.geometry('1080x710')
        self.configure(bg = "#261934")
        self.title('Junia Maroc [QCM]')
        self.applyStyle()
        self.suivant = False
        self. filenamepdf	= StringVar()
        # Fixate parameters
        _dParams            = dict()
        _dParams['padx']    = 11
        _dParams['ipadx']   = 11
        _dParams['pady']    = 11
        _dParams['sticky']  = W + N
        # Prepare labels
        _lTitre             = Label(self, text = 'Junia QCM', font = ("Times New Roman (Titres CS)", 40))
        _lsousTitre         = Label(self, text = 'Correction', font = ("Times New Roman (Titres CS)", 30))		
        _fichierpdf         = Label(self, text = 'Fichier pdf: ')
        _fichierjson        = Label(self, text = 'Fichier json: ')
        
        self._matiere            = Label(self, text = 'Matière: ')
        self._prof               = Label(self, text = 'Professeur: ')
        self._niveau             = Label(self, text = 'Niveau: ')
        self._date               = Label(self, text = 'Date: ')
        
        _Style = ttk.Style(self)
        _Style.configure("TProgressbar", foreground='#993822', background='#993822')
        
        self.progress            = Progressbar(self,style = "TProgressbar",orient = HORIZONTAL, length = 400, mode = 'determinate') 
		                        #_lmauvaispoint      = Label(self, text = 'Pts/mauvaises reponses: ')
        

        # Prepare edits

        

       
        #

        _bSuivant           = Button(self, text = 'Corriger',
                                     command = self.executionBoutonSuivant)
        
        self._bPrecedent           = Button(self, text = 'Précédent',
                                     command = self.executionBoutonPrecedent)

        # Position elements
        _lTitre.grid(row = 0, column = 3, **_dParams)
        _lsousTitre.grid(row = 3, column = 1, **_dParams)
        explore_pdf = Button(self,
                        text = "Explorer",
                        command = self.browseFilespdf)
        explore_json = Button(self,
                        text = "Explorer",
                        command = self.browseFilesjson)
        #_lmauvaispoint.grid(row = 9, column = 0,**_dParams)
        #_emauvaisPoint.grid(row = 9 , column = 1,**_dParams)

        #

        explore_pdf.grid(row = 11, column = 2, **_dParams)
        explore_json.grid(row = 5, column = 2, **_dParams)
        _fichierpdf.grid(row = 11, column = 1, **_dParams)
        _fichierjson.grid(row = 5, column = 1, **_dParams)
        self.progress.grid(row = 13,column = 3)
        self._matiere.grid(row = 6,column = 3,**_dParams)
        self._niveau.grid(row = 7, column = 3, **_dParams)
        self._prof.grid(row = 6, column = 1, **_dParams)
        self._date.grid(row = 7, column = 1, **_dParams)
       #
        _bSuivant.grid(row = 12, column = 2, **_dParams)
        self._bPrecedent.grid(row = 12, column = 1, **_dParams)
        #
        
    def executionBoutonPrecedent(self):
        #self.Precedent = True
        
        self._bPrecedent.configure(state= NORMAL)
        self.destroy()
        a=os.getcwd()
        a=a[:-12]
        sys.path.append(a)
        print(a)
        from QCM_app import fenetreMenu
        fenetreMenu().mainloop()  
        
        
    def executionBoutonSuivant(self):
        #print( "Le nom du questionnaire est :  " + self.nomQuestionnaire.get() )
        #print( "Le nom du professeur est :  " + self.nomProfesseur.get() )
        #print( "Le Niveau :  " + self.nNiveau.get() )
        #print( "Le nombre de questions est : ", self.numQuestions.get())
        #print( "La date du QCM est : " , self.cCalendrier.getself._date())
        #print( "L'heur de départ est : ", self.tDepart.get())
        #print( "La durée du QCM est : ", self.tDuree.get())
        print("PDF: ",self.filenamepdf)
        print("JSON:", self.filenamejson)
        
        NOMBRE_PAGES = charger_reponses(self.filenamepdf)
        self.progress["value"] = 10
        self.update_idletasks()
        NOMBRE_PAGES = int(NOMBRE_PAGES/2)
        print(NOMBRE_PAGES)
        NOTATION, NOMBRE_QUESTIONS, MATIERE, PROFESSEUR, NIVEAU, DATE_EXAMEN ,QUESTIONS = charger_quesionnaire(self.filenamejson)
        NOTATION = notation(NOTATION)
        print(NOTATION)
        NOMBRE_PAGES_ETUDIANT = nombre_pages_etudiant(NOMBRE_QUESTIONS)
        NOMBRE_ETUDIANTS = int(NOMBRE_PAGES/NOMBRE_PAGES_ETUDIANT)
        print("DOSSIERLOCAL = " + DOSSIERLOCAL)
        print("NOMBRE_PAGES_ETUDIANT = " +  str(NOMBRE_PAGES_ETUDIANT))
        print("NOMBRE_ETUDIANTS = ", NOMBRE_ETUDIANTS)
        print("NOMBRE_PAGES = " + str(NOMBRE_PAGES))
        print("NOMBRE_QUESTIONS = " + str(NOMBRE_QUESTIONS))
        print("MATIERE = " + MATIERE)
        print("PROFESSEUR = " + PROFESSEUR)
        print("DATE_EXAMEN = " + DATE_EXAMEN)
        print("NIVEAU = " + NIVEAU)
        #print("QUESTIONS = " , QUESTIONS)
        BONNES_REPONSES = []
        BONNES_REPONSES.append("bonnes reponses")
        for question in QUESTIONS:
            BONNES_REPONSES.append(question[-1])
        print(BONNES_REPONSES)
        liste_etudiants = pd.read_excel (f"{relative_path}\copies\{NIVEAU}.xlsx")
        copiesEtudiants = []
        self.progress["value"] = 20
        self.update_idletasks()
        
        for i in range(NOMBRE_ETUDIANTS):
            Copie_corrigé = extraire_reponses_etudiant(i,NOMBRE_PAGES_ETUDIANT,NIVEAU)
            Copie_corrigé = corriger_copie(Copie_corrigé, BONNES_REPONSES)
            #print(Copie_corrigé)
            #copiesEtudiants.append(Copie_corrigé)
            #print(f"Etudiant{i} :",corriger_copie(Copie_corrigé))
            
            for k in range(len(liste_etudiants["ID"])):
                
                #print("Copie_corrigé[0] =", Copie_corrigé[0],"type:",type(Copie_corrigé[0]))
                #print("liste_etudiants[k] =", liste_etudiants["ID"][k],"type:",type(liste_etudiants["ID"][k]))
                if str(Copie_corrigé[0]) == str(liste_etudiants["ID"][k]):
                    
                    liste_etudiants["Note"][k] = Copie_corrigé[1]
                    Copie_corrigé.append(liste_etudiants["Mail"][k])
                    Copie_corrigé.append(liste_etudiants["Prenom"][k])
                    Copie_corrigé.append(liste_etudiants["Nom"][k])
                    Copie_corrigé.append(liste_etudiants["M-Mme"][k])
                    #print("OUI")
                    break
            copiesEtudiants.append(Copie_corrigé)
        self.progress["value"] = 40
        print("liste_etudiants", liste_etudiants)
        print("copie_etudiants[0]", copiesEtudiants)
        liste_etudiants.pop("Mail")
        liste_etudiants.pop("M-Mme")
        
        liste_etudiants.to_excel(f"{relative_path}\copies\{MATIERE}_{NIVEAU}.xlsx")
        os.startfile(f"{relative_path}\copies\{MATIERE}_{NIVEAU}.xlsx")
        STATISTIQUES = statistiques(liste_etudiants["Note"])
        
        print(STATISTIQUES)
        self.progress["value"] = 60
        self.update_idletasks()
        EnvoyerMail(NOMBRE_ETUDIANTS,copiesEtudiants,NOTATION,STATISTIQUES,MATIERE,NOMBRE_QUESTIONS)
        self.progress["value"] = 100
        self.update_idletasks()
        
        self.suivant = True
        """
        for i in range(NOMBRE_ETUDIANTS):
            #print("tppp",copiesEtudiants[i])
            genererCorrectionEtudiant(copiesEtudiants[i][0],
                                      copiesEtudiants[i][1],
                                      copiesEtudiants[i][2],
                                      NOTATION,
                                      copiesEtudiants[i][5],
                                      copiesEtudiants[i][4],
                                      STATISTIQUES,
                                      NOMBRE_QUESTIONS)"""

       	
			
    

        



									 
						  
					  