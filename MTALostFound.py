'''
Scrapes and parses the MTA's lost and found list, which is kept in XML format
and refreshed every hour. Currently outputs a pandas DataFrame that shows
the main categories of items found in order of most in MTA's possession,
the count of the total number of items in each category, and the proportion
of the total number of items found that each category makes up.

A possible contender for submission for project one.

Author: Nicholas Hagans
Version: 4/5/15
'''

import urllib2, xmltodict
import pandas as pd
import csv, os, sys

file = urllib2.urlopen('http://advisory.mtanyct.info/LPUWebServices/CurrentLostProperty.aspx')
data = file.read()
file.close()

with open('lostitems.xml', 'wb') as f:
    f.write(data)

data = xmltodict.parse(data)

lostAndFound = {}
lAF = {}
for category in data['LostProperty']['Category']:
    sum = 0
    lostAndFound[str(category['@Category'])] = {}
    lAF[str(category['@Category'])] = {}
    for sub in category['SubCategory']:
        sum +=  int(sub['@count'])
        lAF[str(category['@Category'])][str(sub['@SubCategory'])] = int(sub['@count'])
        #lostAndFound[str(category['@Category'])][str(sub['@SubCategory'])] = int(sub['@count'])
    lostAndFound[str(category['@Category'])] = sum

totalLost = int(data['LostProperty']['NumberOfLostArticles'])
df = pd.DataFrame(lostAndFound.items(), columns = ['Item', 'Count'])
df = df.sort(columns = ['Count'], ascending = False)

df['Proportion'] = df['Count']/float(df['Count'].sum())
