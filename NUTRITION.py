import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage

data = pd.read_excel("NUTRITION.xlsx",sheat='sheat1')
rating=[]
sugar=[]
for i in xrange(1,len(data)):
    rating.append(float(data["rating"][i]))
    sugar.append(float(data["sugars"][i]))

plt.scatter(rating, sugar, label= "dots", color= "m",marker= ".", s=30)
plt.xlabel('Rating')
plt.ylabel('sugar content')
plt.title('Nutrition Correlation')
print "NEGATIVE CORRELATION"
print np.corrcoef(rating, sugar)[0, 1]
plt.show()
