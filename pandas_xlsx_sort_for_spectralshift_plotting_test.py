__author__ = 'julia'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math



df = pd.read_excel("fundamentalshifts6_selection.xlsx")

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
    criteria_non_zero = dfs['central ROM'] != 0
    criteria_centered = dfs['2w center'] == "center"
    ROM_criteria = dfs['Nmax'] >= 22
    #outGVD0= dfs[GVD0][['day','shot', 'z um', 'EL on target','Nmax','central', 'central2' ]]
    #print(outGVD0)
    criteria_all = dfs['central'] !=0
    overall_shots = dfs[criteria_centered & criteria_all][["shot"]]
    print(len(overall_shots), "all shots with HHG even N<22")

    #out_central =dfs[GVD0 & same_day & ROM_criteria][['central']]
    sub_dataset = dfs[criteria_centered & criteria_non_zero][["Nmax",'central ROM','GVD in fs^2','z um', 'EL on target', "day"]]
    print('xxxxxxxxxxxxxxxxxxxxall centered, with N>22, for different GVDSxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print(sub_dataset)
    x = sub_dataset[["central ROM"]]
    print(len(x), " shots with N>22", x)
    y = sub_dataset[['GVD in fs^2']]
    plt.xlabel("nm")
    plt.ylabel("GVD in fs^2")
    plt.xlim(750,850)

    plt.figure(1)
    plt.scatter( x, y,alpha=0.05, color = "r")
   # plt.colorbar()
    plt.legend()
    plt.show()


    return sub_dataset

def count_dataset_GVD_redshift():
    all_entrys =test2.count()
    print(all_entrys, 'all this day')
    redshift =test2["central"] >= 808
    redshifted = test2[redshift][["Nmax",'central ROM','GVD in fs^2','z um', 'EL on target',"day"]]
    count_red = redshifted.count()
    print(redshifted, "redshifted")
    print("fundamental > 808nm:", redshifted["day"].value_counts())



    print('out of this:')
    print("via  value", redshifted["GVD in fs^2"].value_counts())
    print("via value z in um", redshifted["z um"].value_counts())



test2 = drop_unnamed_columns()
#get_label_names()
#test2 = drop_column(['divergence'])
#, 'comment2', 'side peaks', "Comment 1"
#get_label_names()
print(df.count())

test2 = fundamental_GVD_centered(20190123)
#test3 = count_dataset_GVD_redshift()

#get_label_names()

#print(test2)


#print(test2)



#test = fundamental_GVD(20190118)

#print(test)

#print(test2)


