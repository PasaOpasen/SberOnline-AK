# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 21:48:41 2020

@author: qtckp
"""






import numpy as np
with open('cleaned2987.txt','r', encoding = 'utf-16') as f:
    #lines = [line.split() for line in f.readlines()]
    lines = [line.strip() for line in f.readlines()]
    sentences = [line[:-2] for line in lines]
    stars = np.array(np.array([int(s[-1]) for s in lines])>3)




from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis, LinearDiscriminantAnalysis
from sklearn.metrics import classification_report
from sklearn.linear_model import SGDClassifier
from sklearn import linear_model
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn
import pickle


y = stars
np.sum(y>0)/len(y)

model = TfidfVectorizer()
X = model.fit_transform(sentences)

pickle.dump(model, open('tfidf.model', 'wb'))


models = [
    #("Linear SVM",LinearSVC(C=1,verbose=1)),
    #('sgd',SGDClassifier()),
    ##("Decision Tree",DecisionTreeClassifier(max_depth=3)),
    #("Random Forest",RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1,verbose=True)),
    ##("Neural Net",MLPClassifier(alpha=1, max_iter=1000,verbose=True)),
    ##("AdaBoost",AdaBoostClassifier()),
    #("Naive Bayes gau",GaussianNB()),
    #("LDA",LinearDiscriminantAnalysis()),
    ##("QDA",QuadraticDiscriminantAnalysis()),
    ('logreg',LogisticRegression()),
    ('ridge', linear_model.RidgeClassifier(alpha=0.1)),
    ##('Grad Boost',sklearn.ensemble.GradientBoostingClassifier())
    ]



X = X.toarray()

X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=.2, train_size=.8, shuffle = True )

X_train, X_valid, y_train, y_valid =  train_test_split(X_train, y_train, test_size=.2, train_size=.5, shuffle = True )



results = {}

for name, clf in models:
    print('Now: {}'.format(name))

    clf.fit(X_train, y_train)
    #score = clf.score(X_test, y_test[:,i])
    print(clf.score(X_test, y_test))
    v = f1_score(y_test, clf.predict(X_test))

    #print(classification_report(y_test, clf.predict(X_test), digits = 7))
    print("model = {}  score = {}".format(name,v))
    
    results[name] = v




print('---> LSVM')
for C in (0.1, 0.5, 1):
    clf = LinearSVC(C=C, verbose=1)
    clf.fit(X_train, y_train)

    v = f1_score(y_valid, clf.predict(X_valid))
    
    print(f'C = {C}, score = {v}')



print('---> RF')
for mx in (1, 3, 5):
    for d in (3, 5, 7):
        for n in (10, 15, 20):
            clf = RandomForestClassifier(max_depth=d, n_estimators=n, max_features=mx, verbose=0)
            clf.fit(X_train, y_train)
        
            v = f1_score(y_valid, clf.predict(X_valid))
            
            print(f'max_features = {mx}, depth = {d}, n = {n}, score = {v}')









fits=[
     ("Linear SVM",LinearSVC(C=0.5,verbose=1)),
    ('sgd',SGDClassifier()),
    ("Naive Bayes gau",GaussianNB()),
    ('logreg',LogisticRegression()),
    ('ridge', linear_model.RidgeClassifier(alpha=0.1)),   
      ]

for name, clf in fits:
    print(name)
    clf.fit(X_train, y_train)




from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score



di = {}
    
for ind, (name, fit) in enumerate(fits[3:]):
    X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=.2, train_size=.8, shuffle = True )
    fit.fit(X_train, y_train)
    if ind < 2:
        lr_probs = fit.decision_function(X_test)
    else:
        lr_probs = fit.predict_proba(X_test)
        lr_probs = lr_probs[:, 1]
    # keep probabilities for the positive outcome only
        
    
    # calculate scores
    
    lr_auc = roc_auc_score(y_test, lr_probs)
    # summarize scores
    
    print(f'{name}: ROC AUC=%.3f' % (lr_auc))
    # calculate roc curves
   
    lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs)
    # plot the roc curve for the model
    di[name] = (lr_fpr, lr_tpr)
    #plt.plot(lr_fpr, lr_tpr, label= name)


new_key = ["Naive Bayes", 'LogReg', 'Ridge', 'SGD']
old_key = ["Naive Bayes gau", 'logreg', 'ridge', 'sgd']
for new, old in zip(new_key, old_key):
    di[new] = di.pop(old)



X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=.2, train_size=.8, shuffle = True )  


for name, (l, r) in di.items():

    plt.plot(l, r, label= f'{name} ({sklearn.metrics.auc(l, r):.3})')


ns_probs = [0 for _ in range(len(y_test))]

ns_auc = roc_auc_score(y_test, ns_probs)
print('No Skill: ROC AUC=%.3f' % (ns_auc))
ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)
plt.plot(ns_fpr, ns_tpr, linestyle='--', label='Random (0.5)')
    # axis labels
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
    # show the legend
plt.legend()

plt.title('ROC-curves')
    # show the plot
plt.savefig('rocs.png', dpi = 350)
plt.show()




import pickle
 
with open('config2.dictionary', 'wb') as config_dictionary_file:
  pickle.dump(di, config_dictionary_file)


with open('config.dictionary', 'rb') as config_dictionary_file:
    di2 = pickle.load(config_dictionary_file)
 

logreg = LogisticRegression().fit(X, y)


pickle.dump(logreg, open('logreg.model', 'wb'))


















