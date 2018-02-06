import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage

data = pd.read_excel("SALARY.xlsx",sheat='sheat1')
Overtime_Pay=[]
Other_Pay=[] 
benefits=[]
Basic_Pay=[]
total=[]
for i in xrange(0,len(data)):
	if (data["Year"][i]==2014):
		if (data["OvertimePay"][i]!="Not Provided"):
			Overtime_Pay.append(float(data["OvertimePay"][i]))
		if (data["OtherPay"][i]!="Not Provided"):
			Other_Pay.append(float(data["OtherPay"][i]))
		if (data["Benefits"][i]!="Not Provided"):
			benefits.append(float(data["Benefits"][i]))
		if ((data["OvertimePay"][i]!="Not Provided") and (data["OtherPay"][i]!="Not Provided" )and (data["Benefits"][i]!="Not Provided")):
			total.append(float(data["OvertimePay"][i])+float(data["OtherPay"][i])+float(data["Benefits"][i]))
		if (data["BasePay"][i]!="Not Provided"):
			Basic_Pay.append(float(data["BasePay"][i]))

print "Benifits vs Basic Pay:"+str(np.corrcoef(benefits, Basic_Pay)[0, 1])
print "Overtime Pay vs Basic Pay:"+str(np.corrcoef(Overtime_Pay, Basic_Pay)[0, 1])
print "Other_Pay vs Basic Pay:"+str(np.corrcoef(Other_Pay, Basic_Pay)[0, 1])

plt.scatter(total, Basic_Pay, label= "dots", color= "m",marker= ".", s=30)
plt.xlabel('Extra Pay')
plt.ylabel('Basic Pay')
plt.title('SALARY Ploat')
plt.show()
