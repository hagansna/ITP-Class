'''
Python script that uses the capitolwords api and Python wrapper. This can
accomplish the same task as project1a.py but is cleaner as it uses sunlight's
python wrapper.

Author: Nicholas Hagans
Version: 4/5/15
'''

from keys import SUNLIGHT_API_KEY

SUNLIGHT_API_KEY = SUNLIGHT_API_KEY
import sunlight

emotions = ["happy", "sad", "angry", "love", "hate"]

for emotion in emotions:
    lis = sunlight.services.capitolwords.CapitolWords.dates(self, emotion, party='R', granularity="year", percentages=True, mincount=0)
