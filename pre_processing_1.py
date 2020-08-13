
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')

accidents = pd.read_csv('/home/shubham/VIT/EDA/J_Component/UK_Accident/Accidents0515.csv',index_col='Accident_Index')

#vehicles=pd.read_csv('/home/shubham/VIT/EDA/J_Component/UK_Accident/Vehicles0515.csv', error_bad_lines=False,index_col='Accident_Index',warn_bad_lines=False)

accidents.drop(['Location_Easting_OSGR', 'Location_Northing_OSGR', 'LSOA_of_Accident_Location',
                'Junction_Control', '2nd_Road_Class', 'Local_Authority_(District)', 'Local_Authority_(Highway)', 'Junction_Detail', 'Special_Conditions_at_Site',
                'Carriageway_Hazards', 'Urban_or_Rural_Area', 'Did_Police_Officer_Attend_Scene_of_Accident'], axis=1, inplace=True)



accidents = accidents[accidents.Police_Force != -1]
accidents = accidents[accidents.Accident_Severity != -1]
accidents = accidents[accidents.Number_of_Vehicles != -1]
accidents = accidents[accidents.Number_of_Casualties != -1]
accidents = accidents[accidents.Day_of_Week != -1]
accidents = accidents[accidents.Day_of_Week != -1]
accidents = accidents[accidents.Road_Type != -1]
accidents = accidents[accidents.Speed_limit != -1]
accidents = accidents[accidents.Light_Conditions != -1]
accidents = accidents[accidents.Weather_Conditions != -1]
accidents = accidents[accidents.Road_Surface_Conditions != -1]

accidents.to_csv("/home/shubham/VIT/EDA/J_Component/UK_Accident/Preprocessesed_data/pre_processed_accidents.csv")