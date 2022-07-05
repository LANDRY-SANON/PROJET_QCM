# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 14:53:15 2022

@author: Landry Sanon
"""
import time

from pylatex import Document, Section, Itemize, Enumerate, Description, \
    Command, NoEscape
from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
from pylatex.package import Package
from pylatex import Document, Section, UnsafeCommand
from pylatex.base_classes import Environment, CommandBase, Arguments
import os


sujet = "Mathématiques"
prof = "H. NAQOS"
duree = "2h 00 min"

#informations = {"NbrQuestions" : 30 , 
#                "nomQuestionnaire" : "Algo/C",
#                "nomProfesseur" : "D. HDAFA",
#                "nNiveau" : "JMA3",
#                "tDepart" : "",
#                "tDuree" : "3h 00min"}


def genererQCM(informations, Questions):
    """
    Generate the questionnaire for the user to fill out.
    @param informations - the informations dictionary
    @param Questions - the questions dictionary
    """
    doc = Document(documentclass = 'book')
    doc.packages.append(NoEscape('\\input{structure}'))
    
    doc.append(NoEscape("\\newpage" ))
    doc.append(NoEscape("\\thispagestyle{empty}"))
    doc.append(NoEscape("\\vskip-40mm	\\includegraphics[scale=0.5]{logo.png} \\\\"))
    doc.append(NoEscape(" \\begin{flushright}  \\vskip-20mm   Professeur " + informations["nomProfesseur"] + "\\vskip15mm  \\end{flushright}"))
    doc.append(NoEscape(informations["nNiveau"]))
    doc.append(NoEscape(" \\begin{flushright}  \\vskip-7mm"+    informations["tDate"] + " \\end{flushright}"))
    doc.append(NoEscape("\\begin{center}   \\begin{Large}" + informations["nomQuestionnaire"].upper() + "\end{Large} \\end{center}"))
    doc.append(NoEscape("Durée : " + informations["tDuree"] ))
    
    
    doc.append(NoEscape(" \\begin{center} { \\large CONSIGNES SPÉCIFIQUES } \\\\ Lisez soigneusement les consignes ci-dessous afin de réussir au mieux cette épreuve : \\end{center} "))
    with doc.create(Itemize()) as item:
        if informations["calculatrice"]==0:
            item.add_item("L'usage de la calculatrice ou de tout autre appareil électronique est interdit.")
        else:
            item.add_item("L'usage de la calculatrice ou de tout autre appareil électronique est autorisé.")
        if informations["document"]==0:
            item.add_item("Aucun autre document que ce sujet et sa grille réponse n'est autorisé.")
        else:
            item.add_item("Documents autorisés.")
        if informations["autre"]!="":
            for i in informations["autre"].split("\n"):
                item.add_item(i)
                
        item.add_item(NoEscape("Pour chacune des questions, indiquez sur la feuille de réponses ci-jointes, si les affirmations A, B, C et D sont (\\textbf{V}) vraies ou (\\textbf{F}) fausses en faisant une croix dans la colonne correspondant à votre choix. Vous ne pouvez pas faire de ratures. En cas d'erreur, utilisez la deuxième colonne de réponse. Si la deuxième colonne comporte au moins une réponse, la première colonne ne sera pas corrigée, c'est la deuxième qui sera prise en considération."))
        item.add_item(NoEscape("Chaque réponse exacte est gratifiée de "+informations["point"][0]+" points, tandis que chaque réponse fausse est pénalisée par "+informations["point"][2:]+" point. \\\\ 	Parmi les quatre propositions de chacune des questions \\textbf{de 1 à "+ str(informations["NbrQuestions"])+ "}, une seule est vraie, les autres sont fausses. ( "+informations["point"][0]+"points par question) \\\\ 	Par exemple : Pour indiquer que l'affirmation $B$ est Vraie, cocher les cases comme suit:  \\\\ \\begin{center}	\\includegraphics[scale=0.8]{reponses.png} \\end{center}"))

        for i in range(informations["NbrQuestions"]):
            doc.append(NoEscape("\\begin{exercise}"))
            for ligne in Questions[i][1]:
                doc.append(NoEscape("\\textbf{" + ligne +  " }"))
            with doc.create(Enumerate(enumeration_symbol=r"\textbf{\Alph*. }"), ) as enum:
                enum.add_item(NoEscape(Questions[i][2]))
                enum.add_item(NoEscape(Questions[i][3]))
                enum.add_item(NoEscape(Questions[i][4]))
                enum.add_item(NoEscape(Questions[i][5]))
            doc.append(NoEscape("\\end{exercise}"))
    doc.append(NoEscape("\\newpage"))
    doc.append(NoEscape("\\thispagestyle{empty}"))
    doc.append(NoEscape("\\begin{flushright}"))
    doc.append(NoEscape("\\begin{tabular}{|l|}"))
    doc.append(NoEscape("\\hline"))
    doc.append(NoEscape(" \\\\"))
    doc.append(NoEscape("Identifiant: $\\qquad \\qquad \\qquad \\qquad \\qquad$ \\\\"))
    doc.append(NoEscape(" \\\\"))
    doc.append(NoEscape("\\hline"))
    doc.append(NoEscape("\\end{tabular}"))
    doc.append(NoEscape("\\end{flushright}"))

    
    doc.append(NoEscape("\\begin{center}"))
    for i in range(informations["NbrQuestions"]):
        doc.append(NoEscape("\\begin{tabular}{| l l l l l |}"))
        doc.append(NoEscape("\\hline"))
        doc.append(NoEscape(" & & & & \\\\"))
        doc.append(NoEscape("Question " + str(i+1) + "\\qquad \qquad\\ & & & & \\\\"))
        doc.append(NoEscape(" & A $\\qquad \\square \\qquad$ & B $\\qquad \\square \\qquad$ & C $\\qquad \\square \\qquad$ & D $\\qquad \\square \\qquad$ \\\\ "))
        doc.append(NoEscape(" & & & &  \\\\"))
        doc.append(NoEscape("\\hline"))
        doc.append(NoEscape(" & & & &  \\\\"))
        doc.append(NoEscape("Choix 2 & A $\\qquad \\square \\qquad$ & B $\\qquad \\square \\qquad$ & C $\\qquad \\square \\qquad$ & D $\\qquad \\square \\qquad$ \\\\ "))
        doc.append(NoEscape(" & & & &  \\\\"))
        doc.append(NoEscape("\\hline"))
        doc.append(NoEscape("\\end{tabular}"))
        doc.append(NoEscape("\\\\ \\vskip3mm"))
        doc.append(NoEscape("\\thispagestyle{empty}"))
    doc.append(NoEscape("\\end{center}"))
        
                   
    
    
    doc.generate_pdf('QCM_app1/questionnaire', clean_tex=False, compiler='pdfLaTeX')
    
    os.startfile("QCM_app1\questionnaire.pdf")
    time.sleep(5)
    from QCM_app import fenetreMenu
    fenetreMenu().mainloop()

