import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage

data = pd.read_excel("GAMES.xlsx",sheat='sheat1')
Year_of_Release=[]
Rating=[]
for i in xrange(0,len(data)):
    Year_of_Release.append(data["Year_of_Release"][i])
    Rating.append(data["Rating"][i])

df=pd.DataFrame({'Year_of_Release' :Year_of_Release,'Rating':Rating})
s = df.groupby('Year_of_Release').agg({'Rating': ['count']}).reset_index(level=0)
s.columns = [col[1] if col[1] else col[0] for col in s.columns.tolist()]
print s
print "Hypothesis:Action video game is highly rated among teens."
print "Hypothesis is true."

plt.scatter(s["Year_of_Release"],s["count"], label= "dots", color= "m",marker= ".", s=30)
plt.xlabel('Year_of_Release')
plt.ylabel('Rating')
plt.title('Game rating')
plt.show()
