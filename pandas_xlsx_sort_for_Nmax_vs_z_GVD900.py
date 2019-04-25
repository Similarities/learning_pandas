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


def fundamental_GVD_centered():
    GVD0 = dfs['GVD in fs^2'] == 0
    GVD300 = dfs['GVD in fs^2'] == 300
    GVD600 = dfs['GVD in fs^2'] > 600
    GVD900 = dfs['GVD in fs^2'] <= 900

    criteria_non_zero = dfs['Nmax'] > 1
    criteria_centered = dfs['2w center'] == "center"
    criteria_PP_out = dfs["PP in out"] == "out"
    criteria_EL_below_3 = dfs["EL on target"] < 4
    criteria_EL_above_2 = dfs["EL on target"] > 2
    ROM_criteria = dfs['Nmax'] > 22
    #outGVD0= dfs[GVD0][['day','shot', 'z um', 'EL on target','Nmax','central', 'central2' ]]
    #print(outGVD0)

    overall_shots = dfs[criteria_centered & criteria_non_zero & criteria_EL_below_3 & criteria_EL_above_2 & criteria_PP_out & GVD900 & GVD600][["shot"]]
    print(len(overall_shots), "all shots with HHG content centered")


    shots_ROM = dfs[criteria_centered & ROM_criteria & criteria_EL_below_3 & criteria_EL_above_2 & criteria_PP_out & GVD900 & GVD600][["shot"]]
    print(len(shots_ROM), "only ROM")
    sub_dataset = dfs[criteria_centered & criteria_non_zero & criteria_EL_above_2 & criteria_EL_below_3 & criteria_PP_out & GVD900 & GVD600][["Nmax",'central ROM','GVD in fs^2','z um', 'EL on target', "day"]]
    sub_dataset2= dfs[criteria_centered & criteria_non_zero & criteria_EL_above_2 & criteria_EL_below_3 & criteria_PP_out & GVD900 & GVD600][["Nmax",'central ROM','GVD in fs^2','z um', 'EL on target', "day"]]
    print(sub_dataset)

    EL_up_2half = sub_dataset["EL on target"] <= 2.8
    EL_above_2half = sub_dataset2["EL on target"]> 2.8
    x = sub_dataset[EL_up_2half][["Nmax"]]
    print(len(x), " shots ")
    y = sub_dataset[EL_up_2half][['z um']]
    plt.xlabel("Nmax")
    plt.ylabel("um")
    plt.xlim(10,50)

    plt.figure(1)
    plt.scatter( x, y,alpha=0.1, color = "b", label = "<= 2.5J")
   # plt.colorbar()
    plt.legend()
    x = sub_dataset2[EL_above_2half][["Nmax"]]
    print(len(x), " shots ")
    y = sub_dataset2[EL_above_2half][['z um']]
    plt.xlabel("Nmax")
    plt.ylabel("um")
    plt.xlim(10,50)


    plt.scatter( x, y,alpha=0.1, color = "r", label = ">2.5 & <3.6 J")
   # plt.colorbar()
    plt.legend()
    plt.show()

    plt.show()

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

test2 = fundamental_GVD_centered()
#test3 = count_dataset_GVD_redshift()

#get_label_names()

#print(test2)


#print(test2)



#test = fundamental_GVD(20190118)

#print(test)

#print(test2)


