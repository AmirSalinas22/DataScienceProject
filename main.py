import numpy as np
import pandas as pd

print("start")

# Data
# Growth between 1960 to ~2019
countryLandTot = pd.read_csv("API_AG.LND.TOTL.K2_DS2_en_csv_v2_511817.csv")
countryPopTot = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_511378.csv")


# Current




# Ukraine(246), United States(249), Russia(200), China(38), India(107)
# Print
print(countryLandTot.iloc[246]) # Ukraine(246)
print(countryPopTot.iloc[38])