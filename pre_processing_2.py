import pandas as pd

casualties = pd.read_csv('/home/shubham/VIT/EDA/J_Component/UK_Accident/Casualties0515.csv' , error_bad_lines=False,index_col='Accident_Index',warn_bad_lines=False)

casualties.drop(['Pedestrian_Road_Maintenance_Worker', 'Casualty_Home_Area_Type', 'Pedestrian_Location', 'Pedestrian_Movement'], axis=1, inplace=True)

casualties = casualties[casualties.Sex_of_Casualty != -1]
casualties = casualties[casualties.Age_of_Casualty != -1]
casualties = casualties[casualties.Age_Band_of_Casualty != -1]
casualties = casualties[casualties.Casualty_Severity != -1]
casualties = casualties[casualties.Car_Passenger != -1]
casualties = casualties[casualties.Bus_or_Coach_Passenger != -1]
casualties = casualties[casualties.Casualty_Type != -1]

casualties.to_csv("/home/shubham/VIT/EDA/J_Component/UK_Accident/Preprocessesed_data/pre_processed_casualties.csv")