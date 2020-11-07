import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

test = pd.read_csv("test.csv")
train = pd.read_csv("train.csv")

X = train[['battery_power', 'blue','clock_speed','dual_sim','fc','four_g','int_memory', 'm_dep','mobile_wt',
          'n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi']].values
Y = train['price_range'].values
p = np.random.permutation(len(X)) #tao ra hoan vi ngau nhien trong X de chia ra train

# Chia gia tri trong tap train thanh 2 phan de train trong train
x_train = X[p[:int(0.8*len(X))]].copy()
y_train = Y[p[:int(0.8*len(X))]].copy()

x_test = X[p[int(0.8*len(X)):]].copy()
y_test = Y[p[int(0.8*len(X)):]].copy()

#train bang knn
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(11) #
knn.fit(x_train, y_train) #dieu chinh mo hinh x_train : du lieu, y_train : dich

#test
result = knn.predict(x_test) #predict(x_test) : du doan lop cho du lieu dc cung cap la x_test
# for i in range(10) :
#     print(' result = {0} , y_test = {1} '.format(result[i], y_test[i]))
print(' kq lech : ', len(result[result != y_test]) ,'/',len(y_test))

#Tinh accuracy
from sklearn.metrics import accuracy_score
E = accuracy_score(y_test, result)
print(' Accurary : ', E)

#test bang bo test
X_Test = test[['battery_power', 'blue','clock_speed','dual_sim','fc','four_g','int_memory', 'm_dep','mobile_wt',
          'n_cores','pc','px_height','px_width','ram','sc_h','sc_w','talk_time','three_g','touch_screen','wifi']].values
result_test = knn.predict(X_Test)
# print(len(result_test))

#ghi them vao file test du lieu da test
test['price_range(banghamcosan)'] = result_test
test.to_csv('test.csv')

print('end')


