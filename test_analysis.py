import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.path as mpath
import pandasql as sql
import collections
import os
import glob
import pandasql as sql
from datetime import datetime

#test commit1

#testcase = r"thesis_output\output"

testcase = r"output"
baseDir = r"C:\Users\NImi Jithin\es-m019-m-sc-thesis-nimi-jithin\antgen"
# baseDir = r"F:\NIMI_Studies\MasterThesis\Dataset\Raw_Data\ECO\Data-plug-sm-wise\01_plugs_csv\01"
path = os.path.join(baseDir,testcase)

filenames = []
appliancePowerlist = []
activityPowerlist = []

for filename in os.listdir(path):
    filename = filename.rstrip(".csv")
    if(filename.isupper()):
        appliancePowerlist.append(filename)
    else:
        activityPowerlist.append(filename)
    filenames.append(filename)


print("appliace ===> ", appliancePowerlist)
print("activity ==>", activityPowerlist)





if 'total' in activityPowerlist:
    total = pd.read_csv(path+ r"\total.csv", sep=';',
                           encoding='utf-8', index_col=0, names=['total'])
    total.index = pd.to_datetime(total.index)


# # ############################################################################################################

if 'TV' in appliancePowerlist:
    TV = pd.read_csv(path+ r"\TV.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['TV'])
    TV.index = pd.to_datetime(TV.index)
############################################################################################################

if 'AIREXHAUST' in appliancePowerlist:
    AIREXHAUST = pd.read_csv(path+ r"\AIREXHAUST.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['AIREXHAUST'])
    AIREXHAUST.index = pd.to_datetime(AIREXHAUST.index)
############################################################################################################


if 'IRON' in appliancePowerlist:
    IRON = pd.read_csv(path+ r"\IRON.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['IRON'])
    IRON.index = pd.to_datetime(IRON.index)
## ############################################################################################################
#

if 'STEREO' in appliancePowerlist:
    STEREO = pd.read_csv(path+ r"\STEREO.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['STEREO'])
    STEREO.index = pd.to_datetime(STEREO.index)
## ############################################################################################################

if 'AMPLIFIER' in appliancePowerlist:
    AMPLIFIER = pd.read_csv(path+ r"\AMPLIFIER.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['AMPLIFIER'])
    AMPLIFIER.index = pd.to_datetime(AMPLIFIER.index)
# ############################################################################################################
#
#
if 'VACUUMCLEANER' in appliancePowerlist:
    VACUUMCLEANER = pd.read_csv(path+ r"\VACUUMCLEANER.csv", sep=';',
                       encoding='utf-8', index_col=0, names=['VACUUMCLEANER'])
    VACUUMCLEANER.index = pd.to_datetime(VACUUMCLEANER.index)
# ############################################################################################################
#
if 'COOKINGSTOVE' in appliancePowerlist:
    COOKINGSTOVE = pd.read_csv(path+ r"\COOKINGSTOVE.csv", sep=';',
                       encoding='utf-8', index_col=0, names=['COOKINGSTOVE'])
    COOKINGSTOVE.index = pd.to_datetime(COOKINGSTOVE.index)
# ############################################################################################################
#
if 'DISHWASHER' in appliancePowerlist:
    DISHWASHER = pd.read_csv(path+ r"\DISHWASHER.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['DISHWASHER'])
    DISHWASHER.index = pd.to_datetime(DISHWASHER.index)
# ############################################################################################################

#
if 'COOKER' in appliancePowerlist:
    COOKER = pd.read_csv(path+ r"\COOKER.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['COOKER'])
    COOKER.index = pd.to_datetime(COOKER.index)
# ############################################################################################################


#
if 'BREADCUTTER' in appliancePowerlist:
    BREADCUTTER = pd.read_csv(path+ r"\BREADCUTTER.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['BREADCUTTER'])
    BREADCUTTER.index = pd.to_datetime(BREADCUTTER.index)
# ############################################################################################################
#
if 'COFFEEMAKER' in appliancePowerlist:
    COFFEEMAKER = pd.read_csv(path+ r"\COFFEEMAKER.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['COFFEEMAKER'])
    COFFEEMAKER.index = pd.to_datetime(COFFEEMAKER.index)
# ############################################################################################################
#
if 'MICROWAVE' in appliancePowerlist:
    MICROWAVE = pd.read_csv(path+ r"\MICROWAVE.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['MICROWAVE'])
    MICROWAVE.index = pd.to_datetime(MICROWAVE.index)
############################################################################################################

if 'REFRIGERATOR' in appliancePowerlist:
    REFRIGERATOR = pd.read_csv(path+ r"\REFRIGERATOR.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['REFRIGERATOR'])
    REFRIGERATOR.index = pd.to_datetime(REFRIGERATOR.index)
###########################################################################################################0

if 'DRYER' in appliancePowerlist:
    DRYER = pd.read_csv(path+ r"\DRYER.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['DRYER'])
    DRYER.index = pd.to_datetime(DRYER.index)
##########################################################################################################


if 'FREEZER' in appliancePowerlist:
    FREEZER = pd.read_csv(path+ r"\FREEZER.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['FREEZER'])
    FREEZER.index = pd.to_datetime(FREEZER.index)
##########################################################################################################


if 'KETTLE' in appliancePowerlist:
    KETTLE = pd.read_csv(path+ r"\KETTLE.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['KETTLE'])
    KETTLE.index = pd.to_datetime(KETTLE.index)

###########################################################################################################

if 'CDPLAYER' in appliancePowerlist:
    CDPLAYER = pd.read_csv(path+ r"\CDPLAYER.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['CDPLAYER'])
    CDPLAYER.index = pd.to_datetime(CDPLAYER.index)

###########################################################################################################


if 'PC' in appliancePowerlist:
    PC = pd.read_csv(path+ r"\PC.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['PC'])
    PC.index = pd.to_datetime(PC.index)

###########################################################################################################


if 'PRINTER' in appliancePowerlist:
    PRINTER = pd.read_csv(path+ r"\PRINTER.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['PRINTER'])
    PRINTER.index = pd.to_datetime(PRINTER.index)

###########################################################################################################

if 'TOASTER' in appliancePowerlist:
    TOASTER = pd.read_csv(path+ r"\TOASTER.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['TOASTER'])
    TOASTER.index = pd.to_datetime(TOASTER.index)

###########################################################################################################

if 'use_a_personal_computer' in activityPowerlist:
    COMP = pd.read_csv(path+ r"\use_a_personal_computer.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['COMPUTER'])
    COMP.index = pd.to_datetime(COMP.index)
#
# ###########################################################################################################
#
if 'WASHINGMACHINE' in appliancePowerlist:
    WASHINGMACHINE = pd.read_csv(path+ r"\WASHINGMACHINE.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['WASHINGMACHINE'])
    WASHINGMACHINE.index = pd.to_datetime(WASHINGMACHINE.index)
#
# ###########################################################################################################

if 'cooking_a_dinner' in activityPowerlist:
    cooking_a_dinner = pd.read_csv(path+ r"\cooking_a_dinner.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_cooking_a_dinner'])
    cooking_a_dinner.index = pd.to_datetime(cooking_a_dinner.index)

###########################################################################################################


if 'air_exhaust_operation' in activityPowerlist:
    air_exhaust_operation = pd.read_csv(path+ r"\air_exhaust_operation.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_air_exhaust_operation'])
    air_exhaust_operation.index = pd.to_datetime(air_exhaust_operation.index)

###########################################################################################################



if 'cooker_operation' in activityPowerlist:
    cooker_operation = pd.read_csv(path+ r"\cooker_operation.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_cooker_operation'])
    cooker_operation.index = pd.to_datetime(cooker_operation.index)

###########################################################################################################



if 'cooking_in_stove' in activityPowerlist:
    cooking_in_stove = pd.read_csv(path+ r"\cooking_in_stove.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_cooking_in_stove'])
    cooking_in_stove.index = pd.to_datetime(cooking_in_stove.index)

###########################################################################################################


if 'ironing_clothe' in activityPowerlist:
    ironing_clothe = pd.read_csv(path+ r"\ironing_clothes.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_ironing_clothes'])
    ironing_clothe.index = pd.to_datetime(ironing_clothe.index)

###########################################################################################################



if 'cooking_a_scrambled_egg' in activityPowerlist:
    cooking_a_scrambled_egg = pd.read_csv(path+ r"\cooking_a_scrambled_egg.csv", sep=';',
                    encoding='utf-8', index_col=0, names=['activity_cooking_a_scrambled_egg'])
    cooking_a_scrambled_egg.index = pd.to_datetime(cooking_a_scrambled_egg.index)


###########################################################################################################

if 'preparing_breakfast_with_coffee_or_tea_and_toast_or_egg' in activityPowerlist:
    preparing_breakfast = pd.read_csv(path+ r"\preparing_breakfast_with_coffee_or_tea_and_toast_or_eggs.csv", sep=';',
                    encoding='utf-8', index_col=0, names=['activity_preparing_breakfast'])
    preparing_breakfast.index = pd.to_datetime(preparing_breakfast.index)


###########################################################################################################


if 'dishwasher_operation' in activityPowerlist:
    dishwasher_operation = pd.read_csv(path+ r"\dishwasher_operation.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_dishwasher_operation'])
    dishwasher_operation.index = pd.to_datetime(dishwasher_operation.index)

###########################################################################################################
#
if 'fridge_operation' in activityPowerlist:
    fridge_operation = pd.read_csv(path+ r"\fridge_operation.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_fridge_operation'])
    fridge_operation.index = pd.to_datetime(fridge_operation.index)
##########################################################################################################

if 'freezer_operation' in activityPowerlist:
    freezer_operation = pd.read_csv(path+ r"\freezer_operation.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_freezer_operation'])
    freezer_operation.index = pd.to_datetime(freezer_operation.index)
###########################################################################################################

if 'preparing_coffee' in activityPowerlist:
    preparing_coffee = pd.read_csv(path+ r"\preparing_coffee.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_preparing_coffee'])
    preparing_coffee.index = pd.to_datetime(preparing_coffee.index)
###########################################################################################################


if 'stereo_operation' in activityPowerlist:
    stereo_operation = pd.read_csv(path+ r"\stereo_operation.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_stereo_operation'])
    stereo_operation.index = pd.to_datetime(stereo_operation.index)
###########################################################################################################

if 'preparing_toast' in activityPowerlist:
    preparing_toast = pd.read_csv(path+ r"\preparing_toast.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_preparing_toast'])
    preparing_toast.index = pd.to_datetime(preparing_toast.index)
###########################################################################################################




if 'drying' in activityPowerlist:
    drying = pd.read_csv(path+ r"\drying.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_drying'])
    drying.index = pd.to_datetime(drying.index)
###########################################################################################################



if 'boiling_water' in activityPowerlist:
    boiling_water = pd.read_csv(path+ r"\boiling_water.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_boiling'])
    boiling_water.index = pd.to_datetime(boiling_water.index)
##########################################################################################################

if 'microwaving_food' in activityPowerlist:
    microwaving_food = pd.read_csv(path+ r"\microwaving_food.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_microwaving_food'])
    microwaving_food.index = pd.to_datetime(microwaving_food.index)

###########################################################################################################

if 'vacuuming' in activityPowerlist:
    vacuuming = pd.read_csv(path+ r"\vacuuming.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_vacuuming'])
    vacuuming.index = pd.to_datetime(vacuuming.index)


# ###########################################################################################################
#
if 'washing_a_load_of_laundry' in activityPowerlist:
    washing_a_load_of_laundry = pd.read_csv(path+ r"\washing_a_load_of_laundry.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_washing_a_load_of_laundry'])
    washing_a_load_of_laundry.index = pd.to_datetime(washing_a_load_of_laundry.index)
#
# ###########################################################################################################
#
if 'watching_TV' in activityPowerlist:
    watching_TV = pd.read_csv(path+ r"\watching_TV.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_watching_TV'])
    watching_TV.index = pd.to_datetime(watching_TV.index)

#
# ###########################################################################################################

if 'use_a_personal_computer' in activityPowerlist:
    use_a_personal_computer = pd.read_csv(path+ r"\use_a_personal_computer.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_use_a_personal_computer'])
    use_a_personal_computer.index = pd.to_datetime(use_a_personal_computer.index)

# ###########################################################################################################

if 'preparing_breakfast_with_coffee_and_toast_and_egg' in activityPowerlist:
    preparing_breakfast_with_coffee_and_toast_and_egg = pd.read_csv(path+ r"\preparing_breakfast_with_coffee_and_toast_and_eggs.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['preparing_breakfast_with_coffee_and_toast_and_egg'])
    preparing_breakfast_with_coffee_and_toast_and_egg.index = pd.to_datetime(preparing_breakfast_with_coffee_and_toast_and_egg.index)

###########################################################################################################

if 'preparing_snack' in activityPowerlist:
    preparing_snack = pd.read_csv(path+ r"\preparing_snack.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['preparing_snack'])
    preparing_snack.index = pd.to_datetime(preparing_snack.index)

###########################################################################################################

if 'listen_to_a_74_minute_audio_CD' in activityPowerlist:
    music = pd.read_csv(path+ r"\listen_to_a_74_minute_audio_CD.csv", sep=';',
                        encoding='utf-8', index_col=0, names=['activity_music'])
    music.index = pd.to_datetime(music.index)
# ###########################################################################################################
#
#
#has to change here manually based on the test scenario... copy paste appliance and activities in Notepad and then remove appostrophe using find and replce
## for multilabel classification
final_df = pd.concat([total,AIREXHAUST,COFFEEMAKER,COOKER,COOKINGSTOVE,DRYER,DISHWASHER, FREEZER,
                      IRON, KETTLE,MICROWAVE, REFRIGERATOR,STEREO,TOASTER, TV,VACUUMCLEANER, WASHINGMACHINE,
                      air_exhaust_operation, boiling_water, cooker_operation,
                      cooking_in_stove, dishwasher_operation, drying,
                      ironing_clothe, microwaving_food, freezer_operation, fridge_operation, preparing_coffee,
                      preparing_toast,stereo_operation,vacuuming,
                      washing_a_load_of_laundry, watching_TV], axis=1, join='inner') #PRINTER

# final_df = pd.concat([total,COOKER, COOKINGSTOVE, FREEZER, REFRIGERATOR, STEREO, TV,
#                       cooker_operation,cooking_in_stove, freezer_operation, fridge_operation,
#                       stereo_operation, watching_TV], axis=1, join='inner') #PRINTER

# final_df = pd.concat([total,COFFEEMAKER,COOKINGSTOVE,KETTLE,MICROWAVE, TOASTER,
#                       preparing_breakfast_with_coffee_and_toast_and_egg, preparing_snack], axis=1, join='inner') #PRINTER
#
#
final_df.to_csv("C:/Users/NImi Jithin/es-m019-m-sc-thesis-nimi-jithin/antgen/thesis_output/data_for_model/final_lastMin_simul_model.csv")
# final_df.to_csv("C:/Users/NImi Jithin/es-m019-m-sc-thesis-nimi-jithin/antgen/output/test_data.csv")
# #
# print(len(final_df))
## for multiclass classification

