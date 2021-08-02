#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Acène Azade Hanan Huawei Mattieu
#
# Created:     15/06/2021
# Copyright:
# Licence:
#-------------------------------------------------------------------------------

import pandas
import datetime
import tkinter
import PIL


pandas.options.display.max_rows = 10

df = pandas.read_csv("stationnements.txt", sep='\t', header=0)


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line between rows

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))


# infos de df
print(df.info())

### remplcer ',' par '.' et convertir en type float
##df['Longueur'] = [x.replace(',', '.') for x in df['Longueur']]
##df['Longueur'] = df['Longueur'].astype(float)
##print(df.info())
##
### moyen de 'Longueur'
##print(pandas.Series.mean(df['Longueur']))
##
### navigation sur 'Tarification'
##print(df['Tarification'])
##print(df['Tarification'].value_counts())
##
### crosstable 'Tarification' et 'Plage_horaire'
##print(pandas.crosstab(df['Tarification'], df['Plage_horaire_1-Debut']))
##print(df.loc[df['Tarification']=='NR', 'Plage_horaire_1-Debut':'Plage_horaire_1-Fin'])


# navigation sur 'Plage_horaire_1-Debut'
##print('-'*60, 'Plage_horaire_1-Debut')
##print(df['Plage_horaire_1-Debut'].value_counts())
##
##
### navigation sur 'Plage_horaire-Debut'
##print('-'*60 , 'Plage_horaire_1-Fin')
##print(df['Plage_horaire_1-Fin'].value_counts())
##
##
### navigation sur 'Plage_horaire_2-Debut'
##print('-'*60)
##print(df['Plage_horaire_2-Debut'].value_counts())
##
### navigation sur 'Plage_horaire_2-Fin'
##print('-'*60)
print(df['Plage_horaire_2-Fin'].value_counts())

# creneaux 1
df['Plage_horaire_1-Debut'] = pandas.to_datetime(df['Plage_horaire_1-Debut'], format ="%H:%M")
df['Plage_horaire_1-Fin'] = pandas.to_datetime(df['Plage_horaire_1-Fin'], format ="%H:%M")
df_creneaux_1 = df['Plage_horaire_1-Fin'] - df['Plage_horaire_1-Debut']
print(type(df['Plage_horaire_1-Debut'][1]))         # <class 'pandas._libs.tslibs.nattype.NaTType'>

# creneaux 2
df['Plage_horaire_2-Debut'] = pandas.to_datetime(df['Plage_horaire_2-Debut'], format ="%H:%M")
df['Plage_horaire_2-Fin'] = pandas.to_datetime(df['Plage_horaire_2-Fin'], format ="%H:%M")
df_creneaux_2 = df['Plage_horaire_2-Fin'] - df['Plage_horaire_2-Debut']

# total_creneaux
total_creneaux = abs(df_creneaux_1) + abs(df_creneaux_2)
##print(type(total_creneaux))


##print(df['Plage_horaire_1-Debut'][19394])
##print(df['Plage_horaire_1-Fin'][19394])
##
##print(df_creneaux_1[19394])


##print(df_creneaux_1.value_counts())





##print(type(total_creneaux))
##print(total_creneaux.describe())
##print(total_creneaux.value_counts())
##print(total_creneaux)







def main():
    pass

if __name__ == '__main__':
    main()