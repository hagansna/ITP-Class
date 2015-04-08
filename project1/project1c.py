import pandas as pd
import urllib2
import numpy as np

file = urllib2.urlopen('http://web.mta.info/developers/data/nyct/turnstile/turnstile_150321.txt')
data = file.read()
file.close()

data = data.split('\n')
data = [x.split(',') for x in data]

df = pd.DataFrame(data[1:], columns = data[0])

scp = df['SCP'].unique()

lis = []
for item in scp:
    bo = false
    lis2 = []
    for i in range(0,len(df)):
        if df.get_value(i, 'SCP') == item:
            sum = int(df.get_value(i, 'ENTRIES')
            