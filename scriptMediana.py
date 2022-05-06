import os
from fiona.env import defenv
import geopandas as gpd
import pandas as pd

arr = os.listdir()
suffix_list = []  #lista de .shp files
for e in arr:
    for element in e.split():
        if element.endswith(".shp"):
            suffix_list.append(element)
dataframe = pd.DataFrame()
for shp in suffix_list:
    df1 = gpd.read_file(shp)
    df1 = pd.DataFrame(df1)
    sp1 = df1['N_1a14d']
    sp1 = pd.DataFrame({'N_1a14d': sp1})
    dataframe = pd.concat([sp1,dataframe],axis=1)
#print(dataframe) #n_1a14d de las semanas
df = dataframe.T.median()
arr1 = gpd.read_file(suffix_list[0])
arr1 = pd.DataFrame(arr1)
df2 = arr1.drop('N_1a14d',axis=1)
df2['N_1a14d'] = df
df2 = df2[['REGIÓN', 'COMUNA', 'ID_C_AUC', 'N_1a14d','geometry']]
df2 = gpd.GeoDataFrame(df2)
name = os.getcwd()
name = os.path.basename(name)
os.mkdir('Mediana')
df2.to_file("Mediana/Mediana{}.shp".format(name))