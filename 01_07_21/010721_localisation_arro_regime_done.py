
import googlemaps
import gmplot
import webbrowser
import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk


df = pd.read_csv("df_clean.csv", sep=',', header=0)
g = df.groupby(['Arrondissement','Regime_particulier'])


def getFiltres():
    """Générer les filtres"""
    arro = int(arroCom.get()[-2:])
    filtremap = ((arro,regCom.get()))
    affiMap(filtremap)


def affiMap(filtremap):
    """Afficher les localisations des places parkings sur Google Map"""

    # Générer les donnés geolocalisation
    dfMap = g.get_group(filtremap)
    attractions_lats, attractions_lngs = dfMap['Latitude'], dfMap['Longitude']

    # Setup point 0
    maps=googlemaps.Client(key='AIzaSyAgAxkbr7Ce49eKedJNboaEC9b1o2u5zPE')
    gmap = gmplot.GoogleMapPlotter(48.866667, 2.333333, 12)
    gmap.marker(48.866667, 2.333333, color='cornflowerblue')

    # Afficher les attractions
    gmap.scatter(attractions_lats, attractions_lngs, color='red', size=40, marker=True)

    # Déssiner le map à un HTML fichier et l'afficher dans navigateur
    gmap.draw("Arrondissement-{}-{}.html".format(filtremap[0],filtremap[1]))
    webbrowser.open("Arrondissement-{}-{}.html".format(filtremap[0],filtremap[1]))


def main():
    pass

if __name__ == '__main__':
    main()


fenGeo = tk.Tk()
fenGeo.geometry('1000x200')                # Definir la taille de la fenetre principale
fenGeo.title("Géolocalisation Des Places Parkings Interdites à Paris")      # Titre
fenGeo.iconbitmap("")
fenGeo.configure(bg = 'ivory')             # Définir la couleur de la fenetre titre


# Créer un Combobox pour 'arrondissement'
arroCom = ttk.Combobox(fenGeo, width = 18,)
arroCom['values'] = (
                    'Arrondissement -1',
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
                    'Arrondissement 21',
                    'Aroondissement 22',)

arroCom.place(x=15, y=70)
arroCom.current()

# créer un Combobox pour 'Regime_particulier'
regCom = ttk.Combobox(fenGeo, width=18)
regCom['values'] =(
                'Livraison_BUS',
                'Stationnement_genant',
                'Arret_vigipirate_non_perennise',
                'Arret_vigipirate_perennise',
                'Arret_genant_divers',
                'Stationnement_simple',
                'Arret_simple',
                'Arret_Pompiers',
                'rien')
regCom.place(x=215, y=70)
regCom.current()

# créer un Bouton pour envoyer les filtres et activer la fonction
mapBou = tk.Button(fenGeo, text='Afficher', command=getFiltres)
mapBou.place(x=415, y=70)


arroLabel = tk.Label(fenGeo, text='Choississez Un Arrodissement :', bg='ivory')
regLabel = tk.Label(fenGeo, text='Choississez Une Type de Vandalisation :', bg='ivory')
arroLabel.place(x=15, y=40)
regLabel.place(x=215, y=40)


fenGeo.mainloop()
