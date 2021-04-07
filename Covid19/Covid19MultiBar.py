import pandas as pd
import matplotlib.pyplot as plt
import COVID19Py
import numpy as np

covid19_jhu = COVID19Py.COVID19(data_source="jhu")
latest_jhu = covid19_jhu.getLatest()
locations_ALL = covid19_jhu.getLocations(rank_by='confirmed')


fig = plt.figure(figsize=(10, 10), dpi=300)

countriesCode = ["TW", "IS", "TH", "NZ"]
countries = ["Taiwan", "Iceland", "Thailand", "New Zealand"]
#countriesCode = ["TW", "SB", "BN", "MU"]
#countries = ["Taiwan", "Solomon Islands", "Brunei", "Mauritius"]

LatestItems = ['confirmed', 'recovered', 'deaths']

LatestDict = {}
Confirmed = []
Recovered = []
Deaths = []

itemNum = len(locations_ALL[0]['latest'])
CountriesNum = len(countriesCode)

itemlist = np.arange(0, itemNum)
countrylist = np.arange(0, CountriesNum)


def get_country_latest(location_array, latestItem):
    for location in location_array:
        if (latestItem == 'recovered'):
            if (location['latest']['confirmed'] != 0):
                if (((location['latest'][latestItem] / location['latest']['confirmed']) * 100) > 50.0):
                    print(location['country'], 'recovered=',
                          location['latest'][latestItem], (location['latest'][latestItem] / location['latest']['confirmed']) * 100)
        if (latestItem == 'deaths'):
            if (location['latest']['confirmed'] != 0):
                if (((location['latest'][latestItem] / location['latest']['confirmed']) * 100) > 4.0):
                    print(location['country'], 'deaths=',
                          location['latest'][latestItem], (location['latest'][latestItem] / location['latest']['confirmed']) * 100)
        if (latestItem == 'confirmed'):
            if (location['latest']['confirmed'] < 1500):
                print(location['country'], 'confirmed=',
                      location['latest'][latestItem])


def set_country_latest(location_array, latestItem):
    for country in countriesCode:
        for location in location_array:
            if (location['country_code'] == country):
                if (latestItem == 'recovered'):
                    Recovered.append(location['latest'][latestItem])
                if (latestItem == 'deaths'):
                    Deaths.append(location['latest'][latestItem])
                if (latestItem == 'confirmed'):
                    Confirmed.append(location['latest'][latestItem])
                break
    print('Recovered:', Recovered)
    print('Deaths:', Deaths)
    print('Confirmed:', Confirmed)
    return


# Store data from CSV to dictionary
for idx, data in enumerate(itemlist):
    print(idx, data)
    set_country_latest(locations_ALL, LatestItems[idx])
    #get_country_latest(locations_ALL, LatestItems[idx])

LatestDict['confirmed'] = Confirmed
LatestDict['recovered'] = Recovered
LatestDict['deaths'] = Deaths

df = pd.DataFrame(LatestDict, columns=LatestItems, index=countries)
df.plot.barh()

plt.title('Runtime Covid19 Data')
plt.xlabel('Quantity')
plt.ylabel('Country')
plt.legend(loc='upper right')

# Show graphic
plt.show()
