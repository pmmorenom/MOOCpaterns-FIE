#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 19:14:06 2022

@author: mariasanzgomez
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sem1 = pd.read_csv('user_fechas_W01.csv')
sem2 = pd.read_csv('user_fechas_W2.csv')
sem3 = pd.read_csv('user_fechas_W3.csv')
sem4 = pd.read_csv('user_fechas_W4.csv') 
sem5 = pd.read_csv('user_fechas_W5.csv')
sem6 = pd.read_csv('user_fechas_W6.csv')
total = pd.read_csv('user_fechas.csv')

df_total = pd.DataFrame(total)
corr_df_total = df_total.corr(method='pearson')

df_sem1 = pd.DataFrame(sem1)
corr_df_sem1 = df_sem1.corr(method='pearson')

df_sem2 = pd.DataFrame(sem2)
corr_df_sem2 = df_sem2.corr(method='pearson')

df_sem3 = pd.DataFrame(sem3)
corr_df_sem3 = df_sem3.corr(method='pearson')

df_sem4 = pd.DataFrame(sem4)
corr_df_sem4 = df_sem4.corr(method='pearson')

df_sem5 = pd.DataFrame(sem5)
corr_df_sem5 = df_sem5.corr(method='pearson')

df_sem6 = pd.DataFrame(sem6)
corr_df_sem6 = df_sem6.corr(method='pearson')


corr_table = pd.DataFrame()
corr_table['sem1'] = corr_df_sem1['Nota'] 
corr_table['sem2'] = corr_df_sem2['Nota'] 
corr_table['sem3'] = corr_df_sem3['Nota'] 
corr_table['sem4'] = corr_df_sem4['Nota'] 
corr_table['sem5'] = corr_df_sem5['Nota'] 
corr_table['sem6'] = corr_df_sem6['Nota'] 
corr_table['total']= corr_df_total['Nota'] 
corr = corr_table.drop(corr_table.index[[0]])

print(corr.head())
plt.figure(figsize=(10, 10))
sns.heatmap(corr, annot=True)
plt.show()


#https://www.delftstack.com/es/howto/python-pandas/pandas-correlation-matrix/