#importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

url ="https://covidindia.org/maharashtra/" 
r=requests.get(url,headers={"User-Agent":""}) #Enter your user-agent in the double quotes for the HTTP request
soup=BeautifulSoup(r.text,"html.parser")

data = []
  
# soup.find_all('td') will scrape every element in the url's table 
data_iterator = iter(soup.find_all('td'))
 
while True: 
    try: 
        district = next(data_iterator).text 
        total_cases = next(data_iterator).text 
        recoveries = next(data_iterator).text 
        deaths = next(data_iterator).text 
        active_cases = next(data_iterator).text 

        data.append((district,total_cases,recoveries,deaths,active_cases))
        # StopIteration error is raised when there are no more elements left to iterate
    except StopIteration: 
        break

#Converting the list of data into a DataFrame
df=pd.DataFrame(data)
headers=["District","Total_Cases","Recoveries","Death","Active"]
df.to_csv("MahaCovid.csv",index=False, header=headers) #Creating a csv file in your directory

