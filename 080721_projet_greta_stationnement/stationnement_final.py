#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:
#
# Created:     02/07/2021
# Copyright:   (c) tf 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

"""
==ToDo==
-Débuger : googlemap-Paris
-couleurs des diagrams
-build executable
"""

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import pandas as pd
import numpy as np
import scipy
import matplotlib
import matplotlib.pyplot as plt

import googlemaps
import gmplot
import webbrowser
from easygui import msgbox

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Générer les résultats des 3 Questions
# Q1 :
df1 = pd.read_csv('dfq1.csv')

dicQ1 = {}
listeArro = df1['Arrondissement'].tolist()
listeDA = df1['Duree'].tolist()             # liste Durée-Arrondissement

for i in range(len(listeArro)):
    dicQ1[listeArro[i]] = listeDA[i]

# L'arrondissement a plus de horaires ouvertes
max_valeur_Q1 = 0       # Valeur maximun
max_arro_Q1 = 0         # Arrondissement qui a le valeur maximum
for k in dicQ1:
    if dicQ1[k] > max_valeur_Q1:
        max_valeur_Q1 = dicQ1[k]
        max_arro_Q1 = k

# l'arrondissement -1 n'a que 3 place parkting qui ne donnera pas
# trop de sens dans la comparasion
# On va donc comparer les autres arrondissements
min_valeur_Q1 = dicQ1[1]        # Valeur minimum
min_arro_Q1 = 1                 # Arrondissement qui a le valeur minimum
for k in dicQ1:
    if k == -1:
        pass
    elif dicQ1[k] < min_valeur_Q1:
        min_valeur_Q1 = dicQ1[k]
        min_arro_Q1 = k

res1 = "L'arrondissement {} est celui ou il y a le plus de stationnements illégals. \n L'arrondissement {} est celui ou il y a le moins de stationnements illégals.".format(int(max_arro_Q1), int(min_arro_Q1))


# Q2 :
df2 = pd.read_csv('dfq2.csv')

# Q3
df3 = pd.read_csv('dfq3.csv')

dicQ3 = {}
listeMois = df3['Mois'].tolist()
listeMS = df3['sum'].tolist()       # liste sum par mois

for i in range(len(listeMois)):
    dicQ3[listeMois[i]] = listeMS[i]

# Le mois a plus de horaires ouvertes
max_valeur_Q3 = 0       # Valeur maximun
max_mois_Q3 = 0         # Arrondissement qui a le valeur maximum
for k in dicQ3:
    if dicQ3[k] > max_valeur_Q3:
        max_valeur_Q3 = dicQ3[k]
        max_mois_Q3 = k

# Le mois a moin de horaires ouvertes
min_valeur_Q3 = dicQ3[1]        # Valeur minimum
min_mois_Q3 = 1                 # Arrondissement qui a le valeur minimum
for k in dicQ3:
    if dicQ3[k] < min_valeur_Q3:
        min_valeur_Q3 = dicQ3[k]
        min_mois_Q3 = k

res3 = "Novembre est le mois où la durée de stationnement est la plus faible. \n Août est le mois où la durée de stationnement est la plus grande."


# Classe couleur
class Couleur:
    """Stocker les couleurs"""
    def __init__(self):
        self.fen_bg = "ivory"
        self.title1 = "#0c4fa0"
##        self.title2 = "#FFFFFF"
        self.tex = "#0086EE"        #White
##        self.bou_bg = "#E5E4E2"     #Platinum
        self.bou_fg = "#FF956B"
##        self.lettre = "#C11B17"     #Chilli Pepper

class Font:
    """Stocker les polices de caractères"""
    def __init__(self):
        self.title1 = tkFont.Font(family="Microsoft YaHei UI", size='25', weight="normal")
        self.title2 = tkFont.Font(family="Microsoft YaHei UI", size='25', weight="normal")
        self.bouton = tkFont.Font(family="Microsoft YaHei UI", size='12', weight="bold")
        self.text1 = tkFont.Font(family="Microsoft YaHei UI", size='16', weight="normal")
        self.combobox = tkFont.Font(family="Microsoft YaHei UI", size='14', weight="normal")





