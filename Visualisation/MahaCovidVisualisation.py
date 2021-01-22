#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
#Plot 1
data = pd.read_csv('MahaCovid.csv') #Converts the csv data scraped from Covid India into a DataFrame
ac=data.iloc[:35,4].values #ac active cases
re=data.iloc[:35,2].values #re recovered
de=data.iloc[:35,3].values #de deceased
x=list(data.iloc[:35,0]) #District names
  
plt.figure(figsize=(30,10))
ax=plt.axes() 
ax.set_facecolor('black') 
ax.grid(linewidth=0.4, color='#8f8f8f') 
  
plt.xticks(rotation='vertical', size='20',color='black')
plt.yticks(size='20',color='black') 
  
ax.set_xlabel('\nDistrict', size=30, color='#4bb4f2') 
ax.set_ylabel('Total no. of cases\n', size=30, color='#4bb4f2') 
ax.set_title('Maharashtra district wise breakdown\n',size=50,color='#28a9ff') 

b_re=list(np.add(de,ac)) #plotting a stacked bar
plt.bar(x,re,bottom=b_re,color='green',label="Recovered")
plt.bar(x,ac, bottom =de,color='blue',label="Active") 
plt.bar(x,de,color='red',label="Deceased") 


plt.legend(fontsize=20)
plt.show() #stacked bar plot showing district wise case distribution

#Plot 2
plt.figure(figsize=(30,10))#more granular visualisation of the active cases
ax=plt.axes() 
ax.set_facecolor('black') 
ax.grid(linewidth=0.4, color='#8f8f8f') 
  
plt.xticks(rotation='vertical', size='20',color='black')
plt.yticks(size='20',color='black') 
  
ax.set_xlabel('\nDistrict', size=30, color='#4bb4f2') 
ax.set_ylabel('No. of active cases\n', size=30, color='#4bb4f2') 
  
ax.set_title('Maharashtra District Wise Active Cases\n', 
             size=50,color='#28a9ff') 

plt.bar(x=data['District'],height=data['Active'])
plt.show() #second plot showing district wise active cases

#Plot 3
time_series=pd.read_csv("MahaTimeSeries.csv")
#pulled the day wise data from "https://covidindia.org/open-data/"
#Doc link - "https://docs.google.com/spreadsheets/d/1lgaEhEPfXiLr-88QgtBrEoE-m-lPIpKuIZS7E80EBlY/edit#gid=877650231"
time_series['Date'] = pd.to_datetime(time_series['Date'])
plt.figure(figsize=(30,10))
Y = time_series.iloc[0:,1].values  
X = list(time_series.iloc[0:,0])  
  
ax = plt.axes() 
ax.grid(linewidth=0.5, color='#b8b8b8')  
  
ax.set_facecolor("black")  
ax.set_xlabel('\nMonth',size=30,color='#4bb4f2') 
ax.set_ylabel('No. of Active Cases\n',size=30,color='#4bb4f2') 
  
plt.xticks(rotation='vertical',size='20',color='black') 
plt.yticks(size=20,color='black') 
plt.title("COVID-19 Cases: Maharashtra\n",size=50,color='#28a9ff') 
  
ax.plot(X,Y,linewidth=3)
plt.show() #third plot showing the rise/drop of active cases month wise for the whole state

#Plot 4
time_series=pd.read_csv("MahaTimeSeries.csv")
time_series['Date'] = pd.to_datetime(time_series['Date'])
plt.figure(figsize=(30,10))
Y = time_series.iloc[0:,4].values  
X = list(time_series.iloc[0:,0])  
  
ax = plt.axes() 
ax.grid(linewidth=0.5, color='#b8b8b8')  
  
ax.set_facecolor("black")  
ax.set_xlabel('\nMonth',size=30,color='#4bb4f2') 
ax.set_ylabel('Percentage\n',size=30,color='#4bb4f2') 
  
plt.xticks(rotation='vertical',size='20',color='black') 
plt.yticks(size=20,color='black') 
plt.title("COVID-19 Recovery Rate: Maharashtra\n",size=50,color='#28a9ff') 
  
ax.plot(X,Y,linewidth=3)

plt.show() #fourth plot showing the increasing recovery rate by month

#Plot 5
series=pd.read_csv("MahaTimeSeries.csv")
series['Date'] = pd.to_datetime(series['Date'])
X = list(series.iloc[0:,0]) 
Y = series.iloc[0:,1].values  
Z = series.iloc[0:,4].values 

fig, (ax1,ax2) = plt.subplots(2,sharex=True,figsize=(10,8),gridspec_kw={'hspace': 0 })
fig.suptitle('COVID 19 Monthly : Maharashtra',color='b',size=20)
 
ax1.grid(linewidth=0.5, color='#b8b8b8')  
ax2.grid(linewidth=0.5, color='#b8b8b8')   
# ax1.set_facecolor("black") 
# ax2.set_facecolor("black")  
ax1.set_ylabel('No. of Active Cases\n',size=12,color='b')  
ax2.set_ylabel('%Recovery Rate\n',size=12,color='b')  
plt.xticks(rotation='vertical',size='10',color='black') 

ax1.plot(X, Y)
ax2.plot(X, Z)
plt.show()#subplot showing the inverse ratio of no. of active cases to the recovery rate