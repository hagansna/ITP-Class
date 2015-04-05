'''
Python script that uses the capitolwords api to find which political party says which words
more often. The script first finds the total number of times each word was said
for each party since the collection of the data set (1995). It then plots a
barchart showing which party said each word the most.

A possible contender for submission for project one.

Author: Nicholas Hagans
Version: 4/5/15

'''

import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from keys import SUNLIGHT_API_KEY
#
#emotions = ["happy", "joy", "sad", "love", "hate", "anger", "cry", "feel", "hope", "faith"]
races = ["race", "blacks","african americans", "hispanics", "whites"]
parties = ["D", "R"]

lis = []
for party in parties:
    lis2 = []
    for race in races:
        count = 0
        query_params = { 'apikey': SUNLIGHT_API_KEY,
                        'phrase': race,
                        'party': party,
                        'granularity': 'year',
                        'percentages': 'true',
                        'mincount': '0'
                        }

        endpoint = 'http://capitolwords.org/api/dates.json'

        response = requests.get(endpoint, params=query_params)
        data=response.json()

        for i in range(0,len(data['results'])):
            count += data['results'][i]['count']
            #count = data['results'][i]['count']
            #year = data['results'][i]['year']
            #lis2.append((int(year), emotion, count))
        lis2.append((race, count))
    lis.append(lis2)

dems = lis[0]
reps = lis[1]

repsdf = pd.DataFrame(reps, columns = ['Race', 'Count'])
demsdf = pd.DataFrame(dems, columns = ['Race', 'Count'])

p1 = plt.bar(repsdf.index,repsdf['Count'], .5, color = 'r')
p2 = plt.bar(demsdf.index+.5, demsdf['Count'], .5, color = 'b')

plt.xticks(np.arange(len(repsdf))+.5, tuple(repsdf['Race']))
plt.legend( (p1[0], p2[0]), ('Republicans', 'Democrats') )

plt.show()
