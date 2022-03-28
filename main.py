import numpy as np
import pandas as pd



# Data
# Growth between 1960 to ~2019
countryLandTot = pd.read_csv("API_AG.LND.TOTL.K2_DS2_en_csv_v2_511817.csv")
countryPopTot = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_511378.csv")
# Countries GDP USD
countryGDPTotUSD = pd.read_csv("API_NY.GDP.MKTP.CD_DS2_en_csv_v2_559588.csv")
# Military Expenditure Percentage
countryMilExp = pd.read_csv("API_MS.MIL.XPND.GD.ZS_DS2_en_csv_v2_511529.csv")

# Current
######################


dataPop = countryPopTot.loc[countryPopTot['Country Name'] == 'United States']
dataYear = dataPop.iloc[0]['2008']
print(dataPop)
print(dataYear)


# Ukraine(246), United States(249), Russia(200), China(38), India(107)
# Print
print(countryLandTot.iloc[246])
print(countryPopTot.iloc[38])
print(countryMilExp.iloc[249])