import datetime as dt
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import TimeSeriesSplit, train_test_split
from sklearn.tree import DecisionTreeClassifier

plt.style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')
matplotlib.use('tkagg')

"""df1 = pd.read_csv('/home/shubham/VIT/EDA/J_Component/UK_Accident/Preprocessesed_data/pre_processed_accidents.csv', error_bad_lines=False, index_col='Accident_Index', warn_bad_lines=False);
print(df1.corr(method="pearson"));"""

accidents = pd.read_csv('/home/shubham/VIT/SEM_1/EDA/J_Component/UK_Accident/Preprocessesed_data/pre_processed_accidents.csv', index_col='Accident_Index')
vehicles = pd.read_csv('/home/shubham/VIT/SEM_1/EDA/J_Component/UK_Accident/Preprocessesed_data/Vehicles0515.csv', error_bad_lines=False, index_col='Accident_Index', warn_bad_lines=False)

#corr_matrix = accidents.corr()
#print(corr_matrix["Accident_Severity"].sort_values(ascending=False))

accidents = accidents.join(vehicles, how='outer')
accidents['Date_time'] =  accidents['Date'] +' '+ accidents['Time']
for col in accidents.columns:
    accidents['Date_time'] = pd.to_datetime(accidents.Date_time)

accidents.drop(['Date','Time'],axis =1 , inplace=True)
accidents.dropna(inplace=True)
accident_ml = accidents.drop('Accident_Severity' ,axis=1)
accident_ml = accident_ml[['Age_of_Driver' ,'Vehicle_Type', 'Age_of_Vehicle','Engine_Capacity_(CC)','Day_of_Week' , 'Weather_Conditions' , 'Road_Surface_Conditions'
                          , 'Light_Conditions', 'Sex_of_Driver' ,'Speed_limit']]

# Split the data into a training and test set.
X_train, X_test, y_train, y_test = train_test_split(accident_ml.values,
                                              accidents['Accident_Severity'].values,test_size=0.20, random_state=99)

"""random_forest = RandomForestClassifier(n_estimators=200)
random_forest.fit(X_train,y_train)
Y_pred = random_forest.predict(X_test)
random_forest.score(X_test, y_test)
acc_random_forest1 = round(random_forest.score(X_test, y_test) * 100, 2)

sk_report = classification_report(
    digits=6,
    y_true=y_test,
    y_pred=Y_pred)
print("Accuracy" , acc_random_forest1)
print(sk_report)
pd.crosstab(y_test, Y_pred, rownames=['Actual'], colnames=['Predicted'], margins=True)"""

"""lr = LogisticRegression()
# Fit the model on the trainng data.
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
sk_report = classification_report(
    digits=6,
    y_true=y_test,
    y_pred=y_pred)
print("Accuracy", round(accuracy_score(y_pred, y_test)*100,2))
print(sk_report)
pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'], margins=True)"""

"""plt.figure(figsize=(12,6))
feat_importances = pd.Series(lr.feature_importances_, index=accident_ml.columns)
feat_importances.nlargest(5).plot(kind='barh')"""

decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, y_train)
Y_pred = decision_tree.predict(X_test)
acc_decision_tree1 = round(decision_tree.score(X_test, y_test) * 100, 2)
sk_report = classification_report(
    digits=6,
    y_true=y_test,
    y_pred=Y_pred)
print("Accuracy", acc_decision_tree1)
print(sk_report)
### Confusion Matrix
print(pd.crosstab(y_test, Y_pred, rownames=['Actual'], colnames=['Predicted'], margins=True))
