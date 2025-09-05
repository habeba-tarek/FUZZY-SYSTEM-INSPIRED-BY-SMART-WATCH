#!/usr/bin/env python
# coding: utf-8

# In[17]:


pip install scikit-fuzzy


# In[51]:


import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl
import population
from deap import base, creator, tools, algorithms
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# In[52]:


# Create fuzzy variables
BP=ctrl.Antecedent(np.arange(80, 181, 1), 'BP')
TEMP=ctrl.Antecedent(np.arange(98, 107, 1), 'TEMP')
Age = ctrl.Antecedent(np.arange(20, 80.1, 1), 'Age')
O2_percentage= ctrl.Antecedent(np.arange(80, 100.1, 1), 'O2_percentage')
Sleep_quality= ctrl.Antecedent(np.arange(1, 12.1, 1), 'Sleep_quality')
Heart_rate=ctrl.Antecedent(np.arange(40, 130.1, 1), 'Heart_rate')
HealthCondition = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'HealthCondition')


# In[53]:


# Define membership functions for Blood Pressure
BP['Normal'] = fuzz.trimf(BP.universe, [80, 100, 120])
BP['Pre_Hypertension'] = fuzz.trimf(BP.universe, [90, 115, 140])
BP['High_BP_Stage_1'] = fuzz.trimf(BP.universe, [100, 130, 160])
BP['High_BP_Stage_2'] = fuzz.trimf(BP.universe, [110, 140, 170])
BP['Emergency'] = fuzz.trimf(BP.universe, [130, 155, 180])


# In[54]:


# Define membership functions for Temperature
TEMP['Low'] = fuzz.trimf(TEMP.universe, [98, 98, 100])
TEMP['Temp'] = fuzz.trimf(TEMP.universe, [100, 101, 101])
TEMP['Temp_High_1'] = fuzz.trimf(TEMP.universe, [101, 102, 102])
TEMP['Temp_High_2'] = fuzz.trimf(TEMP.universe, [102, 103, 104])
TEMP['Emergency'] = fuzz.trimf(TEMP.universe, [104, 105, 106])


# In[55]:


# Define membership functions for Age
Age['Young'] = fuzz.trimf(Age.universe, [20, 20, 40])
Age['Middle_Aged'] = fuzz.trimf(Age.universe, [30, 50, 70])
Age['Old'] = fuzz.trimf(Age.universe, [60, 70, 80])


# In[56]:


# Define membership functions for O2_percentage
O2_percentage['Low'] = fuzz.trimf(O2_percentage.universe, [80, 85, 90])
O2_percentage['Medium'] = fuzz.trimf(O2_percentage.universe, [85, 90, 95])
O2_percentage['High'] = fuzz.trimf(O2_percentage.universe, [90, 95, 100])


# In[57]:


# Define membership functions for Sleep_quality
Sleep_quality['Poor'] = fuzz.trimf(Sleep_quality.universe, [1, 3, 6])
Sleep_quality['Average'] = fuzz.trimf(Sleep_quality.universe, [4, 6, 8])
Sleep_quality['Good'] = fuzz.trimf(Sleep_quality.universe, [6, 9, 12])


# In[58]:


# Define membership functions for Heart_rate
Heart_rate['Low'] = fuzz.trimf(Heart_rate.universe, [40, 50, 60])
Heart_rate['Normal'] = fuzz.trimf(Heart_rate.universe, [50, 75, 100])
Heart_rate['High'] = fuzz.trimf(Heart_rate.universe, [90, 110, 130])


# In[59]:


# Define membership functions for Health Condition
HealthCondition['Worst'] = fuzz.trimf(HealthCondition.universe, [0, 0.2, 0.4])
HealthCondition['Normal'] = fuzz.trimf(HealthCondition.universe, [0.3, 0.5, 0.7])
HealthCondition['Good'] = fuzz.trimf(HealthCondition.universe, [0.6, 0.8, 1])


# In[60]:


# Plot the membership functions for Blood Pressure
BP.view()
plt.title('Blood Pressure Membership Functions')
plt.show()


