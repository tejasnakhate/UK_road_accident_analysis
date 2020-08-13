
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder


def preprocessing(data):
    data.drop(
        ['Police_Force', 'Junction_Detail', 'Junction_Control', 'Special_Conditions_at_Site', 'Carriageway_Hazards',
         'Did_Police_Officer_Attend_Scene_of_Accident', 'LSOA_of_Accident_Location', 'Local_Authority_(District)',
         'Local_Authority_(Highway)'], axis=1, inplace=True)
    data.dropna(inplace=True)
    data = data[data.Weather_Conditions != 'Unknown']
    data = data[data.Road_Type != 'Unknown']
    data = data[data.Road_Surface_Conditions != '']

    le = LabelEncoder()
    data["Pedestrian_Crossing-Physical_Facilities"] = le.fit_transform(data["Pedestrian_Crossing-Physical_Facilities"])
    data["Light_Conditions"] = le.fit_transform(data["Light_Conditions"])
    data["Weather_Conditions"] = le.fit_transform(data["Weather_Conditions"])
    data["Road_Surface_Conditions"] = le.fit_transform(data["Road_Surface_Conditions"])
    data["Pedestrian_Crossing-Human_Control"] = le.fit_transform(data["Pedestrian_Crossing-Human_Control"])
    data["Road_Type"] = le.fit_transform(data["Road_Type"])

    data["Time"] = data["Time"].astype(str)
    data['Time'] = data['Time'].str.slice(0, 2, 1)
    data["Time"] = data["Time"].astype(int)

    data.to_csv("/home/shubham/VIT/EDA/J_Component/pre_processed_accidents_2012_to_2014.csv")
    return data





data = pd.read_csv("/home/shubham/VIT/EDA/J_Component/accidents_2012_to_2014.csv")

data = preprocessing(data)
df = pd.DataFrame(data)
#print(df[['Weather_Conditions', 'Road_Type', 'Light_Conditions', 'Road_Surface_Conditions']])

cas_table = data.groupby(['Day_of_Week']).agg({'Number_of_Casualties':['sum']})
cas_table = cas_table.sort_values([('Number_of_Casualties','sum')],ascending=False)
print(cas_table)

