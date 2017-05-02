import vincent
import twit
import sqlite3
from collections import Counter

def getTags():
    dbconn = sqlite3.connect('tweets.db')
    cur = dbconn.cursor()
    cur.execute('select tags from tweets')
    data = []
    finalData = []
    rows = cur.fetchall()
    for row in rows:
        data.append((list(row)[0].encode("utf-8")[1:-1]).split())
    for row in data:
        for element in row:
            if(element == row[-1]):
                finalData.append(element[2:-1].upper())
            else:
                finalData.append(element[2:-2].upper())
    return finalData

def getLocatins():
    dbconn = sqlite3.connect('tweets.db')
    cur = dbconn.cursor()
    cur.execute('select user_location from tweets')
    data = []
    rows = cur.fetchall()

def processData():
    # twit.gatherTwitterData() uncomment this funciton to get a new set of tweets
    hashtags = Counter(getTags()).most_common(15)
    print hashtags
    labels, freq = zip(*hashtags)
    data = {'data':freq, 'x': labels}
    bar = vincent.Bar(data, iter_idx='x')
    bar.to_json('term_freq.json')

processData()