# Créer Tkinter
fen = tk.Tk()
fen.title("Stationnement Paris")
fen.geometry('1000x700')

# Intanciation des classes Couleur() et Font()
couleur = Couleur()
font = Font()

fen.configure(bg=couleur.fen_bg)



# Ecran 1 Accueil
def ecran1():
    global fra1
    global fra0
    global fra2

    fra0 = tk.Frame(fen, height=100)        # Réserver l'espace
    fra1 = tk.Frame(fen, bg=couleur.fen_bg)
    fra2 = tk.Frame(fen)                    # Réserver l'espace

##    fra0.pack()
    fra1.pack()
    fra2.pack()


    titleAccue = tk.Label(fra1, text='Exploration Des Données Stationnements Interdits A Paris', font=font.title1, bg=couleur.fen_bg, fg=couleur.bou_fg)
    imgAccue = tk.PhotoImage(file='parking.png')
    imgAccueLabel = tk.Label(fra1, image=imgAccue)
    analyseBou = tk.Button(fra1, text='Analyse', width=30, height=1, font=font.bouton, fg=couleur.bou_fg, command=ecran2)
    geoBou = tk.Button(fra1, text='Géolocation', width=30, height=1, font=font.bouton, fg=couleur.bou_fg, command=geo)

    titleAccue.grid(row=0, column=0, columnspan=2, pady=35)
    imgAccueLabel.grid(row=1, column=0, columnspan=2)
    imgAccueLabel.image=imgAccue
    analyseBou.grid(row=2, column=0, pady=20)
    geoBou.grid(row=2, column=1, pady=20)

def retourAnalyseAccueil():
    fra3.destroy()
    ecran1()

# Ecran 2 Accueille Analyse
def ecran2():
    global fra3

    fra0.destroy()
    fra1.destroy()

    fra3 = tk.Frame(fen, bg=couleur.fen_bg)
    fra3.pack()

    titleAna = tk.Label(fra3, text='Analyse Des Données', font=font.title2, bg=couleur.fen_bg, fg=couleur.bou_fg)

    q1Label = tk.Label(fra3,
                    text='Q1 : Dans quel arrondissement il y a le plus, le moins de stationnements illégaux ?',
                    font=font.text1, bg=couleur.fen_bg, fg=couleur.tex)
    imgq1 = tk.PhotoImage(file="q1.png")
    imgq1Label = tk.Label(fra3, image=imgq1)
    q1Bou = tk.Button(fra3, text='Afficher', width=30, font=font.bouton, fg=couleur.bou_fg, command=q1)

    q2Label = tk.Label(fra3,
                    text='Q2 : Quels types de stationnements illégaux étaient plus, moins populaires \n dans les arrondissements de Paris ?',
                    font=font.text1, bg=couleur.fen_bg, fg=couleur.tex)
    imgq2 = tk.PhotoImage(file="q2.png")
    imgq2Label = tk.Label(fra3, image=imgq2)
    q2Bou = tk.Button(fra3, text='Afficher', width=30, font=font.bouton, fg=couleur.bou_fg, command=q2)

    q3Label = tk.Label(fra3,
                    text='Q3 : Quels étaient les mois où la durée de stationnement était la plus longue, la plus courte ?',
                    font=font.text1, bg=couleur.fen_bg, fg=couleur.tex)
    imgq3 = tk.PhotoImage(file="q3.png")
    imgq3Label = tk.Label(fra3, image=imgq3)
    q3Bou = tk.Button(fra3, text='Afficher', width=30, font=font.bouton, fg=couleur.bou_fg, command=q3)

    retourBou = tk.Button(fra3, text='Retour', font=font.bouton, fg=couleur.bou_fg, command=retourAnalyseAccueil)

    titleAna.pack(pady=5)


    imgq1Label.pack(pady=2)
    imgq1Label.image=imgq1
    q1Label.pack()
    q1Bou.pack()

    imgq2Label.pack(pady=2)
    imgq2Label.image=imgq2
    q2Label.pack()
    q2Bou.pack()

    imgq3Label.pack(pady=2)
    imgq3Label.image=imgq3
    q3Label.pack()
    q3Bou.pack()

    retourBou.pack(pady=10)



