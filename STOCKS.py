import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage

data = pd.read_excel("STOCKS.xlsx",sheat='sheat1')
Volume=[]
Date=[]
for i in xrange(0,len(data)):
    Volume.append(data["Volume"][i])
    Date.append(data["Date"][i])

plt.scatter(Volume,Date, label= "dots", color= "m",marker= ".", s=30)
plt.xlabel('Volume')
plt.ylabel('Date')
plt.title('Stok prediction')
plt.show()
