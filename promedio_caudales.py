import numpy as np
import pandas as pd

def suma_total(m_matrix):
    (f,c)=m_matrix.shape;
    xs=[];
    for i in range(f):
        suma=0;
        for j in range(c):
            suma+=m_matrix.iloc[i,j];
        xs.append(suma);
    return xs;

def promedio_mensual(m_matrix):
    (f,c)=m_matrix.shape;
    xs=[];
    for j in range(c):
        #   #suma de la columna del mes j# / nro de filas (meses)
        temp=np.sum(m_matrix.iloc[:,j])/f;
        xs.append(temp);
    return xs;

def main():
    caudales=pd.read_csv('caudales.csv', sep=',');
    matrix=caudales;
    print(caudales);
    #drop una columna#
    matrix.drop(['Ano'], axis='columns', inplace=True);
    matrix=matrix.round(decimals=4);
    caudal_total_anual=suma_total(matrix);
    #inserta una columna
    matrix.insert(12,"Total", lista,True);
    print(matrix);

    meses=promedio_mensual(matrix);
    print(meses);
    #inserta una fila con los promedios de cada mes
    matrix.loc[5]=meses;
    print(matrix);
