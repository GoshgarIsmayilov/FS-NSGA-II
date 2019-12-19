#imports
import time
import numpy as np
from sklearn import preprocessing
from sklearn.svm import LinearSVC
from sklearn.model_selection import LeaveOneOut

def label_decision(main):
    decision = 0
    
    if "EWS" in main:
        decision = 1
    elif "BL" in main:
        decision = 2
    elif "NB" in main:
        decision = 3
    elif "RMS" in main:
        decision = 4
     
    return decision

readings,samples,labels = [], [], []
dummy = []
train_length = 63 

# reading file
with open('Datasets/SRBCT_DATASET.txt', 'r') as f:
    x = f.readlines()

for i in range(len(x)-1):
    arr = x[1+i].split('\t')
    readings.append(arr)

for j in range(2,len(readings[0])):
    for i in range(len(readings)):
        dummy.append(readings[i][::j][1])
    samples.append(dummy);
    dummy = list()
    
# label creation
for i in range(len(samples)):
    labels.append (label_decision(samples[i][0]))
    samples[i].pop(0)

samples = preprocessing.MinMaxScaler().fit_transform(samples[:train_length])
labels = np.asarray(labels[:train_length])

indexes           = np.array([1,2,3,4])
scores            = []
loo               = LeaveOneOut()
number_of_classes = np.max(labels)
batch_size        = 1
epochs            = 5

start_time = time.time()
for train_index, test_index in loo.split(samples):
    x_train, x_test = samples[train_index], samples[test_index]
    y_train, y_test = labels[train_index], labels[test_index]
    
    X_train = x_train[:, indexes]
    X_test = x_test[:, indexes]
    Y_train = y_train[:]
    Y_test = y_test[:]
    
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    Y_train = Y_train[:]
    Y_test = Y_test[:]
    
    clf = LinearSVC(random_state=0)
    clf.fit(X_train, Y_train)
    score = clf.score(X_test, Y_test)
    scores.append(score)
end_time = time.time()


print('Score: ' + str(np.average(scores)))
print('Time: ' + str(end_time - start_time))
