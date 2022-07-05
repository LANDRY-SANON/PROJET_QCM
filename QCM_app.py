"""
Created on Tue Feb  8 18:47:59 2022

@author: Landry SANON 
"""
import sys

from test_AboutUS import *
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from ttkwidgets.autocomplete import AutocompleteCombobox
from PIL import Image, ImageTk
sys.path.append('QCM_app1')
from consignes import *
from informationsQCM import *
from questionQCM import *
from latex import *
from enonceLatex import *
sys.path.append('QCM_app2')
from correction import *
from correctionLatex import *
from correction_ui import *
from styleApp import FgColor, BgColor
from PIL import Image,ImageTk

#global 

def nettoayageQuestions(questions):
    """
    Take the questions and clean them up. Remove the newlines and empty strings.
    @param questions - the questions array
    """
    for i in range(len(questions)):
        temp = questions[i][1].split("\n")
        for j in range(len(temp)-1, -1 , -1):
            if(temp[j] == ""):
                temp.pop(j)
        questions[i][1] = temp
        
class fenetreMenu(Tk):
    """
    The menu window for the program. This window is the first window that is displayed.
    It contains the buttons to start the program, and to exit the program.
    @param Tk - the Tkinter module
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

						  
           
		
    
    def __init__(self):
        """
        Initialize the GUI.
        """
        Tk.__init__(self)

 
        # Prepare the window

        self.geometry('1080x710')
        self.configure(bg = "#261934")
        self.title('Junia Maroc [QCM]' )
        self.applyStyle()
        self.suivant = False
        # Fixate parameters
        _dParams            = dict()
        _dParams['padx']    = 11
        _dParams['ipadx']   = 11
        _dParams['pady']    = 11
        _dParams['sticky']  = W + N
        # Prepare labels
        #_lTitre             = Label(self, text = 'JUNIA QCM', font = ("lato", 40,"bold"))

		                        #_lmauvaispoint      = Label(self, text = 'Pts/mauvaises reponses: ')


        # Prepare edits
        

        _bCreer           = Button(self, text = 'Créer un Questionnaire',
                                     command = self.executionBoutonCreer)
        _bCorriger        = Button(self, text = 'Corriger un Questionnaire',
                                     command = self.executionBoutonCorriger)
        _AboutUS          =Button(self, text = 'Qui sommes nous ',
                                     command = self.executionAboutUS)

        # Position elements
        #_lTitre.grid(row = 0, column = 3, **_dParams)
        #_lmauvaispoint.grid(row = 9, column = 0,**_dParams)
        #_emauvaisPoint.grid(row = 9 , column = 1,**_dParams)

        #
        self.image=Image.open('./QCM_app2/JUNIA.png')

        _AboutUS.place(x = 920, y = 0)
        self.pyimage=ImageTk.PhotoImage(self.image)


        
        ttk.Label(self,image=self.pyimage).place(x= 200, y = 50)
        _bCreer.place(x = 200, y = 600)
        
        _bCorriger.place( x=700 , y = 600)

		
    def executionBoutonCreer(self):
            """
            When the user clicks the "Create" button, this function is called. It destroys the current window, and creates a new window with the information from the user.
            The information is stored in a file, and the user is then redirected to the next window.
            @param self - the current window, which is destroyed.
            """
            
            self.suivant = True
            self.destroy()
            window = fenetreInformations()
            window.mainloop()
            if (window.suivant):
                window2 = fenetreConsigne()
                window2.mainloop()	
                if(window2.suivant):
                    informations =  {"nomQuestionnaire" : window.nomQuestionnaire.get() , 
                            "nomProfesseur" : window.nomProfesseur.get() ,
                            "nNiveau" : window.nNiveau.get() ,
                            "tDate" : window.cCalendrier.get_date() ,
                            "tDepart" : window.tDepart.get() , 
                            "point" : window2.bonpoint.get() ,
                            #"autre" : window2.autre.get(1.0, END),
                            "autre" : window2.store['label-text'][:-2],
                            "calculatrice" :window2.opt_selected.get(),
                            "document" :window2.opt1_selected.get(),
                            "tDuree" : window.tDuree.get(),
                            "NbrQuestions" : int(window.NbrQuestions.get())
                            } 
                    if int(informations['tDuree'].split("H")[0])==0:
                        informations['tDuree']=informations['tDuree'].split("H")[1]+" Min"
                    print(informations)
                    nombreQuestions = informations["NbrQuestions"]
            #nomQCM = informations["nomQCM"]


            PageQuestion = questionFenetre(nombreQuestions)
            PageQuestion.mainloop() 
            
            #global questions 
            questions = PageQuestion.bareme
            nettoayageQuestions(questions)


            fileName = informations['nomQuestionnaire'] + ".json"
            jsonObject = {"Informations" : informations, "Question" :questions}
            file = open(fileName, "w")
            json.dump(jsonObject, file)
            file.close()
            
            print(questions)
                    
            
            #print(PageQuestion.suivant)
            
            
            genererQCM(informations, questions)

            genererEnonce(informations, questions)
            
           
    def executionBoutonCorriger(self):
            #print( "Le nom du questionnaire est :  " + self.nomQuestionnaire.get() )
            #print( "Le nom du professeur est :  " + self.nomProfesseur.get() )
            #print( "Le Niveau :  " + self.nNiveau.get() )
            #print( "Le nombre de questions est : ", self.numQuestions.get())
            #print( "La date du QCM est : " , self.cCalendrier.get_date())
            #print( "L'heur de départ est : ", self.tDepart.get())
            #print( "La durée du QCM est : ", self.tDuree.get())
            self.suivant = True
            self.destroy()
            window = fenetreCorrection()
            window.mainloop()
        
			
    def executionAboutUS(self):
        """
        This function is used to display the about us window. It is called when the about us button is pressed.
        """
		#self.f=self
        self.suivant = True
        self.destroy()
        window = fenetreAboutUS()
        window.mainloop()
        #exec(open("AboutUs.py").read())
        """self.suivant = True
       	self.destroy()
        window = fenetreAboutUS()
        window.mainloop()"""
	

   



# create HTMLLabel



