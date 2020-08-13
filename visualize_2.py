import datetime as dt
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')
matplotlib.use('tkagg')


accidents = pd.read_csv('/home/shubham/VIT/EDA/J_Component/UK_Accident/Preprocessesed_data/pre_processed_accidents_junction_control.csv', index_col='Accident_Index')

objects = ['Not at junction or within 20 metres', 'Authorised person', 'Auto traffic signal', 'Stop sign', 'Give way or uncontrolled']
plt.figure(figsize=(12,6))
accidents.Junction_Control.hist(bins=5, rwidth=0.55, alpha=0.5, color='blue')
plt.title('Accident analysis based on Junction Control', fontsize=30)
plt.grid(False)
y_pos = np.arange(len(objects))
plt.xticks(y_pos, objects)
plt.ylabel('Accident count', fontsize=20)
plt.xlabel('Road Surface Condition', fontsize = 13)
plt.show()