import googlemaps
import gmplot
import webbrowser
import numpy as np
import pandas as pd


# Importer dataframe
df = pd.read_csv("df_clean.csv", sep=',', header=0)
df = df.iloc[:100, :]

# Regrouper par 'Regime_particulier'
g = df.groupby(['Regime_particulier'])

typeRigime = df['Regime_particulier'].unique().tolist()
##print(typeRigime)
##print(type(typeRigime))

"""
['Livraison_BUS', 'Stationnement_genant', 'Arret_vigipirate_non_perennise',
'Arret_vigipirate_perennise', 'Arret_genant_divers', 'Stationnement_simple',
'Arret_simple', 'Arret_Pompiers', 'rien']
 """


def affiMap():
    # Setup point 0
    maps=googlemaps.Client(key='AIzaSyAgAxkbr7Ce49eKedJNboaEC9b1o2u5zPE')
    gmap = gmplot.GoogleMapPlotter(48.866667, 2.333333, 12)

    colors = ['red','blue','green','purple','orange','yellow','pink','white','black']

    # Afficher les attractions
    for type in typeRigime:
##        print(type, g.get_group(type))
        attractions_lats, attractions_lngs = g.get_group(type)['Latitude'], g.get_group(type)['Longitude']
##        print(type, attractions_lats)
        gmap.scatter(attractions_lats, attractions_lngs, color=colors[typeRigime.index(type)], size=40, marker=True)
        gmap.marker(48.866667, 2.333333, 'test')


    gmap.draw("{}.html".format(type))
    webbrowser.open("{}.html".format(type))


affiMap()

