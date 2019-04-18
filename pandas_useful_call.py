__author__ = 'julia'


# anzeigen der  obersten Werte
xy_df.head(n=10)

# anzeigen dateiinformationen
xy_df.info()

# dropping coloumn by keyword irreversible
xy_df.drop(labels=['Comments'], axis=1, inplace = True)

# convert NaN to dtype object
xy_df['Fuel whatever'].dtype

#convert into numeric
travel_df['FuelEconomy'] = pd.to_numeric(travel_df['FuelEconomy'],errors='coerce')


# auffuellen NaN mit Mittelwerten
travel_df['FuelEconomy'].fillna(travel_df['FuelEconomy'].mean(),inplace=True)

# give out particular line
travel_df.iloc[0]
travel_df.iloc[9] # ersten 10


#Datagrouping by keyword
travel_df_by_date = travel_df.groupby(['Date'])


# Dataframegrouping with sum grouped by date
travel_df_by_date_combined = travel_df_by_date.sum()

# discriminate by comparison
distance_above_ninety = travel_df_by_date_combined['Distance']>90

#combine two discriminations
ninety_to_hundred_df = travel_df_by_date_combined[distance_above_ninety & distance_below_hundred]

# particular multi-parameter question
over_ninety_on_friday = travel_df_by_date_combined[(travel_df_by_date_combined['AvgMovingSpeed']>90) & (travel_df_by_date_combined['DayOfWeek']=='Friday')]