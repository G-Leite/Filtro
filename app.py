import pandas as pd

#planilhas com dataframe
df1 = pd.read_excel(r' ') #planilha 1
df2 = pd.read_excel(r' ') #planilha 2

#verifica os dados
repetidos = pd.merge(df1, df2, how='inner') 
n_repetem = pd.concat([df1, df2]).drop_duplicates(keep=False)

#cria um novo arquivo em xlsx com duas planilhas, uma de repetidos e uma de não repetidos.
with pd.ExcelWriter(r' ') as writer:
    repetidos.to_excel(writer, sheet_name='Repetidos', index=False)
    n_repetem.to_excel(writer, sheet_name='N Repetem', index=False)

