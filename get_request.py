# id = 1HeL0DakMig9K8adPVwghrr4DQDnjyaurP4ybMn9CWbA

import requests
import time


url = 'https://script.google.com/macros/s/AKfycbxjMh8pkAvXUhlNrpHFn4mNDaqUN0lrtBP5-0SrmZZbOpdjfshAfn0FBw/exec'
for x in range(200):
    myobj = {'seconds': x}
    time.sleep(5)
    y = requests.post(url, data=myobj)
