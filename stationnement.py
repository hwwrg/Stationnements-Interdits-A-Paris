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


# remplcer ',' par '.' et convertir en type float
df['Longueur'] = [x.replace(',', '.') for x in df['Longueur']]
df['Longueur'] = df['Longueur'].astype(float)
print(df.info())

# moyen de 'Longueur'
print(pandas.Series.mean(df['Longueur']))

# navigation sur 'Tarification'
print(df['Tarification'])
print(df['Tarification'].value_counts())

# crosstable 'Tarification' et 'Plage_horaire'
print(pandas.crosstab(df['Tarification'], df['Plage_horaire_1-Debut']))
print(df.loc[df['Tarification']=='NR', 'Plage_horaire_1-Debut':'Plage_horaire_1-Fin'])


def main():
    pass

if __name__ == '__main__':
    main()