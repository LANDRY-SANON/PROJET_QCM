from tk_html_widgets import HTMLLabel


import sys
import os

#import QCM_app

from tkinter import *
from tkinter.ttk import *
from tkinter import ttk

from PIL import Image, ImageTk


sys.path.append('QCM_app2')
from styleApp import FgColor, BgColor
import webbrowser



#from tkhtmlview import HTMLLabel
#from PIL import Image,ImageTk
#import  Application 

description= '''

<h3 style="color:white;">Développée en 2022 , cette application s’inscrie dans le cadre de notre projet <br>de fin d'année ( 1ère année de cycle ingénieur et  témoigne d'une belle collaboration au sein de notre équipe accompagnée et encadrée par nos professeurs à JUNIA-Maroc .</h3>

'''

html_text = '''

<div>

                <div ><img src="./QCM_app2/CV_YNCREA.jpg" >
                <div >
                <a href="https://www.linkedin.com/in/landry-s-763638197/">
                <div>
                      <h4 style="color:gold2; font-size: 10px">SANON Landry</h4>
                    </a></div>
                    <div>
					<h6 style="color:gold;">Elève ingénieur à ISEN   </h6></div>
                </div>
                </div>
                

	
		    

		    
		</div>
'''

html_text_a = '''


        <div>

                <div ><img src="./QCM_app2/mt_photo.jpeg" >
                <div >
                <a href="https://www.linkedin.com/in/landry-s-763638197/">
                <div>
                      <h4 style="color:gold2; font-size: 10px;width:50px ">Mehdi TALIB</h4>
                    </a></div>
					<h6 style="color:gold">Elève ingénieur à ISEN    </h6>
                </div>
                </div>
                

	
		    

		    
		</div>
'''

html_text_b = '''


        <div>

                <div ><img src="./QCM_app2/Ab.jpg" >
                <div >
                <a href="https://www.linkedin.com/in/landry-s-763638197/">
                <div>
                      <h4 style="color:gold2; font-size: 10px;width:50px "> TALHA Abir</h4>
                    </a></div>
					<h6 style="color:gold">Elève ingénieur à ISEN   </h6>
                </div>
                </div>
                

	
		    

		    
		</div>
'''
# create HTMLLabel



def callback(url):
    """
    Open the url in the default browser.
    @param url - the url to open
    """
    webbrowser.open_new_tab(url)


class fenetreAboutUS(Tk):
    """
    This class allows to define the window about us
    @param self - the object itself.
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
        Tk.__init__(self)

 
        # Prepare the windo
        #self.minsize(1023,810)
        

        self.geometry('1080x710')
        self.configure(bg = "#261934")
        self.title('About Us [QCM]' )
        self.applyStyle()
        self.suivant = False
        # Fixate parameters
        _dParams            = dict()
        _dParams['padx']    = 11
        _dParams['ipadx']   = 11
        _dParams['pady']    = 11
        _dParams['sticky']  = W + N
        
        self._bPrecedent           = Button(self, text = 'Précédent',
                                     command = self.executionBoutonPrecedent)
        # Prepare labels
        #_lTitre             = Label(self, text = 'JUNIA QCM', font = ("lato", 40,"bold"))

		                        #_lmauvaispoint      = Label(self, text = 'Pts/mauvaises reponses: ')


        # Prepare edits
        

       
        #

        
        # Position elements
        #_lTitre.grid(row = 0, column = 3, **_dParams)
        #_lmauvaispoint.grid(row = 9, column = 0,**_dParams)
        #_emauvaisPoint.grid(row = 9 , column = 1,**_dParams)

        #
        self.image=Image.open('./QCM_app2/JUNIA1.png')

		

     
        self.pyimage=ImageTk.PhotoImage(self.image)
        label_d = HTMLLabel(self, html=description,background='#261934',padx=58,height=10)
        self.label = HTMLLabel(self, html=html_text,background='#261934')
        self.label_a = HTMLLabel(self, html=html_text_a,background='#261934')
        self.label_b = HTMLLabel(self, html=html_text_b,background='#261934')
        


        self.n1 =Label(self, text="SANON Landry")
		
        self.li1 =Label(self, text="https://www.linkedin.com/")
        #self.linkedin.bind("<Button-1>", lambda e: callback("https://www.linkedin.com/in/landry-s-763638197/"))
        self._bPrecedent.place(x= 100, y = 20)
        ttk.Label(self,image=self.pyimage).place(x= 320, y = 0)
        label_d.place(x= 150, y = 230)
        self.label.place(x= 100, y = 335)
        self.label_a.place(x= 430, y = 335)
        self.label_b.place(x= 750, y = 335)
				
  
		
		
        
    def executionBoutonPrecedent(self):
        """
        When the user clicks the previous button, destroy the current window and go back to the menu.
        @param self - the current window.
        """
        self.Precedent =False
        
        self._bPrecedent.configure(state= NORMAL)
        self.destroy()
        from QCM_app import fenetreMenu
        fenetreMenu().mainloop() 
#window_a=window
        #window_a.mainloop()
        #import Application
        #self.destroy()
        #global p

        #window = fenetreMenu()
        #window_a.mainloop()
        

        
        
            

               
          
 
        

