

import tkinter as tk
from tkinter import ttk

import numpy
import numpy as np
import pandas
import pandas as pd
import tkinter
import PIL
import matplotlib.pyplot as plt
import json
import scipy
import matplotlib
import matplotlib.pyplot as plt

pd.options.display.max_rows = 10

# Q1 :  Dans quel arrondissement il y a le plus de places disponibles aux plages de stationnement ouverts ?

df_Q1_Clean = pd.read_csv('df_Q1_Clean.xls', header = 0)
df_Q1_Clean.head()

# Groupby par Arrondissement

g_Q1 = df_Q1_Clean.groupby('Arrondissement')
print(g_Q1)

# Somme de duree par arrondissement

df_duree_sum = g_Q1[['Duree']].agg([pd.Series.sum])

# Reset the index and the columns

df_duree_sum = df_duree_sum.reset_index()
df_duree_sum.columns = df_duree_sum.columns.droplevel(1)
df_duree_sum = df_duree_sum.rename(columns={'Duree':'Duree_Sum'})

# Supprimer arrodissement 0

df_duree_sum = df_duree_sum.drop(1, axis=0)
print(df_duree_sum.head())

# Answers
# le plus

df_Q1_Court = df_duree_sum.sort_values(by='Duree_Sum')
print("les plus courts :", df_Q1_Court)

# le moins

df_Q1_Long = df_duree_sum.sort_values(by='Duree_Sum', ascending=False)
print("les plus courts :", df_Q1_Long)

# Table plot

df_duree_sum.plot(x='Arrondissement', y='Duree_Sum')


# Préparer un dataframe pour Q3
# Question 3 : Dans quels mois était plus / moins garé plus longtemps / plus courts ?
# Explorer les colonnes 'Date_du_releve' et 'Derniere_date_edition'

df = pd.read_csv('stationnements.txt', sep='\t', header=0)
df.columns

print(df['Date_du_releve'].value_counts(normalize=True),
      df['Derniere_date_edition'].value_counts(normalize=True))

# Il y 70% de lignes ont '2020-08-31' dans 'Date_du_releve' qui va géner le resultat.
# On va donc prendre la colonne 'Date_du_releve'

# Reprendre df_Q1_Clean et ajouter la colonne 'Date_du_releve'

df_Q1_Clean['Date_du_releve'] = df['Date_du_releve']

# Q2

df = pandas.read_csv("stationnements.txt" , sep = '\t', header = 0)

freq = df.groupby(['Arrondissement', 'Regime_particulier']).size() # pour construire la matrice d'arrondissement et combien de fois on a un type de stationnement

print(freq)

freq = freq.reset_index()       # diviser une colonne en 3 colonnes

print(freq)

cd = pandas.DataFrame(freq)     # en dataframe

print(cd)

print(cd.head(0))               # test pa besoin

groups = cd.groupby(by=['Arrondissement'])

freq2 = groups.apply(lambda g: g[g[0] == g[0].max()]) # pour afficher le maximum de chaque arrondissement et le type de stationnement à proprier

print(freq2) # affichage

cd2 = pandas.DataFrame(freq2)

print(cd2)

print(cd2.columns)

groups = cd.groupby(by=['Arrondissement'])

freq3=groups.apply(lambda g: g[g[0] == g[0].min()])# pour afficher le minimum de chaque arrondissement et le type de stationnement

print(freq3)

df = pandas.read_csv("stationnements.txt", sep = '\t', header = 0)

freq = df.groupby(['Arrondissement', 'Regime_particulier']).size() # pour construire la matrice d'arrondissement et combien de fois on a un type de stationnement

print(freq)
freq = freq.reset_index()   # diviser une colonne en 3 colonnes
print(freq)
cd = pandas.DataFrame(freq) # en dataframe
print(cd)
print(cd.head(0)) # test pas besoin

groups = cd.groupby(by = ['Arrondissement'])

