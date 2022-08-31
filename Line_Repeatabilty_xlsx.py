import pandas as pd
import numpy as np

excel_data_path = "C:/Users/sebra/Documents/MPT/Precitec/Metrology/LB and TG scan profile program(#3)/LineScan/Optimized/Excel/L10_11.xlsx"

df = pd.read_excel(excel_data_path)

line1 = df.loc[(df['#Encoder V'] == 1)]           
xyzline1 = line1.iloc[:,[4]]
meanline1 = xyzline1.groupby(np.arange(len(xyzline1))//(len(xyzline1)/24)).mean()
print(line1)
line2 = df.loc[(df['#Encoder V'] == 2)]           
xyzline2 = line2.iloc[:,[4]]
meanline2 = xyzline2.groupby(np.arange(len(xyzline2))//(len(xyzline2)/24)).mean()

line3 = df.loc[(df['#Encoder V'] == 3)]           
xyzline3 = line3.iloc[:,[4]]
meanline3 = xyzline3.groupby(np.arange(len(xyzline3))//(len(xyzline3)/24)).mean()

line4 = df.loc[(df['#Encoder V'] == 4)]           
xyzline4 = line4.iloc[:,[4]]
meanline4 = xyzline4.groupby(np.arange(len(xyzline4))//(len(xyzline4)/24)).mean()

line5 = df.loc[(df['#Encoder V'] == 5)]           
xyzline5 = line5.iloc[:,[4]]
meanline5 = xyzline5.groupby(np.arange(len(xyzline5))//(len(xyzline5)/24)).mean()

line6 = df.loc[(df['#Encoder V'] == 6)]           
xyzline6 = line6.iloc[:,[4]]
meanline6 = xyzline6.groupby(np.arange(len(xyzline6))//(len(xyzline6)/24)).mean()

line7 = df.loc[(df['#Encoder V'] == 7)]           
xyzline7 = line7.iloc[:,[4]]
meanline7 = xyzline7.groupby(np.arange(len(xyzline7))//(len(xyzline7)/24)).mean()

line8 = df.loc[(df['#Encoder V'] == 8)]           
xyzline8 = line8.iloc[:,[4]]
meanline8 = xyzline8.groupby(np.arange(len(xyzline8))//(len(xyzline8)/24)).mean()

line9 = df.loc[(df['#Encoder V'] == 9)]           
xyzline9 = line9.iloc[:,[4]]
meanline9 = xyzline9.groupby(np.arange(len(xyzline9))//(len(xyzline9)/24)).mean()

line10 = df.loc[(df['#Encoder V'] == 11)]           
xyzline10 = line10.iloc[:,[4]]
meanline10 = xyzline10.groupby(np.arange(len(xyzline10))//(len(xyzline10)/24)).mean()

frames = [meanline1, meanline2, meanline3, meanline4, meanline5, meanline6, meanline7, meanline8, meanline9, meanline10]
df_cd = pd.concat(frames,axis=1)
print(df_cd)
df_cd.to_csv('raw.csv', index=False)
repeatabilityLine = df_cd.std(axis=1)
print(repeatabilityLine)
repeatabilityLine.to_csv('out.csv', index=False)
print('Repeatability =', repeatabilityLine.mean(), ' microns')

print(len(xyzline1))