
# coding: utf-8

# In[33]:


import json
from urllib2 import urlopen

story = urlopen('http://www.floatrates.com/daily/inr.json')
story1 = story.read()
data = json.loads(story1)
#print json.dumps(data, indent=2) #remove comment to see the json file


# In[38]:


currency_code = raw_input("Please enter the currency code in which INR is to be converted ")
amount = int(raw_input("Please enter the amount in INR "))
result = amount * data[currency_code]['rate']
print amount,'INR = ',result,currency_code.upper() 
    

