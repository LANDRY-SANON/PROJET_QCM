# -*- coding: utf-8 -*-
"""
Created on Mon May 16 00:09:06 2022

@author: Landry SANON 
"""



from pylatex import Document, Section, Itemize, Enumerate, Description, \
    Command, NoEscape
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
from pylatex.package import Package
from pylatex import Document, Section, UnsafeCommand
from pylatex.base_classes import Environment, CommandBase, Arguments
import os




#informations = {"NbrQuestions" : 30 , 
#                "nomQuestionnaire" : "Algo/C",
#                "nomProfesseur" : "D. HDAFA",
#                "nNiveau" : "JMA3",
#                "tDepart" : "",
#                "tDuree" : "3h 00min"}

relative_path = os.getcwd()     
note = -1
rep = [['C'] , ['D']]
bonneRep = ['A']
numQuestion = 1





def genererCorrectionsQCMQuestion(doc , note , rep, bonneRep, numQuestion):
    """
    Generate the correction for a question.
    @param doc - the document we are generating the correction for.
    @param note - the note for the question.
    @param rep - the reponse for the question.
    @param bonneRep - the correct answer for the question.
    @param numQuestion - the number of the question.
    """

    if (note > 0):
        validation = True
    else:
        validation = False
    
    bonneRep = ord(bonneRep[0]) - 65
    for i in range(len(rep)):
        for j in range(len(rep[i])):
            rep[i][j] = ord(rep[i][j]) - 65
    doc.append(NoEscape("\\thispagestyle{empty}"))
    doc.append(NoEscape("\\begin{center}"))
    doc.append(NoEscape("\\begin{tabular}{| l  l  l  l  l |}"))
    doc.append(NoEscape("\\hline"))
    doc.append(NoEscape(" & & & & \\\\"))
    text = ""
    doc.append(NoEscape("Question " + str(numQuestion) + "\\qquad \qquad\\ & & & & \\\\"))
    text = ""
    for j in range(4):
        trouve = False
        if (j == bonneRep) :
            text = text + '& ' + chr(j + 65) + ' \\textcolor{green}{$\\qquad \\blacksquare \\qquad$}'
            trouve = True
        else:
                for l in range(len(rep[0])):
                    if(j == rep[0][l]):
                        text = text + '& ' + chr(j + 65) + ' \\textcolor{red}{$\\qquad \\blacksquare \\qquad$}'
                        trouve = True
        if(trouve == False):
            text = text + '& ' + chr(j + 65) + ' $\\qquad \\square \\qquad$'
    text = text + '\\\\' 
    doc.append(NoEscape(text))
    doc.append(NoEscape(" & & & & \\\\"))
    doc.append(NoEscape("\\hline" ))
    doc.append(NoEscape(" & & & &  \\\\"))
    text = "Choix 2"
    for j in range(4):
        trouve = False
        if (j == bonneRep) :
            text = text + '& ' + chr(j + 65) + ' \\textcolor{green}{$\\qquad \\blacksquare \\qquad$}'
            trouve = True
        else:
                for l in range(len(rep[1])):
                    if(j == rep[1][l]):
                        text = text + '& ' + chr(j + 65) + ' \\textcolor{red}{$\\qquad \\blacksquare \\qquad$}'
                        trouve = True
        if(trouve == False):
            text = text + '& ' + chr(j + 65) + ' $\\qquad \\square \\qquad$'
    text = text + '\\\\'
    doc.append(NoEscape(text))
    doc.append(NoEscape(" & & & &  \\\\"))
    doc.append(NoEscape("\\hline"))
    doc.append(NoEscape("\\end{tabular}"))
    text = " \\qquad  "
    if (validation == True):
        text = text + "\\textcolor{green}{+" + str(note) + "}"
    else:
        text = text + "\\textcolor{red}{" + str(note) + "}"
    doc.append(NoEscape(text))    
    doc.append(NoEscape("\\\\ \\vskip3mm"))
    doc.append(NoEscape("\\end{center}"))

                   
    
    

#genererCorrectionsQCMQuestion(note , rep, bonneRep, numQuestion)



def genererCorrectionEtudiant(ID, note, reponsesEtudiant, notation, nom, prenom, statistiques,NOMBRE_QUESTIONS):
    """
    Generate the corrected copy of a student.
    @param ID - the student's ID.
    @param note - the student's note.
    @param reponsesEtudiant - the student's answers.
    @param notation - the student's notation.
    @param nom - the student's last name.
    @param prenom - the student's first name.
    @param statistiques - the student's statistics.
    @param NOMBRE_QUESTIONS - the number of questions.
    """


    
    identifiant = str(ID)
    noteFinale = note
    details =reponsesEtudiant
    NOMBRE_QUESTIONS = len(details)
    NOTE_MAXIMALE = NOMBRE_QUESTIONS*notation[0]
    
    
    doc = Document(documentclass = 'book')
    doc.packages.append(NoEscape('\\input{structure}'))
    doc.append(NoEscape("\\newpage"))    
    doc.append(NoEscape("\\thispagestyle{empty}"))
    #doc.append(NoEscape("\\begin{flushright}"))
    doc.append(NoEscape("\\begin{tabular}{|l|l|l|l|l|l|l| }"))
    doc.append(NoEscape("\\hline"))
    #doc.append(NoEscape(" & & & & \\\\")) 
    doc.append(NoEscape("Identifiant $\qquad$ & Prenom $\\qquad$ & Nom $\\qquad$ & Note $\\qquad$ & Min $\\qquad$ & Max $\\qquad$ & Moyenne $\\qquad$ \\\\"))
    doc.append(NoEscape("\\hline"))
    doc.append(NoEscape(identifiant +  "&" + prenom + "&" + nom + "&" + str(noteFinale)+ "/" + str(NOTE_MAXIMALE)  + "&" + str(statistiques[0])+ "/" + str(NOTE_MAXIMALE) + " &" + str(statistiques[1])+ "/" + str(NOTE_MAXIMALE) + " & " + str(statistiques[2])+ "/" + str(NOTE_MAXIMALE)  + "\\\\"))
    doc.append(NoEscape("\\hline"))
    doc.append(NoEscape("\\end{tabular}"))
    #doc.append(NoEscape("\\end{flushright}"))


    
    
    for i in range(NOMBRE_QUESTIONS):
        genererCorrectionsQCMQuestion(doc, details[i][0] , details[i][1], details[i][2], i+1)



    doc.generate_pdf('copies/' + nom, clean_tex=False, compiler='pdfLaTeX')
    #os.startfile(nom + ".pdf")


