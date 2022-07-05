from pdf2image import convert_from_path
import os
#os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import json
import numpy as np
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
# import argparse
import imutils
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import easyocr 
from PIL import ImageFilter
from correctionLatex import *
import os
from thefuzz import fuzz
relative_path = os.getcwd()
DOSSIERLOCAL = f"{relative_path}\copies"

NOMBRE_PAGES_ETUDIANT = -1
NOMBRE_PAGES = -1
NOMBRE_QUESTIONS = -1
QUESTIONS = -1
PROFESSEUR = ""
MATIERE = ""
DATE_EXAMEN = ""
NIVEAU = ""




def charger_reponses(path):
    global relative_path
    """
    Convert the images from the path to a list of images. Save the images in the local directory.
    @param path - the path to the images
    @return the number of pages
    """
    images = convert_from_path(path)
    nombreDePages = len(images)
    for i in range(nombreDePages):
        if(i%2 == 0):
            images[i].save(f"{relative_path}/pages{str(int(i/2))}.jpg", 'JPEG')
    return nombreDePages







def charger_quesionnaire(path):
    """
    Load the questionnaire from the json file.
    @param path - the path to the json file
    @return the questionnaire
    """
    with open(path, "r") as Read_file:
        fichierlu =json.load(Read_file)
        #print(fichierlu)
    return fichierlu['Informations']['point'] , fichierlu['Informations']['NbrQuestions'], fichierlu['Informations']['nomQuestionnaire'], fichierlu['Informations']['nomProfesseur'], fichierlu['Informations']['nNiveau'] ,fichierlu['Informations']['tDate'] ,fichierlu['Question']

 
    



def notation(notation):
    notation = notation.split("/")
    return(int(notation[0]), int(notation[1]))




def nombre_pages_etudiant(nombre_questions):
    """
    Given the number of questions, return the number of pages per student.
    @param nombre_questions - the number of questions           
    @return the number of pages per student         
    """
    return int(np.ceil(nombre_questions/7))








def getKey(tuples):
    return tuples[1]

