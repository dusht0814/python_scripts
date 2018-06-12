
# coding: utf-8

# In[40]:



import json
from urllib2 import urlopen

story = urlopen('http://www.floatrates.com/daily/inr.json')
story1 = story.read()
data = json.loads(story1)

for key in data.iterkeys():   
    del data[key]['name']
        

with open('new_currency1.json','w') as f: #w signifies write operation
    json.dump(data,f,indent=2)
    

    




# In[3]:



currency_code = raw_input("Please enter the currency code in which INR is to be converted ")
amount = int(raw_input("Please enter the amount in INR "))
result = amount * data[currency_code]['rate']
print amount,'INR = ',result,currency_code.upper() 

