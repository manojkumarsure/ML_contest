from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import sys
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from mpl_toolkits.mplot3d import Axes3D
from sklearn import cross_validation
from scipy import stats
from sklearn import svm, grid_search, datasets
from sklearn.svm import SVC

f = open(sys.argv[1])

x = []
y = []
y_res = []
i=0

for line in f:
	x.append([])
	line1 = line.strip().split(",")
	for k in line1[:-1]:
		if k == 'NaN':
			k = 1
		x[i].append(float(k))
	if line1[-1] == '1':
		y.append(int(0))
	else:
		y.append(int(1))
	i+=1;
	dir 

x=np.array(x)
y=np.array(y)
	

bdt = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2),
                         algorithm="SAMME.R",
                         n_estimators=50)

bdt.fit(x, y)

scores = cross_validation.cross_val_score(bdt, x, y, cv=5)
print (scores)	

