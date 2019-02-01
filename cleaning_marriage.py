#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:03:17 2019

@author: BrianHayes
"""

import pandas as pd
import re

marriage = pd.read_excel('state_marriagerates.xlsx',
                      skiprows =3, ###skips the first three rows of metadata
                      header =[1,2],  ## makes the header the second and third row
                      skipfooter=7,  ## skips the metadata footer at the bottom
                      na_values='(NA)',  
                      usecols=25, ### makes the dataframe contain the first 25 columns which is the entire data set
                      index_col=[0]) 


                       


            

marriage.dropna(how='all', inplace=True)

marriage = marriage.stack([0,1]).reset_index()

### renames the columns to match the data that appears in that column
marriage.rename(columns={marriage.columns[0] : 'State',
                       marriage.columns[1] : 'Marriage rate',
                       marriage.columns[2]:'Year',
                       marriage.columns[3]: 'Rate'}
                       , inplace=True)   



   ##### exports data  to a new excel file 
marriage.to_excel(excel_writer='state_marriagerates_clean.xls', 
                  sheet_name='marriage', 
                  na_rep='null',)


                  