def retourq1Analyse():
    fraQ1.destroy()
    ecran2()

# Ecran 3 Résultats Analyse : chaque question une frame
def q1():
    global fraQ1

    fra0.destroy()
    fra3.destroy()


    fraQ1 = tk.Frame(fen, bg=couleur.fen_bg)
    fraQ1.pack()

    titleQ1 = tk.Label(fraQ1, text='Résultats Question 1', font=font.title2, bg=couleur.fen_bg, fg=couleur.bou_fg)
    labelQ1 = tk.Label(fraQ1, text=res1, font=font.text1, bg=couleur.fen_bg, fg=couleur.tex)

    titleQ1.pack(pady=10)
    labelQ1.pack(pady=5)

    f1 = Figure()
    ax1 = f1.add_subplot(111)

    ax1.set_xlim(1,22.5)
    ax1.set_xticks(np.linspace(1,22,22))

    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    ax1.text(16,2605660,"max : 16eme",fontsize=14,color="g",alpha=1)
    ax1.text(2,394920,"min : 2eme",fontsize=14,color="g",alpha=1)

    ax1.set_xlabel("Arrondissement (21=Bois Vencennes, 22=Bois Boulogne)")

    ax1.plot(listeArro, listeDA,"b-.d")

    canvas1 = FigureCanvasTkAgg(f1, master=fraQ1)
    canvas1.draw()
    canvas1.get_tk_widget().pack()

    retourBou = tk.Button(fraQ1, text='Retour', font=font.bouton, fg=couleur.bou_fg, command=retourq1Analyse)
    retourBou.pack(pady=15)

def q2():

    global fraQ1

    fra0.destroy()
    fra3.destroy()

    fraQ1 = tk.Frame(fen, bg=couleur.fen_bg)
    fraQ1.pack()

    titleQ2 = tk.Label(fraQ1, text='Résultats Question 2', font=font.title2, bg=couleur.fen_bg, fg=couleur.bou_fg)
    titleQ2.pack(pady=15)

    colonnes_q2 = tuple(df2.keys().tolist())

    tv2 = ttk.Treeview(fraQ1, show="headings", height=24, columns=colonnes_q2)  # show="headings"
    for i in colonnes_q2:
        tv2.column(i, width=185, anchor="center")
        tv2.heading(i, text=i)

    tv2.pack(pady=15)

    for i in range(df2.shape[0]):
        tv2.insert("", i, values=(
                                df2['Arrondissement'][i],
                                df2['Max_Regime_particulier'][i],
                                df2['Numbre_Max'][i],
                                df2['Min_Regime_particulier'][i],
                                df2['Numbre_Min'][i],
                                ))
    retourBou = tk.Button(fraQ1, text='Retour', font=font.bouton, fg=couleur.bou_fg, command=retourq1Analyse)
    retourBou.pack(pady=15)

