from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor

boston = load_boston()

print (boston.DESCR)
X = boston.data
y = boston.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.25)


print ("The max target value is", np.max(boston.target))
print ("The min target value is", np.min(boston.target))


ss_x = StandardScaler()
ss_y = StandardScaler()

X_train = ss_x.fit_transform(X_train)
X_test = ss_x.transform(X_test)

y_train = ss_y.fit_transform(y_train)
y_test = ss_y.transform(y_test)

#print X_train
print y_train

#print X_train
print y_train


lr = LinearRegression()

lr.fit(X_train, y_train)

lr_y_predict = lr.predict(X_test)

sgdr = SGDRegressor()

sgdr.fit(X_train, y_train)

sgdr_y_predict = sgdr.predict(X_test)


print 'The value of default measurement of LinearRegression is', lr.score(X_test, y_test)


from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


print 'The value of R-squared of LinearRegression is', r2_score(y_test, lr_y_predict)


print 'The mean squared error of LinearRegression is', mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(lr_y_predict))


print 'The mean absoluate error of LinearRegression is', mean_absolute_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(lr_y_predict))


print 'The value of default measurement of SGDRegressor is', sgdr.score(X_test, y_test)


print 'The value of R-squared of SGDRegressor is', r2_score(y_test, sgdr_y_predict)


print 'The mean squared error of SGDRegressor is', mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(sgdr_y_predict))


print 'The mean absoluate error of SGDRegressor is', mean_absolute_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(sgdr_y_predict))
