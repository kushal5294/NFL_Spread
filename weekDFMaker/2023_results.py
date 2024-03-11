#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:10:42 2023

@author: kushal
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
column = ["Week", "Time", "Away", "Home"]
ml = []
year = "_2023"
url = requests.get ("https://www.pro-football-reference.com/years/2023/games.htm")

soup = BeautifulSoup(url.text, 'html.parser')

teamStatTable = soup.find("div", attrs = {'id':'div_games'}).find('table').find("tbody")
   
   
teamRows = teamStatTable.find_all("tr")
count = 0;

for row in teamRows:
   print(count)
   if (count >= 289 ):
       df = pd.DataFrame(ml, columns=column)
       df.to_csv("scrape.csv")
       break
   if ( (row.has_attr("class"))):
       count = count +1
       continue
   
   else:
     columns = row.find_all("td")
     Week = row.find("th").text
     Time = columns[2].text
     swap = columns[4].text == '@'
     
     if (swap): # away is the winner
         Away = columns[3].text
         Home = columns[5].text
        # AwayPoints = int(columns[7].text)
        # HomePoints = int(columns[8].text)
         
     else: #home is winner
       Away = columns[5].text
       Home = columns[3].text
       #AwayPoints = int(columns[8].text)
       #HomePoints = int(columns[7].text)
       
     #Diff = HomePoints - AwayPoints
     Away = Away + year
     Home = Home + year
     stats = [Week, Time, Away, Home]
     ml.append(stats)
     print (stats)
   
     count  = count +1

df = pd.DataFrame(ml, columns=column)
df.to_csv("scrape.csv")

     
