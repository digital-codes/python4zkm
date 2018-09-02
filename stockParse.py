# quandl stock data
import quandl
import numpy
import matplotlib.pyplot as plt
import private as pr

# you will need to add your key to the private file
quandl.ApiConfig.api_key = pr.quandl_key
quandl.ApiConfig.api_version = '2015-04-09'

# get: database code / dataset code
#data = quandl.get('LBMA/GOLD', start_date='2018-08-01', end_data='2018-09-01', returns='numpy')
data = quandl.get('LBMA/GOLD', start_date='2018-01-01', end_data='2018-09-01')



#print(data)
gdate = [] 
gvalue = []
gx = []
for d in range(len(data)):
    date, value = data.index[d],data["EURO (PM)"][d]
    #print(date,value)
    gdate.append(date)
    gvalue.append(value)
    gx.append(value + 12.5)

#print(gdate,gvalue)
gold = {}
gold["date"] = gdate
gold["value"] = gvalue

plt.ylabel("Gold [€]")
#using original array works
#plt.plot(data.index,data["EURO (PM)"])
#this works too, if iterated over items
plt.plot(gold["date"],gold["value"],label="value")
plt.xlabel("year")
plt.legend()
plt.show()



rural = quandl.get("WWDI/USA_SP_RUR_TOTL")
urban = quandl.get("WWDI/USA_SP_URB_TOTL")
plt.subplot(2, 1, 1)				
plt.plot(rural.index,rural)					
plt.xticks(rural.index[0::3],[])					
plt.title("American Population")					
plt.ylabel("Rural [%]")				
plt.subplot(2, 1, 2)				
plt.plot(urban.index,urban)					
plt.xlabel("year")						
plt.ylabel("Urban [%]")				
plt.show()

           

## European Commission Annual Macro-Economic Database
##
##Annual macro-economic database of the European Commission's Directorate General for Economic and Financial Affairs (DG ECFIN).
##
##    Free
##
##AMECO / FRA_1_0_0_0_ZUTN 	Unemployment rate: total; Member States: definition EUROSTAT - (Percentage of active population) - France
##AMECO / DEU_1_0_0_0_ZUTN 	Unemployment rate: total; Member States: definition EUROSTAT - (Percentage of active population) - Germany
##AMECO / GRC_1_0_0_0_ZUTN 	Unemployment rate: total; Member States: definition EUROSTAT - (Percentage of active population) - Greece

fr = quandl.get("AMECO/FRA_1_0_0_0_ZUTN",start_date="2000-01-01")
de = quandl.get("AMECO/DEU_1_0_0_0_ZUTN",start_date="2000-01-01")
gr = quandl.get("AMECO/GRC_1_0_0_0_ZUTN",start_date="2000-01-01")
plt.subplot(3, 1, 1)				
plt.plot(fr.index,fr)					
plt.xticks(fr.index[0::3],[])					
plt.title("Unemployment rate")					
plt.ylabel("FR [%]")			
plt.subplot(3, 1, 2)				
plt.plot(de.index,de)					
plt.xlabel("year")						
plt.ylabel("DE [%]")				
plt.subplot(3, 1, 3)				
plt.plot(de.index,gr)					
plt.xlabel("year")						
plt.ylabel("GR [%]")				
plt.show()