def q3():

    global fraQ1

    fra0.destroy()
    fra3.destroy()

    fraQ1 = tk.Frame(fen, bg=couleur.fen_bg)
    fraQ1.pack()

    titleQ3 = tk.Label(fraQ1, text='Résultats Question 3', font=font.title2, bg=couleur.fen_bg, fg=couleur.bou_fg)
    labelQ3 = tk.Label(fraQ1, text=res3, font=font.text1, bg=couleur.fen_bg, fg=couleur.tex)


    titleQ3.pack(pady=10)
    labelQ3.pack(pady=5)

    f3 = Figure()
    ax3 = f3.add_subplot(111)

    ax3.set_xlim(1,12.3)
    ax3.set_xticks(np.linspace(1,12,12))

    ax3.spines["top"].set_visible(False)
    ax3.spines["right"].set_visible(False)

    ax3.text(7.5,25605660,"max : Août",fontsize=14,color="g",alpha=1)
    ax3.text(10,1222240,"min : Novembre",fontsize=14,color="g",alpha=1)

    ax3.set_xlabel("Mois")

    ax3.plot(listeMois, listeMS,"b-.d")

    canvas3 = FigureCanvasTkAgg(f3, master=fraQ1)
    canvas3.draw()
    canvas3.get_tk_widget().pack()

    retourBou = tk.Button(fraQ1, text='Retour', font=font.bouton, fg=couleur.bou_fg, command=retourq1Analyse)
    retourBou.pack(pady=10)


# Ecran 4 Géolocalisation
# Functons Ecran 4
df = pd.read_csv("df_clean.csv", sep=',', header=0)

group_AR = df.groupby(['Arrondissement','Regime_particulier'])
group_Arro = df.groupby(['Arrondissement'])
group_Reg = df.groupby(['Regime_particulier'])


def aucuneDonnee():
    """Afficher erreur de choix des données"""
    msgbox("Aucune Donnée.")

def geneDfMap():
    global nondonneLabel
    """Générer la DataFrame pour googlemap"""

    # Récupérer les filtres de tkinter
    arro = arroCom.get()[-2:]           # Arrondissement, 'is' pour 'Paris'
    reg = regCom.get()                  # Type de régime

    # Controler si données existent
    if (arro == 'is') | (reg == 'Toutes Les Types'):
        pass
    else:
        try:
            test4 = group_AR.get_group((int(arro),regCom.get()))
        except:
            print("non existant")
            aucuneDonnee()              # Afficher erreur
        print(arro, reg)

    # Créer URL adresse
    url = "{}-{}".format(arro, reg)

    # Construire dataframe pour générer les coordonnées géograpiques
    if (arro == 'is') & (reg == 'Toutes Les Types'):        # 'is' --> Paris
        dfMap = df
    elif arro == 'is':
        dfMap = group_Reg.get_group(reg)
    elif reg == 'Toutes Les Types':
        dfMap = group_Arro.get_group(int(arro))
    else:
        dfMap = group_AR.get_group((int(arro),regCom.get()))

    # Appleler fonction
    affiMap(dfMap, url)


def affiMap(dfMap, url):
    """Afficher les localisations des places parkings sur Google Map"""

    # Générer les donnés geolocalisation
    attractions_lats, attractions_lngs = dfMap['Latitude'].tolist(), dfMap['Longitude'].tolist()

    # Setup point 0
    maps=googlemaps.Client(key='AIzaSyAgAxkbr7Ce49eKedJNboaEC9b1o2u5zPE')
    gmap = gmplot.GoogleMapPlotter(48.866667, 2.333333, 12)
    gmap.marker(48.866667, 2.333333, color='cornflowerblue', title='test')

    # Afficher les attractions
    gmap.scatter(attractions_lats, attractions_lngs, )
    print(dfMap['Regime_particulier'].unique())

    # listes des couleurs et des types
    colors = ['red','blue','green','purple','orange','yellow','pink','white','black']   # trop moche
    typeRigime = df['Regime_particulier'].unique().tolist()

    # Colorer et donner un titre
    for i in range(len(attractions_lats)):
        type = dfMap['Regime_particulier'].iloc[i]
        color=colors[typeRigime.index(type)]

        gmap.marker(attractions_lats[i], attractions_lngs[i], color=color, title="Type : {}. Coordonnées : {} , {}".format(type, attractions_lats[i], attractions_lngs[i]) )

    # Déssiner le map à un HTML fichier et l'afficher dans navigateur
    gmap.draw("{}.html".format(url))
    webbrowser.open("{}.html".format(url))