# In[61]:


# Plot the membership functions for Temperature
TEMP.view()
plt.title('Temperature Membership Functions')
plt.show()


# In[62]:


# Plot the membership functions for Age
Age.view()
plt.title('Age Membership Functions')
plt.show()


# In[63]:


# Plot the membership functions for O2_percentage
O2_percentage.view()
plt.title('O2_percentage Membership Functions')
plt.show()


# In[64]:


# Plot the membership functions for Sleep_quality
Sleep_quality.view()
plt.title('Sleep_quality Membership Functions')
plt.show()


# In[65]:


# Plot the membership functions for Heart_rate 
Heart_rate.view()
plt.title('Heart_rate Membership Functions')
plt.show()


# In[66]:


# Plot the membership functions for Health Condition 
HealthCondition.view()
plt.title('Health Condition Membership Functions')
plt.show()


# In[107]:


# Define rules
rule1 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Good'])
rule2 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule3 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule4 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule5 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule6 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule7 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule8 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule9 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Old'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule10 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule11 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule12 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule13 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule14 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule15 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule16 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule17 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule18 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule19 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule20 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule21 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule22 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['High'], HealthCondition['Normal'])
rule23 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Worst'])
rule24 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule25 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule26 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Good'])
rule27 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Old'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule28 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule29 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule30 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule31 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule32 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule33 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule34 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule35 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule36 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule37 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Old'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule38 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Normal'])
rule39 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule40 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule41 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule42 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Low'], HealthCondition['Normal'])
rule43 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule44 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule45 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule46 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule47 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Old'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule48 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Normal'])
rule49 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule50 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule51 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule52 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule53 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule54 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule55 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule56 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule57 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Old'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule58 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Normal'])
rule59 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule60 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule61 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule62 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule63 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule64 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule65 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule66 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule67 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Old'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule68 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Normal'])
rule69 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule70 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule71 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule72 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule73 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule74 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule75 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule76 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule77 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Old'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule78 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Normal'])
rule79 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule80 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule81 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule82 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule83 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule84 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule85 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule86 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule87 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Old'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule88 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Normal'])
rule89 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule90 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule91 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule92 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule93 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule94 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule95 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule96 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule97 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Old'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule98 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Normal'])
rule99 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule100 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule101 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule102 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule103 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule104 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule105 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule106 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule107 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Old'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule108 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Normal'])
rule109 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule110 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule111 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule112 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['High'], HealthCondition['Normal'])
rule113 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule114 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule115 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule116 = ctrl.Rule(BP['Normal'] & TEMP['Low'] & Age['Middle_Aged'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Good'])
rule117 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Old'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule118 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule119 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule120 = ctrl.Rule(BP['High_BP_Stage_1'] & TEMP['Temp_High_1'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule121 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule122 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule123 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule124 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule125 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Young'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule126 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule127 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['High'], HealthCondition['Normal'])
rule128 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule129 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule126 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule127 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['High'], HealthCondition['Normal'])
rule128 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule129 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule130 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule131 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule132 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule133 = ctrl.Rule(BP['Emergency'] & TEMP['Emergency'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Low'], HealthCondition['Worst'])
rule134 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule135 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['High'], HealthCondition['Normal'])
rule136 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule137 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule138 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule139 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule140 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule141 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['High'], HealthCondition['Normal'])
rule142 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule143 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule144 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule145 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Normal'], HealthCondition['Normal'])
rule146 = ctrl.Rule(BP['Normal'] & TEMP['Temp'] & Age['Young'] & O2_percentage['High'] & Sleep_quality['Good'] & Heart_rate['High'], HealthCondition['Normal'])
rule147 = ctrl.Rule(BP['Pre_Hypertension'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Medium'] & Sleep_quality['Average'] & Heart_rate['High'], HealthCondition['Normal'])
rule148 = ctrl.Rule(BP['High_BP_Stage_2'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Medium'] & Sleep_quality['Good'] & Heart_rate['Low'], HealthCondition['Normal'])
rule149 = ctrl.Rule(BP['Emergency'] & TEMP['Temp'] & Age['Middle_Aged'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['High'], HealthCondition['Worst'])
rule150 = ctrl.Rule(BP['Emergency'] & TEMP['Temp_High_2'] & Age['Old'] & O2_percentage['Low'] & Sleep_quality['Poor'] & Heart_rate['Normal'], HealthCondition['Worst'])
rule151 = ctrl.Rule((BP['Normal'] & TEMP['Low'] & Age['Young']),HealthCondition['Good'])


# In[108]:


# Create control system
# Include the additional rules in the ControlSystem
bptemp_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, 
                                  rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, 
                                  rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, 
                                  rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, 
                                  rule38, rule39,rule40, rule41, rule42, rule43, rule44,rule45, rule46, rule47, 
                                  rule48, rule49, rule50,rule51, rule52, rule53, rule54, rule55, rule56,
                                  rule57, rule58, rule59, rule60, rule61, rule62,rule63, rule64, rule65,
                                  rule66, rule76, rule68, rule79, rule70, rule71, rule72, rule73, rule74, rule75,
                                  rule76, rule77, rule78, rule79, rule80,rule81, rule82, rule83, rule84, rule85, 
                                  rule86, rule87, rule88, rule89, rule90,
                                  rule91, rule92, rule93, rule94, rule95, rule96, rule97, rule98, rule99, rule100,
                                  rule101, rule102, rule103, rule104, rule105, rule106, rule107, rule108, rule109,
                                  rule110, rule111, rule112, rule113, rule114, rule115, rule116, rule117, rule118,
                                  rule119, rule120, rule121, rule122, rule123, rule124, rule125, rule126, rule127,
                                  rule128, rule129, rule130, rule131, rule132, rule133, rule134, rule135, rule136,
                                  rule137, rule138, rule139, rule140, rule141, rule142, rule143, rule144, rule145,
                                  rule146, rule147, rule148, rule149, rule150,rule151])

health_classification = ctrl.ControlSystemSimulation(bptemp_ctrl)


# In[109]:


print(len(HealthCondition.universe))


# In[115]:


health_classification.input['BP'] = 130 
health_classification.input['TEMP'] = 102
health_classification.input['Age'] = 45
health_classification.input['O2_percentage'] = 92 
health_classification.input['Sleep_quality'] = 7
health_classification.input['Heart_rate'] = 80

# Crunch the numbers
health_classification.compute()

# Defuzzify using centroid method
health_result = (HealthCondition.defuzzify_method=='centroid')

# Print the result
print("Health Condition:", health_result)
print("Health Condition:", health_classification.output['HealthCondition'])


# In[114]:


# Plot the result
HealthCondition.view(sim=health_classification)
plt.title('Inferred Health Condition')
plt.show()


# In[90]:


# Plot the result
BP.view(sim=health_classification)
plt.title('Inferred Blood Pressure')
plt.show()


# In[91]:


# Plot the result
TEMP.view(sim=health_classification)
plt.title('Inferred Temperture')
plt.show()


# In[92]:


# Plot the result
Age.view(sim=health_classification)
plt.title('Inferred Age')
plt.show()


# In[93]:


# Plot the result
O2_percentage.view(sim=health_classification)
plt.title('Inferred O2_percentage')
plt.show()


# In[94]:


# Plot the result
Sleep_quality.view(sim=health_classification)
plt.title('Inferred Sleep_quality')
plt.show()


# In[95]:


# Plot the result
Heart_rate.view(sim=health_classification)
plt.title('Inferred Heart_rate')
plt.show()


# In[ ]:





# In[ ]:




