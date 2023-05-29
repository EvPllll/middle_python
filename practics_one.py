import pandas as pd
import numpy as np

if __name__ == '__main__':
    table = pd.read_csv("C:\All files\Projects\Middle_python\learnings\one\sales_headers.csv", parse_dates=['date'])
    # print(table[['sales', 'family']].groupby('family').sum())
    table.loc[table.family == 'EGGS', ('store_nbr', 'sales')] = 50
    table.loc[table.index == 1, ('family')] = 'BRAIN'
    table.loc[table.index == 1, ('sales')] = 560.756
    table.loc[table.index == 4, ('family')] = 'BRAIN'

    # print(table[['family', 'sales']].groupby('family').sum())
    table.loc[table.index == 0, ('onpromotion')] = 1
    # print(table)

    table_two = pd.read_csv("C:\All files\Projects\Middle_python\learnings\one\sales_headers.csv", index_col=[False] ,parse_dates=['date'])
    table_two.loc[table_two.sales == 0, ('sales')] = 560.964
    table_two.loc[table_two.family == 'DAIRY', ('family')] = 'EGGS' # изменение одного элемента
    table_two['sales'] = np.where((table_two.family == 'EGGS'), 50, table_two.sales) # изменение нескольких элементов

    # print(table_two[['family', 'sales']].groupby('family').sum())

    table_two.loc[table_two.sales == 50, ('family', 'store_nbr')] = 432 # тоже изменение нескольких элементов
    print(table_two)
    print(table)