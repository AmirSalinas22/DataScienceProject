import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def PlotCountry(country, color, num, topic):
    ##### DATA EXTRACTION/MINIPULATION #####
    countryPlot = plt
    plotTitle = country.iloc[0][0]
    country = country.iloc[:, 2:60]
    country = np.array(country).flatten()
    country = np.reshape(country, 58)
    years = range(1960, 2019)
    countryGDP_TL = pd.DataFrame(list(zip(years, country)))
    countryGDP_TL.columns = ['Year', 'Value']
    # print(countryGDP_TL.shape)
    # print(countryGDP_TL)

    ##### PLOT #####
    countryPlot.figure(num)  # COMMENT OUT IF YOU WANT TO SHOW MULTIPLE COUNTRIES IN A SINGLE FIGURE
    countryPlot.plot(countryGDP_TL['Year'], countryGDP_TL['Value'], color=color, label=plotTitle)
    # countryPlot.legend(plotTitle) # DOESNT WORK FOR IF YOU HAVE MULTIPLE FIGURE IN ONE
    countryPlot.title(plotTitle + ' ' + topic)
    countryPlot.xlabel("Year")
    countryPlot.xlim(1960, 2019)
    countryPlot.ylabel(topic + " (US$)")
    return countryPlot


##################### START #####################


###### DATA/DATASETS ######
militaryExpenditure_TL = pd.read_csv("Military_Expenditure_1960-2019.csv")
population_TL = pd.read_csv("Population_1960-2019.csv")
gdp_TL = pd.read_csv("GDP_1960-2019.csv")

### NOTE* BETTER VARIABLE DISTRUBUTION E.g. Country Object ({data, color, Name,})

####### GLOBAL VALUES ######## (might change this)

gdp_Color = 'red'
militaryExpediture_Color = 'black'
population_Color = 'blue'

############# COUNTRIES GDP ##############

###### USA GDP GROWTH ######
usaGDP_TL = gdp_TL.loc[gdp_TL['Country Name'] == 'United States']
PlotCountry(usaGDP_TL, gdp_Color, 1, 'GDP')

###### CHINA GDP GROWTH ######
chinaGDP_TL = gdp_TL.loc[gdp_TL['Country Name'] == 'China']
PlotCountry(chinaGDP_TL, gdp_Color, 2, 'GDP')

###### RUSSIAN GDP GROWTH ######
russiaGDP_TL = gdp_TL.loc[gdp_TL['Country Name'] == 'Russian Federation']
PlotCountry(russiaGDP_TL, gdp_Color, 3, 'GDP')

###### INDIA GDP GROWTH ######
indiaGDP_TL = gdp_TL.loc[gdp_TL['Country Name'] == 'India']
PlotCountry(indiaGDP_TL, gdp_Color, 4, 'GDP')

###### GERMANY GDP GROWTH ######
germanyGDP_TL = gdp_TL.loc[gdp_TL['Country Name'] == 'Germany']
PlotCountry(germanyGDP_TL, gdp_Color, 5, 'GDP')

plt.show()

############## Military Expenditures ##################

###### USA MILITARY EXPENDITURES GROWTH ######
usaME_TL = militaryExpenditure_TL.loc[militaryExpenditure_TL['Country Name'] == 'United States']
PlotCountry(usaME_TL, militaryExpediture_Color, 1, 'Military Expenditures')

###### CHINA MILITARY EXPENDITURES GROWTH ######
chinaME_TL = militaryExpenditure_TL.loc[militaryExpenditure_TL['Country Name'] == 'China']
PlotCountry(chinaME_TL, militaryExpediture_Color, 2, 'Military Expenditures')

###### RUSSIAN MILITARY EXPENDITURES GROWTH ######
russiaME_TL = militaryExpenditure_TL.loc[militaryExpenditure_TL['Country Name'] == 'Russian Federation']
PlotCountry(russiaME_TL, militaryExpediture_Color, 3, 'Military Expenditures')

###### INDIA MILITARY EXPENDITURES GROWTH ######
indiaME_TL = militaryExpenditure_TL.loc[militaryExpenditure_TL['Country Name'] == 'India']
PlotCountry(indiaME_TL, militaryExpediture_Color, 4, 'Military Expenditures')

###### GERMANY MILITARY EXPENDITURES GROWTH ######
germanyME_TL = militaryExpenditure_TL.loc[militaryExpenditure_TL['Country Name'] == 'Germany']
PlotCountry(germanyME_TL, militaryExpediture_Color, 5, 'Military Expenditures')

plt.show()

###### USA POPULATION GROWTH ######
usaPop_TL = population_TL.loc[population_TL['Country Name'] == 'United States']
PlotCountry(usaPop_TL, population_Color, 1, 'Population')

###### CHINA POPULATION GROWTH ######
chinaPop_TL = population_TL.loc[population_TL['Country Name'] == 'China']
PlotCountry(chinaPop_TL, population_Color, 2, 'Population')

###### RUSSIAN POPULATION GROWTH ######
russiaPop_TL = population_TL.loc[population_TL['Country Name'] == 'Russian Federation']
PlotCountry(russiaPop_TL, population_Color, 3, 'Population')

###### INDIA POPULATION GROWTH ######
indiaPop_TL = population_TL.loc[population_TL['Country Name'] == 'India']
PlotCountry(indiaPop_TL, population_Color, 4, 'Population')

###### GERMANY POPULATION GROWTH ######
germanyPop_TL = militaryExpenditure_TL.loc[militaryExpenditure_TL['Country Name'] == 'Germany']
PlotCountry(germanyPop_TL, population_Color, 5, 'Population')

plt.show()