freq2 = groups.apply(lambda g: g[g[0] == g[0].max()]) # pour afficher le maximum de chaque arrondissement et le type de stationnement à proprier

print(freq2) # affichage

cd2 = pandas.DataFrame(freq2)
print(cd2)

print(cd2.columns)

groups = cd.groupby(by=['Arrondissement'])

freq3=groups.apply(lambda g: g[g[0] == g[0].min()])

print(freq3)

# interface

fenetre = tk.Tk()
fenetre.geometry('1000x600')                # Definir la taille de la fenetre principale
fenetre.title("Stationnement à Paris")      # Titre
fenetre.iconbitmap("")
fenetre.configure(bg = 'ivory')             # Définir la couleur de la fenetre titre

# label arrondissement

labelChoix1 = tk.Label(fenetre , text = "Arrondissement" , bg = 'ivory')
labelChoix1.place(x = 35 , y = 50)

# label choix de la durée

labelChoix2 = tk.Label(fenetre , text = "Type durée" , bg = 'ivory')
labelChoix2.place(x = 160 , y = 50)

# label choix du mois

labelChoix3 = tk.Label(fenetre , text = "Mois" , bg = 'ivory')
labelChoix3.place(x = 280 , y = 50)

# Création de bouton type de stationnement

button = tk.Button(fenetre , text = 'Quitter' , bg = 'ivory' , command =  fenetre.destroy)
button.place(x = 800 , y = 100)

# Zone de texte pour affichage

v = tk.StringVar()
text_affichage = tk.Text(fenetre)
text_affichage.place(x = 50 , y = 140)

# Combobox creation arrondissement

n0 = tk.StringVar()
arrond = ttk.Combobox(fenetre , width = 18 , textvariable = n0)

# Adding combobox drop down list

arrond['values'] = (' Arrondissement 1',
                    ' Arrondissement 2',
                    ' Arrondissement 3',
                    ' Arrondissement 4',
                    ' Aroondissement 5',
                    ' Arrondissement 6',
                    ' Arrondissement 7',
                    ' Arrondissement 8',
                    ' Aroondissement 9',
                    ' Arrondissement 10',
                    ' Arrondissement 11',
                    ' Arrondissement 12',
                    ' Aroondissement 13',
                    ' Arrondissement 14',
                    ' Arrondissement 15',
                    ' Arrondissement 16',
                    ' Aroondissement 17',
                    ' Aroondissement 18',
                    ' Arrondissement 19',
                    ' Arrondissement 20',
                    ' Arrondissement 21',
                    ' Aroondissement 22',)

arrond.place(x = 15 , y = 70)
arrond.current()

# Combobox creation Durée

n1 = tk.StringVar()

duree = ttk.Combobox(fenetre , width = 12 , textvariable = n1)

n2 = tk.StringVar()

mois = ttk.Combobox(fenetre , width = 12 , textvariable = n2)

mois['values'] = ('Janvier',
                  'Février',
                  'Mars',
                  'Avril',
                  'Mai',
                  'Juin',
                  'Juillet',
                  'Août',
                  'Septembre',
                  'Octobre',
                  'Novembre',
                  'Décembre',)

mois.place(x = 250 , y = 70)
mois.current()

# creation Combobox stationnement

labelChoix4 = tk.Label(fenetre , text = 'Stationnement' , bg = 'ivory')
labelChoix4.place(x = 360 , y = 50)

n3 = tk.StringVar()

stationnement = ttk.Combobox(fenetre , width = 15 , textvariable = n3)
stationnement.place(x = 350 , y = 70)

stationnement['values'] = ('le + populaire', 'le - populaire')
stationnement.current()

# Adding combobox drop down list

duree['values'] = ('Min','Max')
duree.place(x = 150 , y = 70)
duree.current()

fenetre.mainloop()

# le stationnement le plus repandu dans l'arrondissement" {arr}.format(o) est le stationement génant

#
