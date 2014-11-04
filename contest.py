from sklearn.lda import LDA
from sklearn import cross_validation
import numpy
fp=open('contest_train.csv','r')
s=fp.read()
fp.close()
TrainInp=[]
TrainOutp=[]
for i in s.split('\n')[:-1]:
	TrainInp.append([])
	for j in i.split(',')[:-1]:
		TrainInp[-1].append(float(j))
for i in s.split('\n')[:-1]:
	TrainOutp.append(float(i.split(',')[-1]))
clf = LDA()
scores = cross_validation.cross_val_score(clf,(TrainInp),(TrainOutp),cv=5)
print scores