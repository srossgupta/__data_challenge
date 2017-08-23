from __future__ import print_function
import os
import numpy as np
import pandas as pd

## Add the path of your sample folder 
os.chdir('../data/sampleData/Samples')

#### 2014 - 2016
## DOD Data

# Accessions
DodAccession =pd.read_csv('2014-2016////DOD////Accessions DoD FY2014Q4.txt',
                sep='|', index_col=False,
                names=['Family Name','Given Name','Effective Date','Agency','SubAgency','AccSep','State','Age Range','YSD (Year Since Degree) Range','Education Level','Pay Plan',
                'Grade','LOS (Length of Service) Level','Occupation','Occupational Category (PATCO)','Adjusted Basic Pay','TOA (Type of Appointment)','Work Schedule',
                'NSFTP (Non-Seasonal Full-Time Permanent) Indicator'])

DodAccession.head()
# Separations
DodSeparation =pd.read_csv('2014-2016////DOD////Separations DoD FY2015Q4.txt',
                sep='|', index_col=False, 
                 names=['Family Name','Given Name','Effective Date','Agency','SubAgency','AccSep','State','Age Range','YSD (Year Since Degree) Range','Education Level','Pay Plan',
                'Grade','LOS (Length of Service) Level','Occupation','Occupational Category (PATCO)','Adjusted Basic Pay','TOA (Type of Appointment)','Work Schedule',
                'NSFTP (Non-Seasonal Full-Time Permanent) Indicator'])

print(DodSeparation.head())
# Translations
DodTranslation =pd.read_fwf('2014-2016////DOD////Pay Plan Translation.txt', 
                widths = [22,99,29,16],
                index_col=False)
DodTranslation = DodTranslation.ix[2:]
                
# Status
DodStatus =pd.read_csv('2014-2016////DOD////DoD_201609.txt',
                sep='|', index_col=False, low_memory=False,
                names=['Family Name','Given Name','File Date','Agency','SubAgency','State','Age Range',
                'YSD (Year Since Degree) Range','Education Level','Pay Plan','Grade','LOS (Length of Service) Level',
                'Occupation','Occupational Category (PATCO)','Adjusted Basic Pay','Supervisor','TOA (Type of Appointment)',
                'Work Schedule','NSFTP (Non-Seasonal Full-Time Permanent) Indicator'])
DodStatus.head()
############################################################################################

#### 2014 - 2016
## Non - DOD Data

# Accessions
NonDodAccession =pd.read_csv('2014-2016////Non-DOD////Accessions Non_DoD FY2016Q3.txt',
                sep='|', index_col=False,
                 names=['Family Name','Given Name','Effective Date','Agency','SubAgency','AccSep','State','Age Range','YSD (Year Since Degree) Range','Education Level','Pay Plan',
                'Grade','LOS (Length of Service) Level','Occupation','Occupational Category (PATCO)','Adjusted Basic Pay','TOA (Type of Appointment)','Work Schedule',
                'NSFTP (Non-Seasonal Full-Time Permanent) Indicator'])
                
# Separations
NonDodSeparation =pd.read_csv('2014-2016////Non-DOD////Separations Non_DoD FY2015Q4.txt',
                sep='|', index_col=False,
                 names=['Family Name','Given Name','Effective Date','Agency','SubAgency','AccSep','State','Age Range','YSD (Year Since Degree) Range','Education Level','Pay Plan',
                'Grade','LOS (Length of Service) Level','Occupation','Occupational Category (PATCO)','Adjusted Basic Pay','TOA (Type of Appointment)','Work Schedule',
                'NSFTP (Non-Seasonal Full-Time Permanent) Indicator'])

# Translations
NonDodTranslation =pd.read_fwf('2014-2016////Non-DOD////Pay Plan Translation.txt',
                widths = [22,99,29,16],
                index_col=False)
NonDodTranslation = NonDodTranslation.ix[2:]

# Status
NonDodStatus =pd.read_csv('2014-2016////Non-DOD////Non_DoD_201609.txt',
                sep='|', index_col=False, low_memory=False,
                names=['Family Name','Given Name','File Date','Agency','SubAgency','State','Age Range',
                'YSD (Year Since Degree) Range','Education Level','Pay Plan','Grade','LOS (Length of Service) Level',
                'Occupation','Occupational Category (PATCO)','Adjusted Basic Pay','Supervisor','TOA (Type of Appointment)',
                'Work Schedule','NSFTP (Non-Seasonal Full-Time Permanent) Indicator'])

############################################################################################

#### 1973 - 2014
## DOD Data

# Dynamic
DodDynamic =pd.read_fwf('1973-2014////DOD////Dynamic////SEP1985.DOD.FO05M4.txt',
                widths = [9,23,2,3,9,6,2,2,6,9,4,1,6,2,1],
                index_col=False,
                names=['ID','Name','Agency/SubAgency','Accession/Separation Indicator','Effective Date',
                'Age Range','Pay Plan','Grade','LOS Level','Duty Station','Occupation','Occupation Category',
                'Adjusted Basic Pay','Type of Appointment','Work Schedule'])
                
# Status
DodStatus73 =pd.read_fwf('1973-2014////DOD////Status////Status_DoD_1973_09.txt',
                widths = [9,23,8,4,9,5,3,2,2,6,4,1,6,1,2,1,1],
                index_col=False,
                names=['ID','Name','File Date','Agency/SubAgency Code','Duty Station','Age Range',
                'Education Level','Pay Plan','Grade','LOS Level','Occupation','Occupation Category',
                'Adjusted Basic Pay','Supervisory Status','Type of Appointment','Work Schedule',
                'NonSeasonal Fulltime Payment Indicator'])

############################################################################################

#### 1973 - 2014
## Non - DOD Data

# Dynamic
NonDodDynamic =pd.read_fwf('1973-2014////Non-DOD////Dynamic////JUN1995.NONDOD.FO05M3.txt',
                widths = [9,23,2,3,9,6,2,2,6,9,4,1,6,2,1],
                index_col=False,
                names=['ID','Name','Agency/SubAgency','Accession/Separation Indicator','Effective Date',
                'Age Range','Pay Plan','Grade','LOS Level','Duty Station','Occupation','Occupation Category',
                'Adjusted Basic Pay','Type of Appointment','Work Schedule'])
                
# Status
NonDodStatus73 =pd.read_fwf('1973-2014////Non-DOD////Status////Status_Non_DoD_2014_06.txt',
                widths = [9,23,8,4,9,5,3,2,2,6,4,1,6,1,2,1,1],
                index_col=False,
                names=['ID','Name','File Date','Agency/SubAgency Code','Duty Station','Age Range',
                'Education Level','Pay Plan','Grade','LOS Level','Occupation','Occupation Category',
                'Adjusted Basic Pay','Supervisory Status','Type of Appointment','Work Schedule',
                'NonSeasonal Fulltime Payment Indicator'])

print(NonDodStatus73.head())
system.exit(0)
