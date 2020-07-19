import requests
# from openpyxl import Workbook
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import pandas as pd


df = pd.DataFrame()
output = []
counter = 0
while True:
    r = requests.get("https://api.thingspeak.com/channels/1091564/feeds.json?api_key=UI3L8BT1NRQHWQ87&results=1")
    
    channelDict = r.json()

    feedsList = channelDict['feeds']
    counter = counter + 1
    field1Values=[]

    for everyitem in feedsList:
        field1Values.append(int(everyitem['field1']))
    print(field1Values[0])  
    # output.append(field1Values[0])
    # df['field1'] = pd.Series(output) 
    
    # file2 = open(r"C:\Users\Admin\Desktop\out.txt","a") 
    # file2.writelines(str(counter) +","+str(field1Values[0]) + "\n")
    # file2.close()

    time.sleep(1)
    # df.to_csv("C:/Users/Admin/Desktop/output.csv")

# print(df)
    
    