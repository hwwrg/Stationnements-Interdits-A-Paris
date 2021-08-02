import pandas as pd
import numpy as np
import scipy
import matplotlib
import matplotlib.pyplot as plt

pd.options.display.max_rows = 10


# Réponse Q1 :  Dans quel arrondissement il y a le plus de places disponibles
# aux plages de stationnement ouverts?
df_Q1_Clean = pd.read_csv('df_Q1_Clean.xls', header=0)
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
# le moin
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
df_Q3 = df_Q1_Clean.copy()
print(df_Q3.head())
print(df_Q3.info())

# Transférer jour à mois et ajouter la colonne 'Mois'
df_Q3['Mois'] = pd.Series([])
for row in range(0,df_Q3.shape[0]):
    df_Q3['Mois'][row] = df['Date_du_releve'][row][5:7]
df_Q3.head()

df_Q3_Clean = df_Q3.copy()
df_Q3_Clean.to_csv('df_Q3_Clean.csv')