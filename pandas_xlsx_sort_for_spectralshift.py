__author__ = 'julia'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math


df = pd.read_excel("fundamentalshifts3.xlsx")

dfs = df.replace(np.nan, True, regex=True)
# group by just gives an object... is not printable * neither by iloc
    #new_dfs = dfs.set_index([label],inplace=True)
    #new_dfs = dfs.groupby([label])

def sort_by_day(day):
    label_set = set(dfs.columns)
    label_list = list(label_set)[::-1]

    print(label_set, " label_set")
    print(label_list, "label_list")
    sorted_by_day_df = dfs['day'] == day
    #print(sorted_by_day_df)


    return dfs[sorted_by_day_df][label_list]

def get_label_names():
    label_set = set(dfs.columns)
    #print(label_set, "labels in dfs..")
    print(" number:", len(label_set))
    return label_set

def drop_column(liste):
    dfs.drop(labels=liste, axis=1, inplace = True)
    return dfs

def drop_unnamed_columns():
    auswahl = dfs.columns.str.match('Unnamed')
    empty_column_index = [i for i, x in enumerate(auswahl) if x]

    print(auswahl, empty_column_index)
    #macht er nicht: weil [liste] klammer vergessen!!
    for i in range(len(empty_column_index)):

        number = empty_column_index[i]
       # print(number)
        delete_column = "Unnamed: "+str(number)
       # print(delete_column, "labelname for column to be deleted")
        dfs.drop(labels = [delete_column], axis = 1, inplace = True)
    label_set = set(dfs.columns)
    #print(label_set, "cleaned", len(label_set))
    return dfs

def only_centered_diagnostic():
    criteria_centered = dfs['2w center'] == "center"
    label_set = set(dfs.columns)
    label_list = list(label_set)
    dfs[criteria_centered][label_list]
    return dfs


def fundamental_GVD_centered(day):
    GVD0 = dfs['GVD in fs^2'] == 0
    GVD300 = dfs['GVD in fs^2'] == 300
    GVD600 = dfs['GVD in fs^2'] == 600
    GVD900 = dfs['GVD in fs^2'] == 900
    same_day = dfs['day'] == day
    criteria_centered = dfs['2w center'] == "center"
    ROM_criteria = dfs['Nmax'] >= 22
    #outGVD0= dfs[GVD0][['day','shot', 'z um', 'EL on target','Nmax','central', 'central2' ]]
    #print(outGVD0)
    
    #out_central =dfs[GVD0 & same_day & ROM_criteria][['central']]
    out_put_all = dfs[same_day & ROM_criteria & criteria_centered][["Nmax",'central','GVD in fs^2','z um', 'EL on target']]
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print(out_put_all)
    #mean_value= out_central.mean()
    #mean_NROM = out_Nmax.mean()

    #z_same_day = dfs[GVD0 & same_day & ROM_criteria][['z um']]
    #standard_deviation = out_central.std()
    #print(mean_value, str(day), 'GVD0', "stdD", standard_deviation)
    #print(mean_NROM, "Nmax for ROM signal")
    
    
    ##plt.show()
    #return mean_value, standard_deviation
    return out_put_all
    


test2 = drop_unnamed_columns()
#get_label_names()
#test2 = drop_column(['divergence'])
#, 'comment2', 'side peaks', "Comment 1"
#get_label_names()


test2 = fundamental_GVD_centered(20190123)


#get_label_names()

#print(test2)


#print(test2)



#test = fundamental_GVD(20190118)

#print(test)

#print(test2)


