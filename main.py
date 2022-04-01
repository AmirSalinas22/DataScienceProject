import numpy as np
import pandas as pd


militaryExpenditure_TL = pd.read_csv("Military_Expenditure_1960-2019.csv")
population_TL = pd.read_csv("Population_1960-2019.csv")
gdp_TL = pd.read_csv("GDP_1960-2019.csv")

print(gdp_TL)







####################################################################################################
#  OLD Data

# Gets...cell (Row x Column)
#dataPop = countryPopTot.loc[countryPopTot['Country Name'] == 'United States']
# Row's Column (cell)
#dataYear = dataPop.iloc[0]['2018']
#print(dataPop) # Row data
#print(dataYear) # cell
# Ukraine(246), United States(249), Russia(200), China(38), India(107)
# Print
#print(countryLandTot.iloc[246])
#print(countryPopTot.iloc[38])
#print(countryMilExp.iloc[249])

################################################################################################################