def retourGeoAccueil():
    fraGeo.destroy()
    ecran1()

def geo():

    global fraGeo

    """Activer la géolocalisation"""
    global arroCom
    global reg
    global regCom

    fra0.destroy()
    fra1.destroy()
    fra2.destroy()

    # Créer une frame geolocalisation
    fraGeo = tk.Frame(fen, bg=couleur.fen_bg)
    fraGeo.pack()

    # titre
    titleGeo = tk.Label(fraGeo, text='Géolocation Des Stationnement Illégals A Paris', font=font.title2, bg=couleur.fen_bg, fg=couleur.bou_fg)

    # lables
    arroLabel = tk.Label(fraGeo, text='Choississez Un Arrondissement :', bg=couleur.fen_bg, fg=couleur.tex, font=font.text1)
    regLabel = tk.Label(fraGeo, text='Choississez Une Type de Vandalisation :', bg=couleur.fen_bg, fg=couleur.tex, font=font.text1)


    # Créer un Combobox pour 'arrondissement'
    arroCom = ttk.Combobox(fraGeo, justify="center", width=20, font=font.combobox)
    arroCom['values'] = (
                        'Arrondissement 1',
                        'Arrondissement 2',
                        'Arrondissement 3',
                        'Arrondissement 4',
                        'Aroondissement 5',
                        'Arrondissement 6',
                        'Arrondissement 7',
                        'Arrondissement 8',
                        'Aroondissement 9',
                        'Arrondissement 10',
                        'Arrondissement 11',
                        'Arrondissement 12',
                        'Aroondissement 13',
                        'Arrondissement 14',
                        'Arrondissement 15',
                        'Arrondissement 16',
                        'Aroondissement 17',
                        'Aroondissement 18',
                        'Arrondissement 19',
                        'Arrondissement 20',
                        'Bois De Vincennes 21',
                        'Bois De Boulogne 22',
                        'Autres -1',
                        #'Paris',
                        )
    arroCom.current(0)


    # Créer un Combobox pour 'Regime_particulier'
    regCom = ttk.Combobox(fraGeo, width=20, font=font.combobox)
    regCom['values'] =(
                    'Livraison_BUS',
                    'Stationnement_genant',
                    'Arret_vigipirate_non_perennise',
                    'Arret_vigipirate_perennise',
                    'Arret_genant_divers',
                    'Stationnement_simple',
                    'Arret_simple',
                    'Arret_Pompiers',
                    'Non Répertorié',
                    #'Toutes Les Types',
                    )
    regCom.current(0)

    # créer un Bouton pour envoyer les filtres et activer la fonction
    mapBou = tk.Button(fraGeo, text='Afficher', font=font.bouton, fg=couleur.bou_fg, command=geneDfMap)

    imgGeo = tk.PhotoImage(file="paris.png")
    imgGeoLabel = tk.Label(fraGeo, image=imgGeo, borderwidth=0)

    retourBou = tk.Button(fraGeo, text='Retour', font=font.bouton, fg=couleur.bou_fg, command=retourGeoAccueil)



    titleGeo.grid(row=0, column=0, columnspan=3, pady=15)

    arroLabel.grid(row=1, column=0, padx=20, pady=10)
    regLabel.grid(row=1, column=1, padx=20, pady=10)

    arroCom.grid(row=2, column=0)
    regCom.grid(row=2, column=1)
    mapBou.grid(row=2, column=2)

    imgGeoLabel.grid(row=3, column=0, columnspan=3, pady=15)
    imgGeoLabel.image=imgGeo

    retourBou.grid(row=4, column=0, columnspan=3, pady=15)


    print('finit')


def main():
    ecran1()

    fen.mainloop()


if __name__ == '__main__':
    main()
