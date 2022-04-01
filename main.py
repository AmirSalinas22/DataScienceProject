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
    #countryPlot.figure(num) # COMMENT OUT IF YOU WANT TO SHOW MULTIPLE COUNTRIES IN A SINGLE FIGURE
    countryPlot.plot(countryGDP_TL['Year'], countryGDP_TL['Value'], color= color, label = plotTitle)
    # countryPlot.legend(plotTitle) # DOESNT WORK FOR IF YOU HAVE MULTIPLE FIGURE IN ONE
    countryPlot.title(plotTitle + ' ' + topic)
    countryPlot.xlabel("Year")
    countryPlot.xlim(1960, 2019)
    countryPlot.ylabel( topic + " (US$)")
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

    ########## COUNTRIES GDP ##########

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
PlotCountry(usaGDP_TL, militaryExpediture_Color, 1, 'Military Expenditures')

    ###### CHINA MILITARY EXPENDITURES GROWTH ######
chinaME_TL = militaryExpenditure_TL.loc[militaryExpenditure_TL['Country Name'] == 'China']
PlotCountry(chinaGDP_TL, militaryExpediture_Color, 2, 'Military Expenditures')

    ###### RUSSIAN MILITARY EXPENDITURES GROWTH ######
russiaME_TL = militaryExpenditure_TL.loc[militaryExpenditure_TL['Country Name'] == 'Russian Federation']
PlotCountry(russiaGDP_TL, militaryExpediture_Color, 3, 'Military Expenditures')

    ###### INDIA GDP GROWTH ######
indiaME_TL = militaryExpenditure_TL.loc[militaryExpenditure_TL['Country Name'] == 'India']
PlotCountry(indiaGDP_TL, militaryExpediture_Color, 4, 'Military Expenditures')

    ###### GERMANY MILITARY EXPENDITURES GROWTH ######
germanyME_TL = militaryExpenditure_TL.loc[militaryExpenditure_TL['Country Name'] == 'Germany']
PlotCountry(germanyGDP_TL, militaryExpediture_Color, 5, 'Military Expenditures')

plt.show()