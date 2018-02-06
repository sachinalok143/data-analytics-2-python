import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage
# %matplotlib inline

data = pd.read_excel("SNACKS.xls",sheat='sheat1')
Liking_scores=[]
Saltiness=[]
Sweetness=[]
Acidity=[]
Crunchiness=[]
for i in xrange(1,len(data)):
    Liking_scores.append(float(data["Liking scores"][i]))
    Saltiness.append(float(data["Saltiness"][i]))
    Sweetness.append(float(data["Sweetness"][i]))
    Acidity.append(float(data["Acidity"][i]))
    Crunchiness.append(float(data["Crunchiness"][i]))
 # corr=dataframe.corr()
 # print corr
data=data[0:len(data)]
# print data


def correlation_matrix(data):
    from matplotlib import pyplot as plt
    from matplotlib import cm as cm

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap('jet', 30)
    cax = ax1.imshow(data.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title('Snaks correlation matrix')
    labels=['Liking scores','Saltiness','Sweetness','Acidity','Crunchiness']
    ax1.set_xticklabels(labels,fontsize=10)
    ax1.set_yticklabels(labels,fontsize=10)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    fig.colorbar(cax, ticks=[0,.05,.10,.15,.20,.25,.30,.35,.40,.45,.50,.55,.60,.65,.70,.75,.8,.85,.90,.95,1])
    plt.show()

correlation_matrix(data)

def polyfit(x, y, degree):
    results = {}

    coeffs = np.polyfit(x, y, degree)

     # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot

    return results

cofOfDet=polyfit(Liking_scores,Saltiness,1.5)
print cofOfDet
print polyfit(Acidity,Saltiness,1.5)
print polyfit(Crunchiness,Sweetness,1.5)
print polyfit(Liking_scores,Saltiness,1.5)
print polyfit(Crunchiness,Saltiness,1.5)
print polyfit(Crunchiness,Saltiness,1.5)