import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



data = pd.read_excel("MOVIE.xlsx",sheat='sheat1')
imdb_score=[]
for i in xrange(1,len(data)):
    imdb_score.append(float(data["Column 27"][i]))
mean = np.mean(imdb_score)
std_Dev=np.std(imdb_score)
print ("Population mean:"+str(mean))
print ("Population Standard deviation:"+str(std_Dev))
print ("Population length:"+str(len(data)))

######################### Script to get Data of 2016 movies using web srcapping#################

import bs4
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

url="http://www.imdb.com/list/ls070941500/"
page =uReq(url)
page_html=page.read()
page.close()

page_soup=soup(page_html,"lxml")
# print page_soup
movie=page_soup.findAll("div",{"class":"info"})
file = open("imdb_2016.txt","w")
imdb_score2016=[]
for x in xrange(0,len(movie)):
	movie_name=movie[x].b.a.get_text()
	imdb_score=movie[x].div.findAll("span",{"class":"value"})[0].get_text()	
	imdb_score2016.append(float(imdb_score))
	file.write(str(x)+". \t"+movie_name+"\t\t\t\t\t\t\t\t\t"+ imdb_score+"\n")
file.close()

SampleMean=np.mean(imdb_score2016)
Sample_std_dev=np.std(imdb_score2016)
print ("Sampel mean:"+str(SampleMean))
print ("Sample Standard deviation:"+str(Sample_std_dev))
print ("Sample size:"+str(len(imdb_score2016)))


######################## Hypothesis Proof #########################################

# (i)

# step 1:
# 	H0:mean(2016)>Mean(till 2015)
# 	H1:mean(2016)<=Mean(till 2015)

# step 2:
# 	z -distribution will used
# 	degree of freedom=65
# 	alfa=0.05
#	1.96
# step 3:
# 	z=(Sample mean - Population mean)/(Population Standard deviation/root(size of sample))
# 	z=-3.16855	
# step 4:
# 	H0 is accepted
# step 5:
# 	popularity of films increases


############################## (ii) ################

# step 1:
# 	H0:mean(2016)>Mean(till 2015)
# 	H1:mean(2016)<=Mean(till 2015)

# step 2:
# 	t-distribution will used
# 	degree of freedom=65
# 	alfa=0.05
#	2.00
# step 3:
# 	t=(Sample mean - Population mean)/(Sample Standard deviation/root(size of sample))
# 	t= -2.16	
# step 4:
# 	H0 is accepted
# step 5:
# 	popularity of films increases