def extraire_informations_sans_identifiant(image):
    """
    Take the input image and extract the information without the identifier.
    @param image - the image to be processed
    @return The information without the identifier
    """
    Rep = []
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edged = cv2.Canny(image, 75, 200)
    thresh = cv2.threshold(blurred, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    # find the contours in the thresholded image, then initialize
     # the list of contours that match the questions
     # find the contours in the thresholded image, then initialize
     # the list of contours that match the questions
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    questionCnts = []
    LA=[] 
    # loop on contours
    for c in cnts:
    # calculate the bounding box of the contour, then use the
    # bounding box to derive aspect ratio
        (x, y, w, h) = cv2.boundingRect(c)
        ar = w / float(h)

    #     cv2.rectangle(paper,(x,y),(x+w,y+h),(0,255,0),2)
    #     res = cv2.drawContours(warped, [c], -1, (255, 0, 25), 1)
    #     cv2.imwrite("contours_or.png", paper)


          # in order to label the outline as a question, region
          # must be wide enough, high enough and
          # have an aspect ratio of approximately 1
        if  ar >= 4 and ar <= 4.5 :
            #ar >= 0.5 and ar <= 2:#w >= 8 and h >= 8 and
            LA.append((x, y, w, h))
            #cv2.imwrite("contours_or.png", image)
            questionCnts.append(c) 
    LA=sorted(LA, key = getKey)
    # find the contours in the thresholded image, then initialize
    # the list of contours that match the questions
    z=dict() 
    j=0
    for i in LA:
        j=j+1
        threshb=thresh[i[1]:,i[0]+140:][int(i[3]/2):i[3],:i[2]-150]
        thresha=thresh[i[1]:,i[0]+140:][:int(i[3]/2),:i[2]-150]


        cntsa = cv2.findContours(thresha.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cntsa = imutils.grab_contours(cntsa)
        cntsb = cv2.findContours(threshb.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        cntsb = imutils.grab_contours(cntsb)    
        questiona = []
        questionb = []

    # loop on contours
        for c in cntsa:
        # calculate the bounding box of the contour, then use the
              # bounding box to derive aspect ratio
            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)
            if  w >= 8 and h >= 8 and ar >= 0.5 and ar <= 2:
                
                (x, y, w, h) = cv2.boundingRect(c)
                #LA.append((x, y, w, h))
                #res = cv2.drawContours(image, [c], -1, (255, 0, 255), 2)
                #cv2.imwrite("contours_or.png", image)
                questiona.append(c)

        for c in cntsb:

            (x, y, w, h) = cv2.boundingRect(c)
            ar = w / float(h)
            if  w >= 8 and h >= 8 and ar >= 0.5 and ar <= 2:
                #:#
                (x, y, w, h) = cv2.boundingRect(c)
                #LA.append((x, y, w, h))
                #res = cv2.drawContours(image, [c], -1, (255, 0, 255), 2)
                #cv2.imwrite("contours_or.png", image)
                questionb.append(c)
        questionb=contours.sort_contours(questionb,method="left-to-right")[0]
        questiona=contours.sort_contours(questiona,method="left-to-right")[0]
        #print(len(questionb))
        z[j]=[questiona,questionb]     
        cna = contours.sort_contours(z[j][0],method="left-to-right")[0]
        bubbled = None
        L=list()
        for (e, d) in enumerate(cna):
            if e%2 ==1:
                mask = np.zeros(thresha.shape, dtype="uint8")
                cv2.drawContours(mask, [d], -1, 255, -1)
                mask = cv2.bitwise_and(thresha, thresha, mask=mask)
                #plt.imshow(mask,cmap="gray")
                #plt.show()
                total = cv2.countNonZero(mask)
                #print((total,e))
                if  total > 285:
                    if  e==1:
                        L.append('A')
                    if  e==3 :
                        L.append('B')
                    if  e==5 :
                        L.append('C')
                    if  e==7:
                        L.append('D')
                    L=list(dict.fromkeys(L))    
                    #bubbled = (total, j)

        cnb = contours.sort_contours(z[j][1], method="left-to-right")[0]
        #bubbled = None
        Lb=list()
        for (f, g) in enumerate(cnb):
            if f%2 ==1:
                mask = np.zeros(threshb.shape, dtype="uint8")
                cv2.drawContours(mask, [g], -1, 255, -1)
                mask = cv2.bitwise_and(threshb, threshb, mask=mask)
                
                #plt.imshow(mask,cmap="gray")
                #plt.show()
                total = cv2.countNonZero(mask)
                #print((total,f))    
                if  total > 285:
                    if  f==1:
                        Lb.append('A')
                    if  f==3 :
                        Lb.append('B')
                    if  f==5 :
                        Lb.append('C')
                    if  f==7:
                        Lb.append('D')
                    #L=list(dict.fromkeys(L))    
                    #bubbled = (total, j)
        Rep.append([L,Lb])       
    return Rep



def extraire_informations_avec_identifiant(image,NIVEAU):
    """
    Take the input image and extract the information from it.
    @param image - the image to extract the information from
    @return the information extracted from the image
    """
    #cv2.imshow("Fenetre", image)
    #cv2.waitKey()
    image0 = image[280:500,1000:]
    image0 = cv2.GaussianBlur(image0, (5, 5), 0)
    image0 =  cv2.threshold(image0, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    reader = easyocr.Reader(['en'])
    bounds = reader.readtext(image0, allowlist = '0123456789')
    image1 = image[380:,:]
    bounds=bounds[1][1]
    print(type(bounds),bounds)
    liste_etudiants = pd.read_excel (f"{relative_path}\copies\{NIVEAU}.xlsx")
    liste_id_etu=liste_etudiants["ID"]
    Max= max([fuzz.ratio(bounds,str(i)) for i in liste_id_etu])
    bounds=[i for i in liste_id_etu if fuzz.ratio(bounds,str(i)) ==Max][0]
    return [bounds] + extraire_informations_sans_identifiant(image1)

    

def extraire_reponses_etudiant(n,nbr_pages,NIVEAU):
    global relative_path
    print(relative_path)
    path = f"{relative_path}\copies\pages" + str(nbr_pages*n) + ".jpg"
    print(path)
    image = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
    
    reponses = extraire_informations_avec_identifiant(image,NIVEAU)
    print(reponses[0])
    for i in range(nbr_pages*n + 1 , (n+1)*nbr_pages):
        path = f"{relative_path}\copies\pages" + str(i) + ".jpg"
        print(path)
        image = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        reponses = reponses + extraire_informations_sans_identifiant(image)
    return reponses



    
    
def corriger_question(reponse,question):
    """
    Take the input question and compare it to the dictionary of questions and answers.
    For any matching questions, grab the answer.
    @param reponse - the user's response
    @param question - the question itself
    @return The answer to the question
    """
    question = question  #remettre question[i][-1]
    question = [question]
    #print(question)
    return corriger(question,reponse,1)


def corriger(reponse, question, i):
    """
    This function is used to correct the answers given by the user. It is used to correct the answers given by the user.
    @param reponse - the answers given by the user.
    @param question - the questions given by the user.
    @param i - the index of the question.
    @returns the corrected answers.
    """
    nbr_reponses = len(reponse[i])
    #print("bonne reponse",question, "- reponse etudiant",reponse)
    if nbr_reponses == 4:
        #print("reponse retenue",reponse[i])
        return (0,reponse,question)
    elif nbr_reponses != 0:
        #print("bonne reponse ",question, "- reponse etudiant",reponse[i])
        #print("reponse retenue", reponse[i])
        return (3,reponse,question) if reponse[i]==question else (-1,reponse,question)
    else:
        if i == 1:
            #print("reponse retenue",reponse[i])
            return corriger(reponse, question, 0)
        else:
            #print("reponse retenue",reponse[i])
            return (0,reponse,question)
        
        

def corriger_copie(copie, bonne_reponse):
    """
    Take the copy of the answers and the correct answers and compare them. For each answer,
    compare it to the correct answer. If it is correct, add 1 to the note.
    @param copie - the copy of the answers           
    @param bonne_reponse - the correct answers           
    @return The note and the grid of the answers           
    """
    grille = []
    note = 0
    for i in range(1,len(copie)):
        grille.append(corriger(copie[i],[bonne_reponse[i]],1))
        note += grille[i-1][0]
    return [copie[0],note,grille]


import pandas as pd


#print (liste_etudiants)






from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib

from email.mime.base import MIMEBase
from email import encoders

import os


def statistiques(notes):
    """
    Given a list of notes, return the min, max, mean.
    @param notes - the list of notes
    @returns the min, max, mean
    """
    return (np.min(notes),np.max(notes), round(np.mean(notes)),2)




import smtplib, ssl





def EnvoyerMail(NOMBRE_ETUDIANTS,copiesEtudiants,NOTATION,STATISTIQUES,MATIERE,NOMBRE_QUESTIONS):
    """
    Send an email to the receiver with the results of the test.
    @param NOMBRE_ETUDIANTS - the number of students in the test.
    @param copiesEtudiants - the list of students' answers.
    @param NOTATION - the notation of the test.
    @param STATISTIQUES - the statistics of the test.
    @param MATIERE - the subject of the test.
    @param NOMBRE_QUESTIONS - the number of questions in the test.
    """
    port=587 # For SSL
    smtp_server = "smtp.office365.com"
    sender_email = "qcm_junia_maroc@outlook.com"#"simpleattempt001234@hotmail.com"##"maliokinew@gmail.com" # Enter your address
    password = "JuniaMaroc2022&"#'gTWR_iG2RNW7_R!'#
    for i in range(NOMBRE_ETUDIANTS):
        copie = copiesEtudiants[i]
        if (len(copie) == 7):
            identifiant = copie[0]
            note = copie[1]
            grille = copie[2]
            mail = copie[3]
            prenom = copie[4]
            nom = copie[5]
            gender = copie[6]
        genererCorrectionEtudiant(identifiant,note,grille, NOTATION, nom, prenom, STATISTIQUES,NOMBRE_QUESTIONS)
        message = MIMEMultipart("alternative")
        message["Subject"] = "Note - " + MATIERE.upper()
        message["From"] = sender_email
        #message["To"] = liste_etudiants["Mail"][i]
        #print(message["To"] , liste_etudiants["Mail"][i])
        receiver_email = mail # Enter receiver address
        # Create the plain-text and HTML version of your message
        #text = "Bonjour,\n Votre note est:" + str(liste_etudiants["Note"][4]) + "/60.\nBonne reception."
        print(gender + " " + prenom + " " + nom)
        m=MATIERE.lower()
        note_m=str(round(STATISTIQUES[2],2))
        Total=NOMBRE_QUESTIONS*NOTATION[0]
        html = f"""\
        <html>
        <body>
            <p>Bonjour  {gender + " " + prenom + " " + nom.upper()},</p>
            <p>
            <br>Votre note en {m} est <b> {note}/{Total} </b> <br>
            </p>
            <p> La note maximale de la classe : <b> {str(STATISTIQUES[0])} </b> </p>
            <p> La note minimale de la classe : <b> {str(STATISTIQUES[1])} </b> </p>
            <p> La note moyenne de la classe : <b> {note_m} </b> </p>
            <p>Vous trouverez ci joint les documents relatives à votre evaluation  </p>
            <p>Bien cordialement</p>
        </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        #part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        #message.attach(part1)
        file_name1 = DOSSIERLOCAL +"\\"+nom + '.pdf'
        nom_fichier = nom + '.pdf'
        message.attach(part2)
        
        with open(file_name1, 'rb') as attachment:
            file_part1 = MIMEBase('application', 'octet-stream')
            file_part1.set_payload(attachment.read())
            encoders.encode_base64(file_part1)
            file_part1.add_header(
            'Content-Disposition',
            'attachment; filename =' + str(nom_fichier)
            )
        message.attach(file_part1)

        nom_fichier = "Enonce.pdf"
        file_name2 = f"{relative_path}\QCM_app1\Enonce.pdf"
        message.attach(part2)
        
        with open(file_name2, 'rb') as attachment:
            file_part2 = MIMEBase('application', 'octet-stream')
            file_part2.set_payload(attachment.read())
            encoders.encode_base64(file_part2)
            file_part2.add_header(
            'Content-Disposition',
            'attachment; filename =' + str(nom_fichier)
            )
        message.attach(file_part2)


        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.set_debuglevel(1)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit
            



