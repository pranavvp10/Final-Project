# Importing useful libraries
import numpy as np
import pandas as pd
from collections import OrderedDict
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
import collections


#tranfer market value prediction
def player_prediction(training_file,input_set):


    data_path= training_file#'data.csv'
    model_data = pd.read_csv(data_path) #loading csv file and using it as dataframe using pandas
    model_data.drop(['ID'], axis=1, inplace=True)
    model_data.drop(['overall'], axis=1, inplace=True)
    model_data.drop(['player_positions'], axis=1, inplace=True)


    target_name = 'value_eur'  #variable to be predicted or estimated
    X = model_data.drop('value_eur', axis=1)
    y = model_data[target_name]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123) #splitiing data into training set and test set

    #Ridge Regreesion
    ridge_regression = Ridge() #assinging ridge regression function to ridge_regression or( making it as an object)
    ridge_regression.fit(X_train, y_train) #fiting the training data and training.(learning process happen here)


    head_set=['age','height_cm','weight_kg','weak_foot','skill_moves','attacking_crossing',
          'attacking_finishing','attacking_heading_accuracy','attacking_short_passing','attacking_volleys','skill_dribbling',
          'skill_curve','skill_fk_accuracy','skill_long_passing','skill_ball_control','movement_acceleration',
          'movement_sprint_speed','movement_agility','movement_reactions','movement_balance','power_shot_power',
          'power_jumping','power_stamina','power_strength','power_long_shots','mentality_aggression','mentality_interceptions',
          'mentality_positioning','mentality_vision','mentality_penalties','mentality_composure','defending_marking',
          'defending_standing_tackle','defending_sliding_tackle','goalkeeping_diving','goalkeeping_handling','goalkeeping_kicking',
          'goalkeeping_positioning','goalkeeping_reflexes']
    #input_set=[32,170,72,4,4,88,95,70,92,88,97,93,94,92,96,91,84,93,95,95,86,68,75,68,94,48,40,94,94,75,96,33,37,26,6,11,15,14,8]
    new_data = collections.OrderedDict()
    i=0
    for h in head_set:
        new_data[h]=input_set[i]
        i =i+1
    new_data = pd.Series(new_data).values.reshape(1,-1)
    return ridge_regression.predict(new_data)[0] #returning the predicted transfer  value for given input data



#overall performance prediction
def player_prediction2(training_file,input_set):


    data_path= training_file#'data.csv'
    model_data = pd.read_csv(data_path)
    model_data.head()
    model_data.drop(['ID'], axis=1, inplace=True)
    model_data.drop(['value_eur'], axis=1, inplace=True)
    model_data.drop(['player_positions'], axis=1, inplace=True)


    target_name = 'overall' #variable to be predicted or estimated
    X = model_data.drop('overall', axis=1)
    y = model_data[target_name]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)


    #Ridge Regreesion
    ridge_regression = Ridge()
    ridge_regression.fit(X_train, y_train)



    head_set=['age','height_cm','weight_kg','weak_foot','skill_moves','attacking_crossing',
          'attacking_finishing','attacking_heading_accuracy','attacking_short_passing','attacking_volleys','skill_dribbling',
          'skill_curve','skill_fk_accuracy','skill_long_passing','skill_ball_control','movement_acceleration',
          'movement_sprint_speed','movement_agility','movement_reactions','movement_balance','power_shot_power',
          'power_jumping','power_stamina','power_strength','power_long_shots','mentality_aggression','mentality_interceptions',
          'mentality_positioning','mentality_vision','mentality_penalties','mentality_composure','defending_marking',
          'defending_standing_tackle','defending_sliding_tackle','goalkeeping_diving','goalkeeping_handling','goalkeeping_kicking',
          'goalkeeping_positioning','goalkeeping_reflexes']
    #input_set=[32,170,72,4,4,88,95,70,92,88,97,93,94,92,96,91,84,93,95,95,86,68,75,68,94,48,40,94,94,75,96,33,37,26,6,11,15,14,8]
    new_data = collections.OrderedDict()
    i=0
    for h in head_set:
        new_data[h]=input_set[i]
        i =i+1
    new_data = pd.Series(new_data).values.reshape(1,-1)
    return ridge_regression.predict(new_data)[0]




